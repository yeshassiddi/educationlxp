from django.urls import path
from auth_user_app.views import *

urlpatterns = [

	path('student_register/', RegisterView.as_view()),
	path('Attendance/', Attendance.as_view()),


]