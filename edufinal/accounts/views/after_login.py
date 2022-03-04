from django.shortcuts import render,redirect
from django.views import View

import os
from django.conf import settings
from django.http import HttpResponse, Http404
from admin_dashboard.models import *
from django.http.response import JsonResponse

class StudyMaterialSection(View):

	templates_name = 'accounts/discussion.html'

	def get(self,request):
		context = {}
		user_instance = User.objects.get(id = request.user.id)
		try:
			course_id = self.request.GET.get('course_id')
			try:
				course_instance = Course.objects.get(id =  course_id)
			except:
				course_instance = Course.objects.last()

			try:
				course_id = course_instance.id
			except:
				course_id = ''



			study_material = StudyMaterial.objects.filter(course_instance = course_instance)
			study_discussion = StudyDiscussion.objects.filter(course_instance = course_instance)
			print("user_instance.role_instance.role_name",user_instance.role_instance.role_name)

			if user_instance.role_instance.role_name.lower() == 'student':
				all_courses = Course.objects.filter(students = user_instance)
			else:
				all_courses = Course.objects.filter(professor = user_instance)
			print("all_courses",all_courses)

			return render(request,self.templates_name,locals())
		except:
			return render(request,self.templates_name,locals())

	def post(self,request):
		context = {}
		try:
			## getting course_id and validate it 
			course_id = self.request.POST.get('course_id')
			if not course_id:
				msg='Error ! Course Id is required'
				return render(request,self.templates_name,locals())
			## ends here getting course_id and validate it 
			user_id = request.user.id
			user_instance = User.objects.get(id = user_id)

			try:
				course_instance = Course.objects.get(id =  course_id)
			except:
				course_instance = Course.objects.last()

			try:
				course_id = course_instance.id
			except:
				course_id = ''



			study_material = StudyMaterial.objects.filter(course_instance = course_instance)
			study_discussion = StudyDiscussion.objects.filter(course_instance = course_instance)
			print("user_instance.role_instance.role_name",user_instance.role_instance.role_name)

			if user_instance.role_instance.role_name.lower() == 'student':
				all_courses = Course.objects.filter(students = user_instance)
			else:
				all_courses = Course.objects.filter(professor = user_instance)




			## getting select_seller and validate it 
			file = self.request.FILES.get('file')
			if not file:
				msg= 'Error ! File is Required'
				return render(request,self.templates_name,locals())
			## ends here getting select_seller and validate it 



			seller_livestream_instance = StudyMaterial.objects.create(file =  file,user_instance = user_instance,course_instance = course_instance)

			course_instance = Course.objects.get(id =  course_id)
			study_material = StudyMaterial.objects.filter(course_instance = course_instance)
			study_discussion = StudyDiscussion.objects.filter(course_instance = course_instance)
			return render(request,self.templates_name,locals())


		except Exception as e:
			print(e)
			msg= 'Something went wrong ,Please try or contact us later'
			return render(request,self.templates_name,locals())


class DiscussionPost(View):

	templates_name = 'accounts/discussion.html'

	def get(self,request):
		context = {}
		user_instance = User.objects.get(id = request.user.id)
		try:
			course_id = self.request.GET.get('course_id')
			try:
				course_instance = Course.objects.get(id =  course_id)
			except:
				course_instance = Course.objects.last()

			try:
				course_id = course_instance.id
			except:
				course_id = ''



			study_material = StudyMaterial.objects.filter(course_instance = course_instance)
			study_discussion = StudyDiscussion.objects.filter(course_instance = course_instance)

			if user_instance.role_instance.role_name.lower() == 'student':
				all_courses = Course.objects.filter(students = user_instance)
			else:
				all_courses = Course.objects.filter(professor = user_instance)
			return render(request,self.templates_name,locals())
		except:
			msg= 'Something went wrong ,Please try or contact us later'

			return render(request,self.templates_name,locals())

	def post(self,request):
		context = {}
		try:

			## getting course_id and validate it 
			course_id = self.request.POST.get('course_id')
			if not course_id:
				msg= 'Error ! Course Id is required'
				return render(request,self.templates_name,locals())
			## ends here getting course_id and validate it 
			user_id = request.user.id
			user_instance = User.objects.get(id = user_id)

			try:
				course_instance = Course.objects.get(id =  course_id)
			except:
				course_instance = Course.objects.last()

			try:
				course_id = course_instance.id
			except:
				course_id = ''



			study_material = StudyMaterial.objects.filter(course_instance = course_instance)
			study_discussion = StudyDiscussion.objects.filter(course_instance = course_instance)
			print("user_instance.role_instance.role_name",user_instance.role_instance.role_name)

			if user_instance.role_instance.role_name.lower() == 'student':
				all_courses = Course.objects.filter(students = user_instance)
			else:
				all_courses = Course.objects.filter(professor = user_instance)



			## getting description and validate it 
			description = self.request.POST.get('description')
			if not description:
				msg= 'Error ! description is Required'
				return render(request,self.templates_name,locals())
			## ends here getting description and validate it 



			seller_livestream_instance = StudyDiscussion.objects.create(description =  description,user_instance = user_instance,course_instance = course_instance)
			success_msg = 'Posted'

			course_instance = Course.objects.get(id =  course_id)
			study_material = StudyMaterial.objects.filter(course_instance = course_instance)
			study_discussion = StudyDiscussion.objects.filter(course_instance = course_instance)
			return render(request,self.templates_name,locals())


		except Exception as e:
			print(e)
			msg= 'Something went wrong ,Please try or contact us later'
			return render(request,self.templates_name,locals())

def download_file(request):
    course_id = request.GET.get('course_id')
    study_material = StudyMaterial.objects.get(id = course_id)
    path = study_material.file.name
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise Http404


class ProfilePage(View):

	templates_name = 'accounts/profile.html'

	def get(self,request):

		context = {}
		user_instance = User.objects.get(id = request.user.id)
		try:
			course_id = self.request.GET.get('course_id')
			try:
				course_instance = Course.objects.get(id =  course_id)
			except:
				course_instance = Course.objects.last()

			try:
				course_id = course_instance.id
			except:
				course_id = ''



			study_material = StudyMaterial.objects.filter(course_instance = course_instance)
			study_discussion = StudyDiscussion.objects.filter(course_instance = course_instance)
			print("user_instance.role_instance.role_name",user_instance.role_instance.role_name)

			if user_instance.role_instance.role_name.lower() == 'student':
				all_courses = Course.objects.filter(students = user_instance)
			else:
				all_courses = Course.objects.filter(professor = user_instance)
			mentor_instance = MentorNeed.objects.filter(student = user_instance).last()
			enrol_instance = EnrollmentStatus.objects.filter(student = user_instance).last()

			return render(request,self.templates_name,locals())
		except:
			return render(request,self.templates_name,locals())

	def post(self, request, *args, **kwargs):

		''' this function will hit while post request only and we can get every thing from request.POST parameter'''
		context = {}
		try:
			try:

				user_instance = User.objects.get(id=request.user.id)
			except Exception as e:
				print("e is", e)
				data = {"message":"User does not exists"}
				return JsonResponse(data)

			# getting first_name password and validate it
			first_name = request.POST.get('first_name')
			if not first_name:
				context['message'] = 'Error ! Please, Enter your First Name'
				context['status'] = 400
				return JsonResponse(context)
			# ends here first_name password and validate it

			# getting last_name password and validate it
			last_name = request.POST.get('last_name')
			if not last_name:
				context['message'] = 'Error ! Please, Enter your Last Name'
				context['status'] = 400
				return JsonResponse(context)
			# ends here last_name password and validate it

			# getting phone password and validate it
			phone = request.POST.get('phone')
			if not phone:
				context['message'] = 'Error ! Please, Enter your phone'
				context['status'] = 400
				return JsonResponse(context)
			# ends here phone password and validate it

			date = request.POST.get('date')
			email = request.POST.get('email')

			user_image = request.FILES.get('user_image')

			if not email:
				context['message'] = 'Error ! Email is Required'
				context['status'] = 400
				return JsonResponse(context)


			user_instance.first_name = first_name
			user_instance.email = email
			user_instance.last_name = last_name
			user_instance.phone = phone
			user_instance.joining_date = date
			if user_image:
				user_instance.user_image = user_image

			user_instance.save()

			context['message'] = 'Success ! Your Profile has been successfully changed '
			context['status'] = 200
			return JsonResponse(context)
				

		except Exception as e:
			print("e is", e)
			data = {"status": 500, "message": "Something Going Wrong ! Please try again later or contact us"}
			return JsonResponse(context)

class Mentorship(View):

	templates_name = 'accounts/profile.html'

	def post(self, request, *args, **kwargs):

		''' this function will hit while post request only and we can get every thing from request.POST parameter'''
		context = {}
		try:
			try:

				user_instance = User.objects.get(id=request.user.id)
			except Exception as e:
				print("e is", e)
				data = {"message":"User does not exists"}
				return JsonResponse(data)

			# getting mentor password and validate it
			mentor = request.POST.get('mentor').strip()
			print(request.POST)

			# ends here mentor password and validate it
			looking_mentor = request.POST.get('looking_mentor').strip()
			

			try:
				mentor_instance = MentorNeed.objects.get(student = user_instance)
			except Exception as e:
				mentor_instance = MentorNeed()


			mentor_instance.mentor = mentor
			mentor_instance.need_mentor = looking_mentor
			mentor_instance.student = user_instance
			mentor_instance.save()

			context['message'] = 'Success ! Your Information has been successfully changed '
			context['status'] = 200
			return JsonResponse(context)
				

		except Exception as e:
			print("e is", e)
			data = {"status": 500, "message": "Something Going Wrong ! Please try again later or contact us"}
			return JsonResponse(context)



class OtherUserProfilePage(View):

	templates_name = 'accounts/other_profile.html'

	def get(self,request):

		context = {}
		user_instance = User.objects.get(id = request.GET.get('id'))
		print(request.user.id,request.GET.get('id') )
		if str(request.GET.get('id')) == str(request.user.id) :
			return redirect('/ProfilePage/?course_id={}'.format(request.GET.get('course_id')))
		try:
			course_id = self.request.GET.get('course_id')
			try:
				course_instance = Course.objects.get(id =  course_id)
			except:
				course_instance = Course.objects.last()

			try:
				course_id = course_instance.id
			except:
				course_id = ''



			study_material = StudyMaterial.objects.filter(course_instance = course_instance)
			study_discussion = StudyDiscussion.objects.filter(course_instance = course_instance)
			print("user_instance.role_instance.role_name",user_instance.role_instance.role_name)

			if user_instance.role_instance.role_name.lower() == 'student':
				all_courses = Course.objects.filter(students = user_instance)
			else:
				all_courses = Course.objects.filter(professor = user_instance)
			mentor_instance = MentorNeed.objects.filter(student = user_instance).last()

			return render(request,self.templates_name,locals())
		except:
			return render(request,self.templates_name,locals())







class AttendancePage(View):

	templates_name = 'accounts/attendance.html'

	def get(self,request):

		context = {}
		user_instance = User.objects.get(id = request.user.id)
		course_id = self.request.GET.get('course_id')
		try:
			course_instance = Course.objects.get(id =  course_id)
		except:
			course_instance = Course.objects.last()

		try:
			course_id = course_instance.id
		except:
			course_id = ''

		study_material = StudyMaterial.objects.filter(course_instance = course_instance)
		study_discussion = StudyDiscussion.objects.filter(course_instance = course_instance)

		if user_instance.role_instance.role_name.lower() == 'student':
			all_courses = Course.objects.filter(students = user_instance)
		else:
			all_courses = Course.objects.filter(professor = user_instance)
		mentor_instance = MentorNeed.objects.filter(student = user_instance).last()
		attendance_per_course = AttendenceUser.objects.filter(student = user_instance)

		all_courses_list = []
		for one_course in all_courses:
			course_dict = {}
			course_dict['name_of_course'] = one_course.course_name
			course_dict['course_id'] = one_course.id

			getting_all_attendence_per = AttendenceUser.objects.filter(student = user_instance, course_instance = one_course)
			attend_list = []
			for one_attend in getting_all_attendence_per:
				attend_dict  = {}
				attend_dict['date'] = one_attend.created_on
				attend_dict['id'] = one_attend.id
				attend_list.append(attend_dict)
			course_dict['attendance'] = attend_list
			all_courses_list.append(course_dict)



		return render(request,self.templates_name,locals())

class EnrollmentPage(View):

	templates_name = 'accounts/enrollment.html'

	def get(self,request):

		context = {}

		user_instance = User.objects.get(id = request.user.id)
		course_id = self.request.GET.get('course_id')
		try:
			course_instance = Course.objects.get(id =  course_id)
		except:
			course_instance = Course.objects.last()

		try:
			course_id = course_instance.id
		except:
			course_id = ''

		study_material = StudyMaterial.objects.filter(course_instance = course_instance)
		study_discussion = StudyDiscussion.objects.filter(course_instance = course_instance)

		if user_instance.role_instance.role_name.lower() == 'student':
			all_courses = Course.objects.filter(students = user_instance)
		else:
			all_courses = Course.objects.filter(professor = user_instance)
		mentor_instance = MentorNeed.objects.filter(student = user_instance).last()

		enrol_instance = EnrollmentStatus.objects.filter(student=user_instance).last()

		return render(request,self.templates_name,locals())

