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



class AttendanceView(LoginRequiredMixin, AttendanceGroupRequiredMixin, View):
    def get(self, request):
        return render(request, 'attendance/attendance.html')
    
    def post(self, request):
        decoded_qr_text = request.POST.get('text')

        ## Check if QR code is not empty
        if not decoded_qr_text:
            return JsonResponse({'success':False, 'message': 'No QR code found'}, status=200)
        
        ## Check if QR code is valid email
        try:
            validate_email(decoded_qr_text)
        except ValidationError as e:
            print("bad email, details:", e)
            return JsonResponse({'success':False, 'message': 'Invalid QR code'}, status=200)

        ## cheeck if this employee email is valid
        try:
            employee = Employee.objects.get(email=decoded_qr_text)
        except Employee.DoesNotExist:
            return JsonResponse({'success':False, 'message': 'Employee not found'}, status=200)
        
        ## mark attendance
        Attendance.objects.create(employee=employee)

        return JsonResponse({'success':True, 'message': 'Attendance marked'}, status=200)

    
    def attendance_marked(self, request):
        return render(request, 'attendance/attendance_marked.html')
    
class CustomLoginView(LoginView):
    template_name = 'attendance/login.html'
    redirect_authenticated_user = True

class AttendanceMarkedView(LoginRequiredMixin, AttendanceGroupRequiredMixin, View):
    def get(self, request):
        return render(request, 'attendance/attendance_marked.html')
    