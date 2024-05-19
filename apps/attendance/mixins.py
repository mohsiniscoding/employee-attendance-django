from django.conf import settings
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib import messages

class AttendanceGroupRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.groups.filter(name=settings.ATTENDANCE_ACCOUNT_GROUP).exists()
    
    def handle_no_permission(self):
        if self.request.user.is_authenticated:
            logout(self.request)
        
        return redirect('login')