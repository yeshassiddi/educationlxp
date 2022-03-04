from django.test import TestCase

from admin_dashboard.models import *

class TestAdminModels(TestCase):
    def test_model_str(self):
        student = AttendenceUser.objects.create(student= "12")
        course = AttendenceUser.objects.create(course_instance="1")
        self.assertEqual(str(student),"123")
