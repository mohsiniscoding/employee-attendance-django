from django.contrib import admin
from apps.attendance.models import Attendance

class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('employee', 'created_at', 'updated_at')
    search_fields = ('employee__first_name', 'employee__last_name', 'employee__email', 'date')
    list_filter = ('created_at', 'employee__email')
    ordering = ('-created_at',)

admin.site.register(Attendance, AttendanceAdmin)