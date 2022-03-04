from django.shortcuts import redirect
from django.urls import reverse
import sys
from admin_dashboard.models import User



def StudentRequired(function):

   '''this decorator we will used only if the url only visible by Admin'''


   def wrap(request,*args, **kwargs):
      try:
         if request.user:
            user= request.user.id

            obj = User.objects.get(id = int(user), is_superuser = False)
         else:
            return redirect('%s?next=%s' % (reverse('Login'), reverse('StudyMaterialSection')))
      except:
         print(sys.exc_info())
         return redirect('%s?next=%s' % (reverse('Login'), reverse('StudyMaterialSection')))

      return function(request, *args, **kwargs)

   return wrap



