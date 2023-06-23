from django.db import models

# Create your models here.
class Course(models.Model):#ชื่อไม่ซ้ำ
    student = models.ForeignKey()
    course = models.CharField()
    status_course = models.CharField()
    course_date = models.DateField()

class CoursePayment(models.Model):
    student = models.ForeignKey()
    payment_status = models.BooleanField()
    payment_date = models.DateField()