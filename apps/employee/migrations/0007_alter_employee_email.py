# Generated by Django 5.0.6 on 2024-05-18 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0006_employee_designation_alter_employee_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
