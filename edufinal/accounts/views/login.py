from django.shortcuts import render,redirect
from django.views import View
from admin_dashboard.models import User
from django.contrib import messages
from django.db.models import Q
from django.utils import timezone
from django.contrib.auth import login,authenticate,logout

# Create your views here.



class Login(View):
	templates_name = 'login/login.html'
	def get(self,request):
		context = {}

		try:
			context['msg'] = request.GET.get('msg')
			return render(request,self.templates_name,context)
		except:
			return render(request,self.templates_name,context)
	def post(self,request):
		context = {}

		try:

			username = request.POST.get('username')
			if not username:
				context['msg'] ='Error! Please Enter Your username'
				return render(request,self.templates_name,context)


			password = request.POST.get('password')
			if not password:
				context['msg'] = 'Error ! Please Enter Your Password'
				return render(request,self.templates_name,context)

			email_check = User.objects.filter(username = username)
			print("email_check", email_check)

			if email_check:
				if email_check[0].is_active == True :
					username_auth = authenticate(username = email_check[0].username,password = password)
					if username_auth:
						
						login(request,username_auth)
						return redirect("/")
					else:
						print("00")
						context['msg'] = 'Error ! Incorrect Username and Password, Please Try Again'
						return render(request,self.templates_name,context)
				else:
					print("00")
					context['msg'] = 'Error ! Incorrect Username and Password, Please try Again'
					return render(request,self.templates_name,context)
			else:
				print("1")
				context['msg'] = 'Error ! Incorrect Username ,Please try again'
				return render(request,self.templates_name,context)
		except Exception as e:
			print(e)
			context['msg'] = 'Something Went Wrong, Please Try Again or Contact Us'
			return render(request,self.templates_name,context)
		
class UserLogoutView(View):

	def get(self,request):

		logout(request)
		return redirect('/login/?sucess_msg=Success ! Your Account has been Successfully Logout')



