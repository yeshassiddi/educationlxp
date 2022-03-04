from django.contrib import admin
from admin_dashboard.models import MentorNeed,User, Master_Role, Course,StudyMaterial,StudyDiscussion,EnrollmentStatus,AttendenceUser
from django import forms
# Register your models here.

class UserCreationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name','last_name','role_instance','image','email','username','password','is_active','phone','gender','pin_code')

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


@admin.register(MentorNeed)
class MentorNeedAdmin(admin.ModelAdmin):
    list_display = ('id', 'mentor','created_on')
    list_per_page = 10



@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    form = UserCreationForm
    list_display = ('id', 'email', 'username', 'first_name', 'last_name','created_on')
    list_per_page = 10


@admin.register(EnrollmentStatus)
class EnrollmentStatusAdmin(admin.ModelAdmin):
    list_display = ('id','student', 'student_type', 'apply_status', 'fee_paid', 'created_on')
    list_per_page = 10


@admin.register(AttendenceUser)
class AttendenceUserAdmin(admin.ModelAdmin):
    list_display = ('id','created_on')
    list_per_page = 10



@admin.register(Master_Role)
class Master_Admin(admin.ModelAdmin):
    list_display = ('id', 'role_name')
    list_per_page = 10



@admin.register(Course)
class Course(admin.ModelAdmin):
    list_display = ('id', 'course_name', 'description', 'created_on')
    list_per_page = 10

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields["students"].queryset = User.objects.filter(role_instance__role_name = 'Student')
        form.base_fields["professor"].queryset = User.objects.filter(role_instance__role_name = 'Professor')

        return form

    def get_queryset(self, request): 
        qs = super().get_queryset(request) 
        if request.user.is_superuser:
            return qs


@admin.register(StudyMaterial)
class StudyMaterialAdmin(admin.ModelAdmin):
    list_display = ('id','title','created_on' )
    list_per_page = 10


@admin.register(StudyDiscussion)
class StudyDiscussionAdmin(admin.ModelAdmin):
    list_display = ('id','title','created_on' )
    list_per_page = 10
