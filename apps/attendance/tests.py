from django.test import TestCase, Client
from django.contrib.auth.models import User, Group
from django.urls import reverse
from django.conf import settings
from unittest.mock import patch, MagicMock
from io import BytesIO
from PIL import Image
from django.core.files.uploadedfile import SimpleUploadedFile
import json

from apps.employee.models import Employee
from apps.attendance.models import Attendance
from apps.attendance.mixins import AttendanceGroupRequiredMixin


class AttendanceModelTest(TestCase):
    """Tests for the Attendance model"""

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
    def test_create_attendance(self, mock_get_id_card):
        """Test creating an attendance record"""
        # Mock ID card generation
        mock_id_card = MagicMock()
        mock_id_card.read.return_value = b'fake_id_card_data'
        mock_get_id_card.return_value = mock_id_card

        # Create an employee
        photo = self.create_test_image_file()
        employee = Employee.objects.create(
            first_name='John',
            last_name='Doe',
            designation='Developer',
            email='john.doe@example.com',
            phone='1234567890',
            photo=photo
        )

        # Create attendance record
        attendance = Attendance.objects.create(
            employee=employee,
            status=Attendance.Status.CHECK_IN
        )

        self.assertEqual(attendance.employee, employee)
        self.assertEqual(attendance.status, Attendance.Status.CHECK_IN)
        self.assertIsNotNone(attendance.created_at)
        self.assertIsNotNone(attendance.updated_at)

    @patch('apps.employee.models.get_id_card_photo')
    def test_attendance_default_status(self, mock_get_id_card):
        """Test that attendance has default status of UNKNOWN"""
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

        # Create attendance without specifying status
        attendance = Attendance.objects.create(employee=employee)

        self.assertEqual(attendance.status, Attendance.Status.UNKNOWN)

    @patch('apps.employee.models.get_id_card_photo')
    def test_attendance_str_representation(self, mock_get_id_card):
        """Test the string representation of attendance"""
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

        attendance = Attendance.objects.create(employee=employee)

        # Verify string representation includes employee name and date
        str_repr = str(attendance)
        self.assertIn('Bob Johnson', str_repr)
        self.assertRegex(str_repr, r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}')

    @patch('apps.employee.models.get_id_card_photo')
    def test_attendance_status_choices(self, mock_get_id_card):
        """Test all attendance status choices"""
        mock_id_card = MagicMock()
        mock_id_card.read.return_value = b'fake_id_card_data'
        mock_get_id_card.return_value = mock_id_card

        photo = self.create_test_image_file()
        employee = Employee.objects.create(
            first_name='Test',
            last_name='User',
            designation='Tester',
            email='test.user@example.com',
            phone='1111111111',
            photo=photo
        )

        # Test CHECK_IN status
        attendance1 = Attendance.objects.create(
            employee=employee,
            status=Attendance.Status.CHECK_IN
        )
        self.assertEqual(attendance1.status, 'Check In')

        # Test CHECK_OUT status
        attendance2 = Attendance.objects.create(
            employee=employee,
            status=Attendance.Status.CHECK_OUT
        )
        self.assertEqual(attendance2.status, 'Check Out')

        # Test UNKNOWN status
        attendance3 = Attendance.objects.create(
            employee=employee,
            status=Attendance.Status.UNKNOWN
        )
        self.assertEqual(attendance3.status, 'Unknown')

    @patch('apps.employee.models.get_id_card_photo')
    def test_attendance_cascade_delete(self, mock_get_id_card):
        """Test that attendance is deleted when employee is deleted"""
        mock_id_card = MagicMock()
        mock_id_card.read.return_value = b'fake_id_card_data'
        mock_get_id_card.return_value = mock_id_card

        photo = self.create_test_image_file()
        employee = Employee.objects.create(
            first_name='Delete',
            last_name='Test',
            designation='Tester',
            email='delete.test@example.com',
            phone='9999999999',
            photo=photo
        )

        # Create attendance
        attendance = Attendance.objects.create(employee=employee)
        attendance_id = attendance.id

        # Verify attendance exists
        self.assertTrue(Attendance.objects.filter(id=attendance_id).exists())

        # Delete employee
        employee.delete()

        # Verify attendance is also deleted (CASCADE)
        self.assertFalse(Attendance.objects.filter(id=attendance_id).exists())


class AttendanceViewTest(TestCase):
    """Tests for the AttendanceView"""

    def setUp(self):
        """Set up test client, user, and group"""
        self.client = Client()

        # Get or create attendance group
        self.attendance_group, created = Group.objects.get_or_create(
            name=settings.ATTENDANCE_ACCOUNT_GROUP
        )

        # Create a test user
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.user.groups.add(self.attendance_group)

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

    def test_attendance_view_get_unauthenticated(self):
        """Test that unauthenticated users are redirected to login"""
        response = self.client.get(reverse('attendance'))
        self.assertEqual(response.status_code, 302)
        self.assertIn('/login/', response.url)

    def test_attendance_view_get_authenticated(self):
        """Test that authenticated users can access the attendance page"""
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('attendance'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'attendance/attendance.html')

    @patch('apps.employee.models.get_id_card_photo')
    def test_attendance_view_post_valid_qr(self, mock_get_id_card):
        """Test posting valid QR code data"""
        # Mock ID card generation
        mock_id_card = MagicMock()
        mock_id_card.read.return_value = b'fake_id_card_data'
        mock_get_id_card.return_value = mock_id_card

        # Create an employee
        photo = self.create_test_image_file()
        employee = Employee.objects.create(
            first_name='John',
            last_name='Doe',
            designation='Developer',
            email='john.doe@example.com',
            phone='1234567890',
            photo=photo
        )

        # Login
        self.client.login(username='testuser', password='testpass123')

        # Post QR code data
        response = self.client.post(
            reverse('attendance'),
            {'text': 'john.doe@example.com'}
        )

        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertTrue(data['success'])
        self.assertEqual(data['message'], 'Attendance marked')

        # Verify attendance was created
        self.assertTrue(
            Attendance.objects.filter(employee=employee).exists()
        )

    def test_attendance_view_post_empty_qr(self):
        """Test posting empty QR code data"""
        self.client.login(username='testuser', password='testpass123')

        response = self.client.post(
            reverse('attendance'),
            {'text': ''}
        )

        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertFalse(data['success'])
        self.assertEqual(data['message'], 'No QR code found')

    def test_attendance_view_post_invalid_email(self):
        """Test posting invalid email format"""
        self.client.login(username='testuser', password='testpass123')

        response = self.client.post(
            reverse('attendance'),
            {'text': 'not-an-email'}
        )

        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertFalse(data['success'])
        self.assertEqual(data['message'], 'Invalid QR code')

    def test_attendance_view_post_employee_not_found(self):
        """Test posting email of non-existent employee"""
        self.client.login(username='testuser', password='testpass123')

        response = self.client.post(
            reverse('attendance'),
            {'text': 'nonexistent@example.com'}
        )

        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertFalse(data['success'])
        self.assertEqual(data['message'], 'Employee not found')

    def test_attendance_view_post_unauthenticated(self):
        """Test that unauthenticated users cannot post"""
        response = self.client.post(
            reverse('attendance'),
            {'text': 'test@example.com'}
        )
        self.assertEqual(response.status_code, 302)

    def test_attendance_view_without_group_permission(self):
        """Test that users not in attendance group cannot access"""
        # Create user without attendance group
        user_no_group = User.objects.create_user(
            username='nogroup',
            password='testpass123'
        )

        self.client.login(username='nogroup', password='testpass123')
        response = self.client.get(reverse('attendance'))

        # Should redirect to login (after logout)
        self.assertEqual(response.status_code, 302)
        self.assertIn('/login/', response.url)


class CustomLoginViewTest(TestCase):
    """Tests for the CustomLoginView"""

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )

    def test_login_view_get(self):
        """Test GET request to login view"""
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'attendance/login.html')

    def test_login_view_successful_login(self):
        """Test successful login"""
        response = self.client.post(
            reverse('login'),
            {
                'username': 'testuser',
                'password': 'testpass123'
            }
        )
        # Should redirect after successful login
        self.assertEqual(response.status_code, 302)

    def test_login_view_redirect_authenticated_user(self):
        """Test that authenticated users are redirected"""
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('login'))
        # Should redirect authenticated users
        self.assertEqual(response.status_code, 302)


class AttendanceMarkedViewTest(TestCase):
    """Tests for the AttendanceMarkedView"""

    def setUp(self):
        self.client = Client()
        self.attendance_group, created = Group.objects.get_or_create(
            name=settings.ATTENDANCE_ACCOUNT_GROUP
        )
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.user.groups.add(self.attendance_group)

    def test_attendance_marked_view_authenticated(self):
        """Test that authenticated users can access marked page"""
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('attendance_marked'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'attendance/attendance_marked.html')

    def test_attendance_marked_view_unauthenticated(self):
        """Test that unauthenticated users are redirected"""
        response = self.client.get(reverse('attendance_marked'))
        self.assertEqual(response.status_code, 302)
        self.assertIn('/login/', response.url)


class AttendanceGroupRequiredMixinTest(TestCase):
    """Tests for the AttendanceGroupRequiredMixin"""

    def setUp(self):
        self.client = Client()
        self.attendance_group, created = Group.objects.get_or_create(
            name=settings.ATTENDANCE_ACCOUNT_GROUP
        )

    def test_mixin_allows_user_in_group(self):
        """Test that users in attendance group can access"""
        user = User.objects.create_user(
            username='groupuser',
            password='testpass123'
        )
        user.groups.add(self.attendance_group)

        self.client.login(username='groupuser', password='testpass123')
        response = self.client.get(reverse('attendance'))
        self.assertEqual(response.status_code, 200)

    def test_mixin_redirects_user_not_in_group(self):
        """Test that users not in attendance group are redirected"""
        user = User.objects.create_user(
            username='nogroupuser',
            password='testpass123'
        )

        self.client.login(username='nogroupuser', password='testpass123')
        response = self.client.get(reverse('attendance'))

        # Should redirect to login
        self.assertEqual(response.status_code, 302)
        self.assertIn('/login/', response.url)

    def test_mixin_redirects_unauthenticated_user(self):
        """Test that unauthenticated users are redirected"""
        response = self.client.get(reverse('attendance'))
        self.assertEqual(response.status_code, 302)
        self.assertIn('/login/', response.url)
