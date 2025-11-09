from django.test import TestCase
from django.core.exceptions import ValidationError
from django.core.files.uploadedfile import SimpleUploadedFile
from django.db import IntegrityError
from unittest.mock import patch, MagicMock
from io import BytesIO
from PIL import Image

from apps.employee.models import Employee, validate_image
from apps.employee.card_utils import get_id_card_photo, textsize


class ValidateImageTest(TestCase):
    """Tests for the validate_image function"""

    def create_test_image(self, size_kb=100, format='JPEG'):
        """Helper method to create test images of specific sizes"""
        image = Image.new('RGB', (100, 100), color='red')
        image_io = BytesIO()
        image.save(image_io, format=format)
        image_io.seek(0)

        # Pad to desired size
        current_size = len(image_io.getvalue())
        target_size = size_kb * 1024
        if current_size < target_size:
            padding = b'\0' * (target_size - current_size)
            image_io.write(padding)

        image_io.seek(0)
        return image_io

    def test_validate_image_valid_jpeg(self):
        """Test that valid JPEG images pass validation"""
        image_io = self.create_test_image(size_kb=100, format='JPEG')
        uploaded_file = SimpleUploadedFile(
            "test_image.jpg",
            image_io.getvalue(),
            content_type="image/jpeg"
        )

        # Should not raise ValidationError
        try:
            validate_image(uploaded_file)
        except ValidationError:
            self.fail("validate_image raised ValidationError unexpectedly!")

    def test_validate_image_too_large(self):
        """Test that images larger than 2MB fail validation"""
        image_io = self.create_test_image(size_kb=2100, format='JPEG')  # 2.1 MB
        uploaded_file = SimpleUploadedFile(
            "large_image.jpg",
            image_io.getvalue(),
            content_type="image/jpeg"
        )

        with self.assertRaises(ValidationError) as context:
            validate_image(uploaded_file)

        self.assertIn('too large', str(context.exception))

    def test_validate_image_invalid_format(self):
        """Test that non-JPEG images fail validation"""
        image_io = self.create_test_image(size_kb=100, format='PNG')
        uploaded_file = SimpleUploadedFile(
            "test_image.png",
            image_io.getvalue(),
            content_type="image/png"
        )

        with self.assertRaises(ValidationError) as context:
            validate_image(uploaded_file)

        self.assertIn('not supported', str(context.exception))


class EmployeeModelTest(TestCase):
    """Tests for the Employee model"""

    def create_test_image_file(self, filename="test.jpg"):
        """Helper method to create a valid test image file"""
        image = Image.new('RGB', (100, 100), color='blue')
        image_io = BytesIO()
        image.save(image_io, format='JPEG')
        image_io.seek(0)

        return SimpleUploadedFile(
            filename,
            image_io.getvalue(),
            content_type="image/jpeg"
        )

    @patch('apps.employee.models.get_id_card_photo')
    def test_create_employee_success(self, mock_get_id_card):
        """Test creating an employee with valid data"""
        # Mock the ID card generation
        mock_id_card = MagicMock()
        mock_id_card.read.return_value = b'fake_id_card_data'
        mock_get_id_card.return_value = mock_id_card

        photo = self.create_test_image_file()

        employee = Employee.objects.create(
            first_name='John',
            last_name='Doe',
            designation='Software Engineer',
            email='john.doe@example.com',
            phone='1234567890',
            photo=photo
        )

        self.assertEqual(employee.first_name, 'John')
        self.assertEqual(employee.last_name, 'Doe')
        self.assertEqual(employee.designation, 'Software Engineer')
        self.assertEqual(employee.email, 'john.doe@example.com')
        self.assertEqual(employee.phone, '1234567890')
        self.assertIsNotNone(employee.created_at)
        self.assertIsNotNone(employee.updated_at)

        # Verify ID card generation was called
        mock_get_id_card.assert_called_once()

    @patch('apps.employee.models.get_id_card_photo')
    def test_employee_str_representation(self, mock_get_id_card):
        """Test the string representation of an employee"""
        mock_id_card = MagicMock()
        mock_id_card.read.return_value = b'fake_id_card_data'
        mock_get_id_card.return_value = mock_id_card

        photo = self.create_test_image_file()

        employee = Employee.objects.create(
            first_name='Jane',
            last_name='Smith',
            designation='Designer',
            email='jane.smith@example.com',
            phone='0987654321',
            photo=photo
        )

        self.assertEqual(str(employee), 'Jane Smith')

    @patch('apps.employee.models.get_id_card_photo')
    def test_employee_unique_email(self, mock_get_id_card):
        """Test that employee emails must be unique"""
        mock_id_card = MagicMock()
        mock_id_card.read.return_value = b'fake_id_card_data'
        mock_get_id_card.return_value = mock_id_card

        photo1 = self.create_test_image_file('test1.jpg')
        photo2 = self.create_test_image_file('test2.jpg')

        # Create first employee
        Employee.objects.create(
            first_name='John',
            last_name='Doe',
            designation='Engineer',
            email='duplicate@example.com',
            phone='1111111111',
            photo=photo1
        )

        # Try to create second employee with same email
        with self.assertRaises(IntegrityError):
            Employee.objects.create(
                first_name='Jane',
                last_name='Doe',
                designation='Designer',
                email='duplicate@example.com',
                phone='2222222222',
                photo=photo2
            )

    @patch('apps.employee.models.get_id_card_photo')
    def test_employee_id_card_generation_on_save(self, mock_get_id_card):
        """Test that ID card is generated when employee is saved"""
        mock_id_card = MagicMock()
        mock_id_card.read.return_value = b'fake_id_card_data'
        mock_get_id_card.return_value = mock_id_card

        photo = self.create_test_image_file()

        employee = Employee.objects.create(
            first_name='Bob',
            last_name='Johnson',
            designation='Manager',
            email='bob.johnson@example.com',
            phone='5555555555',
            photo=photo
        )

        # Verify ID card generation was called with the employee instance
        mock_get_id_card.assert_called_once_with(employee)
        self.assertIsNotNone(employee.id_card_photo)

    @patch('apps.employee.models.get_id_card_photo')
    def test_employee_fields_max_length(self, mock_get_id_card):
        """Test that employee fields respect max_length constraints"""
        mock_id_card = MagicMock()
        mock_id_card.read.return_value = b'fake_id_card_data'
        mock_get_id_card.return_value = mock_id_card

        photo = self.create_test_image_file()

        # Create employee with maximum length fields
        employee = Employee.objects.create(
            first_name='A' * 50,
            last_name='B' * 50,
            designation='C' * 50,
            email='test@example.com',
            phone='1' * 15,
            photo=photo
        )

        self.assertEqual(len(employee.first_name), 50)
        self.assertEqual(len(employee.last_name), 50)
        self.assertEqual(len(employee.designation), 50)
        self.assertEqual(len(employee.phone), 15)


class CardUtilsTest(TestCase):
    """Tests for card_utils.py functions"""

    def test_textsize_function(self):
        """Test the textsize helper function"""
        from PIL import ImageFont
        from django.conf import settings
        import os

        font = ImageFont.truetype(
            os.path.join(settings.BASE_DIR, 'fonts/Montserrat-Bold.ttf'),
            size=40
        )

        width, height = textsize('Test Text', font)

        # Verify that width and height are positive integers
        self.assertIsInstance(width, int)
        self.assertIsInstance(height, int)
        self.assertGreater(width, 0)
        self.assertGreater(height, 0)

    @patch('apps.employee.models.get_id_card_photo')
    def test_get_id_card_photo_returns_content_file(self, mock_get_id_card):
        """Test that get_id_card_photo returns a ContentFile"""
        from django.core.files.base import ContentFile

        # Create a mock employee
        mock_employee = MagicMock()
        mock_employee.first_name = 'Test'
        mock_employee.last_name = 'User'
        mock_employee.designation = 'Tester'
        mock_employee.email = 'test@example.com'

        # Create a test image for the employee photo
        image = Image.new('RGB', (200, 200), color='green')
        image_io = BytesIO()
        image.save(image_io, format='JPEG')
        image_io.seek(0)
        mock_employee.photo = image_io

        # Call the actual function (not mocked)
        mock_get_id_card.side_effect = lambda instance: get_id_card_photo(instance)

        result = mock_get_id_card(mock_employee)

        # Verify it returns a ContentFile
        self.assertIsInstance(result, ContentFile)
