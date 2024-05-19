from django.contrib import admin
from apps.employee.models import Employee

admin.site.site_header = 'Employee Management System'

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone', 'created_at', 'updated_at')
    search_fields = ('first_name', 'last_name', 'email', 'phone')
    list_display_links = ('first_name', 'last_name', 'email', 'phone')

admin.site.register(Employee, EmployeeAdmin)