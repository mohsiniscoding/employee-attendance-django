from typing import Iterable
from django.db import models
from django.core.exceptions import ValidationError

from apps.employee.card_utils import get_id_card_photo

def validate_image(image):
    if image.file.size > 2 * 1024 * 1024:
        raise ValidationError('Image file too large ( > 2mb )')
    file_extension = image.file.name.split('.')[-1].lower()
    if file_extension not in ['jpg', 'jpeg']:
        raise ValidationError('Image file type not supported. Only JPEG files are accepted.')

class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    designation = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    photo = models.ImageField(upload_to='employee_photos', validators=[validate_image])
    id_card_photo = models.ImageField(upload_to='employee_id_cards', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
    def save(self, *args, **kwargs):
        # Determine if we need to regenerate the ID card
        regenerate_id_card = False

        if self.pk:
            # Employee already exists, check if relevant fields changed
            try:
                old_instance = Employee.objects.get(pk=self.pk)
                # Check if photo, name, or designation changed
                if (old_instance.photo != self.photo or
                    old_instance.first_name != self.first_name or
                    old_instance.last_name != self.last_name or
                    old_instance.designation != self.designation):
                    regenerate_id_card = True
            except Employee.DoesNotExist:
                # Safety check - if we can't find the old instance, regenerate
                regenerate_id_card = True
        else:
            # New employee, generate ID card
            regenerate_id_card = True

        # Only regenerate ID card if needed
        if regenerate_id_card:
            ## Remove previous photo if it exists
            if self.id_card_photo:
                self.id_card_photo.delete(save=False)

            ## Add id_card_photo to the instance
            self.id_card_photo.save(
                f'{self.first_name}_{self.last_name}_id_card.jpg',
                get_id_card_photo(self),
                save=False
            )

        super().save(*args, **kwargs)  
