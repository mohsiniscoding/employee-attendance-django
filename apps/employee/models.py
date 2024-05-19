from typing import Iterable
from django.db import models
from django.core.exceptions import ValidationError

from apps.employee.card_utils import get_id_card_photo

def validate_image(image):
    if image.file.size > 2 * 1024 * 1024:
        raise ValidationError('Image file too large ( > 2mb )')
    if image.file.name.split('.')[-1] not in ['jpg', 'jpeg']:
        raise ValidationError('Image file type not supported. Only JPEG and PNG files are accepted.')

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
        ## remove previous photo if it exists
        if self.id_card_photo:
            self.id_card_photo.delete(save=False)
            
        ## add id_card_photo to the instance
        self.id_card_photo.save(
            f'{self.first_name}_{self.last_name}_id_card.jpg',
            get_id_card_photo(self),
            save=False
        )

        super().save(*args, **kwargs)  
