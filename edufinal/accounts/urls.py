from django.urls import path
from accounts.views import *
from admin_dashboard.decorators import *

urlpatterns = [

    path('', StudentRequired(StudyMaterialSection.as_view()),name = 'StudyMaterialSection'),
    path('logout/', UserLogoutView.as_view(),name = 'UserLogoutView'),
    path('login/', Login.as_view(), name = 'Login'),
    path('discussion/', StudentRequired(DiscussionPost.as_view()), name = 'DiscussionPost'),
    path('download_file/', download_file, name = 'download_file'),
    path('ProfilePage/', StudentRequired(ProfilePage.as_view()), name = 'ProfilePage'),
    path('Mentorship/', StudentRequired(Mentorship.as_view()), name = 'Mentorship'),
    path('OtherUserProfilePage/', StudentRequired(OtherUserProfilePage.as_view()), name = 'OtherUserProfilePage'),
    path('Attendance/', StudentRequired(AttendancePage.as_view()), name = 'AttendancePage'),
    path('Enrollment/', StudentRequired(EnrollmentPage.as_view()), name = 'EnrollmentPage'),

]
