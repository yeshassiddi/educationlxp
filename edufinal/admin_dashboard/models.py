from django.db import models
from django.contrib.auth.models import PermissionsMixin,UserManager
from django.contrib.auth.base_user import AbstractBaseUser
from django.core.validators import RegexValidator
from django.core import validators
import re
from django.utils.translation import gettext as _
from django.contrib.auth.base_user import BaseUserManager
import uuid
from django.core.validators import MaxValueValidator, MinValueValidator


class Master_Role(models.Model):
    class Meta:
        db_table = 'master_role'
    id = models.UUIDField(primary_key = True,default = uuid.uuid4 ,editable = False)
    role_name  = models.CharField(max_length=50, null=True, blank=True)
    is_active  = models.BooleanField(('active'), default=True )
    is_deleted = models.BooleanField(('delete'), default=False)

    def __str__(self):
        return self.role_name.capitalize()

    def save(self, *args, **kwargs):
        self.role_name = self.role_name.title()
        super(Master_Role, self).save(*args, **kwargs)


class User(AbstractBaseUser, PermissionsMixin):

    class Meta:
       db_table = "auth_user"

    id = models.UUIDField(primary_key = True,default = uuid.uuid4 ,editable = False)
    username = models.CharField(_('username'), max_length=75, unique=True, help_text=_('Required. 30 characters or fewer. Letters, numbers and @/./+/-/_ characters'), validators = [ validators.RegexValidator(re.compile('^[\w.@+-]+$'), _('Enter a valid username.'), 'invalid') ])
    first_name = models.CharField(('first_name'),validators=[RegexValidator("^[a-zA-Z]{1,50}")], max_length=50, null=True,blank=True)
    last_name = models.CharField(('last_name'),validators=[RegexValidator("^[a-zA-Z]{1,50}")], max_length=50,null=True,blank=True)
    email = models.EmailField(max_length=70,blank=True, null= True, unique= True)
    is_staff = models.BooleanField(default=0)
    is_active = models.BooleanField(('active'), default=True, help_text=_('Designates whether this user should be treated as active. Unselect this instead of deleting accounts.'))
    phone = models.CharField(validators=[RegexValidator( '^[0-9]{10}$')],max_length=12, null=True,blank=True)
    role_instance = models.ForeignKey(Master_Role, on_delete = models.CASCADE, null = True, blank = True)
    image = models.ImageField(null= True ,blank = True,upload_to='users/')


    created_on = models.DateTimeField(auto_now_add=True,blank=True, null=True,)
    updated_on = models.DateTimeField(auto_now=True,blank=True, null=True,)
    joining_date = models.DateField(null = True, blank = True)
    pin_code = models.CharField(max_length = 10, null = True, blank = True)
    gender = models.CharField(max_length = 10, null = True, blank = True)

    objects = UserManager()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def get_full_name(self):
        return self.first_name+" "+self.last_name

    def get_short_name(self):
        return self.first_name

        
    def __unicode__(self):
        return self.email

    def __str__(self):
        return self.username.capitalize()


student_type_choices = (
    ("International", "International"),
    ("Domestic", "Domestic"),
)
class EnrollmentStatus(models.Model):

    id = models.UUIDField( 
    primary_key=True,
    default=uuid.uuid4,
    editable=False)

    student = models.ForeignKey(User, on_delete=models.CASCADE)
    student_type = models.CharField(choices = student_type_choices,default = 'Domestic', max_length = 50)
    apply_status = models.BooleanField(default = False)
    condition_offer = models.BooleanField(default = False)
    interview = models.BooleanField(default = False)
    submit_pending = models.BooleanField(default = False)
    cad_issued = models.BooleanField(default = False)
    fee_paid = models.BooleanField(default = False)
    student_document = models.BooleanField(default = False)
    enrollment_complete = models.BooleanField(default = False)

    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):  
        # return self.student.username
        return "test"


class MentorNeed(models.Model):

    id = models.UUIDField( 
    primary_key=True,
    default=uuid.uuid4,
    editable=False)

    mentor = models.TextField(null = True, blank = True)
    need_mentor = models.TextField(null = True, blank = True)
    created_on = models.DateTimeField(auto_now_add=True)
    student = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):  
        return self.student.username




class Course(models.Model):
    id = models.UUIDField( 
    primary_key=True,
    default=uuid.uuid4,
    editable=False)

    course_name = models.CharField(max_length=200)
    description = models.TextField(null = True,blank = True)
    professor = models.ForeignKey(User, on_delete=models.CASCADE)
    students = models.ManyToManyField(User, related_name = 'student')
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):  
        return self.course_name


class AttendenceUser(models.Model):

    id = models.UUIDField( 
    primary_key=True,
    default=uuid.uuid4,
    editable=False)

    student = models.ForeignKey(User, on_delete=models.CASCADE)
    course_instance = models.ForeignKey(Course, on_delete=models.CASCADE)
    created_on = models.DateField(auto_now_add=True)

    def __str__(self):  
        return self.student.username


class StudyMaterial(models.Model):
    id = models.UUIDField( 
    primary_key=True,
    default=uuid.uuid4,
    editable=False)

    file = models.FileField(null= True ,blank = True,upload_to='study_material/')
    title = models.CharField(
        max_length=30,null = True,blank = True
    )
    user_instance = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    course_instance = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):  
        return self.title

class StudyDiscussion(models.Model):
    id = models.UUIDField( 
    primary_key=True,
    default=uuid.uuid4,
    editable=False)

    title = models.CharField(
        max_length=30,null = True,blank = True
    )
    description = models.TextField(null = True,blank = True)
    user_instance = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    course_instance = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):  
        return self.title
