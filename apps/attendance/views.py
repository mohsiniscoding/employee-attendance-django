from django.shortcuts import render
from django.views.generic import View
from apps.attendance.mixins import AttendanceGroupRequiredMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.http import JsonResponse
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from apps.employee.models import Employee
from apps.attendance.models import Attendance
from django.utils import timezone
from datetime import timedelta
import logging

logger = logging.getLogger(__name__)



class AttendanceView(LoginRequiredMixin, AttendanceGroupRequiredMixin, View):
    def get(self, request):
        return render(request, 'attendance/attendance.html')
    
    def post(self, request):
        decoded_qr_text = request.POST.get('text')
        logger.info(f'Attendance scan attempt by user: {request.user.username}')

        ## Check if QR code is not empty
        if not decoded_qr_text:
            logger.warning('Attendance scan failed: No QR code provided')
            return JsonResponse({'success':False, 'message': 'No QR code found'}, status=200)

        ## Check if QR code is valid email
        try:
            validate_email(decoded_qr_text)
        except ValidationError as e:
            logger.warning(f'Invalid QR code format: {decoded_qr_text}, Error: {e}')
            return JsonResponse({'success':False, 'message': 'Invalid QR code'}, status=200)

        ## check if this employee email is valid
        try:
            employee = Employee.objects.get(email=decoded_qr_text)
        except Employee.DoesNotExist:
            logger.warning(f'Employee not found for email: {decoded_qr_text}')
            return JsonResponse({'success':False, 'message': 'Employee not found'}, status=200)

        ## Get the current time
        now = timezone.now()

        ## Check for recent duplicate scans (within 1 minute)
        one_minute_ago = now - timedelta(minutes=1)
        recent_attendance = Attendance.objects.filter(
            employee=employee,
            created_at__gte=one_minute_ago
        ).first()

        if recent_attendance:
            logger.warning(f'Duplicate attendance attempt for {employee.email} within 1 minute')
            return JsonResponse({
                'success': False,
                'message': f'Already marked attendance ({recent_attendance.status}) less than a minute ago'
            }, status=200)

        ## Get today's date range
        today_start = now.replace(hour=0, minute=0, second=0, microsecond=0)
        today_end = now.replace(hour=23, minute=59, second=59, microsecond=999999)

        ## Get the last attendance record for today
        last_attendance = Attendance.objects.filter(
            employee=employee,
            created_at__gte=today_start,
            created_at__lte=today_end
        ).order_by('-created_at').first()

        ## Determine the status (Check In or Check Out)
        if last_attendance is None or last_attendance.status == Attendance.Status.CHECK_OUT:
            # First attendance of the day or last was CHECK_OUT, so this is CHECK_IN
            status = Attendance.Status.CHECK_IN
            message = 'Checked in successfully'
        elif last_attendance.status == Attendance.Status.CHECK_IN:
            # Last was CHECK_IN, so this is CHECK_OUT
            status = Attendance.Status.CHECK_OUT
            message = 'Checked out successfully'
        else:
            # Fallback for UNKNOWN status
            status = Attendance.Status.CHECK_IN
            message = 'Checked in successfully'

        ## Create attendance record
        attendance = Attendance.objects.create(employee=employee, status=status)
        logger.info(f'Attendance marked: {employee.email} - {status} at {attendance.created_at}')

        return JsonResponse({'success':True, 'message': message, 'status': status}, status=200)

    
    def attendance_marked(self, request):
        return render(request, 'attendance/attendance_marked.html')
    
class CustomLoginView(LoginView):
    template_name = 'attendance/login.html'
    redirect_authenticated_user = True

class AttendanceMarkedView(LoginRequiredMixin, AttendanceGroupRequiredMixin, View):
    def get(self, request):
        return render(request, 'attendance/attendance_marked.html')
    