from rest_framework.views import APIView
import ast,sys,json,random
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.http.response import JsonResponse
from django.utils import timezone
from django.contrib.auth import authenticate, login
from knox.models import AuthToken
from rest_framework.permissions import IsAuthenticated
from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site
from rest_framework import  status, generics
from admin_dashboard.models import User, Master_Role, Course,StudyMaterial,StudyDiscussion,AttendenceUser,EnrollmentStatus

def convert_trueTrue_falseFalse(input):
    if input.lower() == 'false':
        return False
    elif input.lower() == 'true':
        return True
    else:
        raise ValueError("...")

# host return functions starts from here
def current_host(request):

	''' demonstrate docstring for confirm this function will return current request host that we can use everywhere in application '''
	try:
		site_url = get_current_site(request)
		site_url = str(site_url)
		return site_url
	except Exception as e:
		print("\n")
		print("error at current_host is", e)
		return None
# host return functions ends at here



class RegisterView(APIView):

	''' Demonstrate docstring for confirming that this view api will register a user'''


	def post(self, request):
		context = {}
		try:
			username = self.request.POST.get('username')
			if not username:
				context['message'] = 'Please Fill out Your Username'
				context['status'] = 400
				return JsonResponse(context,status=context['status'])

			first_name = self.request.POST.get('first_name')
			last_name = self.request.POST.get('last_name')


			email = self.request.POST.get('email')
			if not email:
				context['message'] = 'Please Fill out Your email'
				context['status'] = 400
				return JsonResponse(context,status=context['status'])

			password = self.request.POST.get('password')
			if not password:
				context['message'] = 'Please Fill out Your Password'
				context['status'] = 400
				return JsonResponse(context,status=context['status'])
			elif password:
				if len(password) <= 6:
					context['message'] = 'Password must contains more than 6 Characters'
					context['status'] = 400
					return JsonResponse(context,status=context['status'])

			try:
				role_instance = Master_Role.objects.get(role_name = 'Student')
			except:
				role_instance = Master_Role.objects.create(role_name = 'Student')

			image = self.request.FILES.get('image')
			phone = self.request.POST.get('phone')
			pin_code = self.request.POST.get('pin_code')
			course_ids = self.request.POST.get('course_ids')
			joining_date = self.request.POST.get('joining_date')
			gender = self.request.POST.get('gender')


			student_type = self.request.POST.get('student_type')
			apply_status = self.request.POST.get('apply_status')
			condition_offer = self.request.POST.get('condition_offer')
			interview = self.request.POST.get('interview')
			submit_pending = self.request.POST.get('submit_pending')
			cad_issued = self.request.POST.get('cad_issued')
			fee_paid = self.request.POST.get('fee_paid')
			student_document = self.request.POST.get('student_document')
			enrollment_complete = self.request.POST.get('enrollment_complete')


            # make obj of class to save register info
			check_user_mobile = User.objects.filter(username = username).count()
			check_email_mobile = User.objects.filter(email = email).count()

			if check_email_mobile > 0:
				context['message'] = 'Sorry,This Email is already in Use'
				context['status'] = 400
				return JsonResponse(context,status=context['status'])	

			if check_user_mobile > 0:
				context['message'] = 'Sorry,This Username is already in Use'
				context['status'] = 400
				return JsonResponse(context,status=context['status'])	
			else:
				user_obj = User.objects.create(email= email, username = username,first_name = first_name,last_name = last_name,phone = phone,role_instance = role_instance)
				if image:
					user_obj.image = image

				if joining_date:
					user_obj.joining_date = joining_date
				if pin_code:
					user_obj.pin_code = pin_code
				if gender:
					user_obj.gender = gender

				user_obj.save()
				obj_enrollment  = EnrollmentStatus.objects.create(student = user_obj,student_type = student_type)
				if apply_status:
					obj_enrollment.apply_status = convert_trueTrue_falseFalse(apply_status)

				if condition_offer:
					obj_enrollment.condition_offer = convert_trueTrue_falseFalse(condition_offer)
				if interview:
					obj_enrollment.interview = convert_trueTrue_falseFalse(interview)
				if submit_pending:
					obj_enrollment.submit_pending = convert_trueTrue_falseFalse(submit_pending)
				if cad_issued:
					obj_enrollment.cad_issued = convert_trueTrue_falseFalse(cad_issued)
				if fee_paid:
					obj_enrollment.fee_paid = convert_trueTrue_falseFalse(fee_paid)
				if student_document:
					obj_enrollment.student_document = convert_trueTrue_falseFalse(student_document)
				if enrollment_complete:
					obj_enrollment.enrollment_complete = convert_trueTrue_falseFalse(enrollment_complete)


				token = AuthToken.objects.create(user_obj)[1]
				context['message'] = 'Thank you for your registration! Your account has been successfully created.'
				context['status'] = 200
				context['token'] = token
				context['user_id'] = user_obj.id
				context['user_email'] = user_obj.email
				context['username'] = user_obj.username
				context['first_name'] = user_obj.first_name
				context['last_name'] = user_obj.last_name
				return JsonResponse(context,status=context['status'])

		except :
			context = {}
			print(sys.exc_info())
			context['message'] = 'An error occurred in registering your account, please try again or contact us'
			context['status'] = 500
			return JsonResponse(context,status=context['status'])


def checkAuthToken(request):
    try:
        token = request.auth.user
        return token
    except Exception as E:
        print(E)        
        return None


class Attendance(APIView):

	''' Demonstrate docstring for confirming that this view api will register a user'''


	def post(self, request):
		context = {}
		try:
			user_id = self.request.POST.get('user_id')
			if not user_id:
				context['message'] = 'Please fill out user_id'
				context['status'] = 400
				return JsonResponse(context,status=context['status'])

			course_id = self.request.POST.get('course_id')
			if not user_id:
				context['message'] = 'Please fill out course_id'
				context['status'] = 400
				return JsonResponse(context,status=context['status'])


			try:
				user_instance = User.objects.get(id = user_id)
			except:
				context['message'] = 'User does not exists'
				context['status'] = 400
				return JsonResponse(context,status=context['status'])

			try:
				course_instance = Course.objects.get(id = course_id)
			except:
				context['message'] = 'Course does not exists'
				context['status'] = 400
				return JsonResponse(context,status=context['status'])

			import datetime
			check_attendance = AttendenceUser.objects.filter(student = user_instance,course_instance = course_instance,created_on  = datetime.datetime.today().date()).count()

			if check_attendance > 0:
				context['message'] = 'Sorry,Attendance already done for this date'
				context['status'] = 400
				return JsonResponse(context,status=context['status'])

			else:
				user_obj = AttendenceUser.objects.create(student = user_instance,course_instance = course_instance,created_on  = datetime.datetime.today().date())

				context['message'] = 'Thank you for your attendance !'
				context['status'] = 200
				return JsonResponse(context,status=context['status'])

		except :
			context = {}
			print(sys.exc_info())
			context['message'] = 'An error occurred in registering your account, please try again or contact us'
			context['status'] = 500
			return JsonResponse(context,status=context['status'])

