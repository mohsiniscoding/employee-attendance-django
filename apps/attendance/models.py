from django.db import models
from apps.employee.models import Employee

class Attendance(models.Model):
    class Meta:
        verbose_name = 'Attendance'
        verbose_name_plural = 'Attendances'

    class Status(models.TextChoices):
        CHECK_IN = "Check In"
        CHECK_OUT = "Check Out"
        UNKNOWN = "Unknown"

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.UNKNOWN)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.employee} - {self.created_at.strftime("%Y-%m-%d %H:%M:%S")}'