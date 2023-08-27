from django.db import models
from django.urls import reverse

# Create your models here.


class Course(models.Model):
  cname = models.CharField(max_length=50)
  dur = models.IntegerField()
  fee = models.IntegerField()
  trainer = models.CharField(max_length=50)

  def __str__(self):
    return self.cname
  
  # def get_absolute_url(self):
  #   return reverse("app1:courses",kwargs={'pk':self.pk})
  
class Student(models.Model):
  sname = models.CharField(max_length=40)
  email = models.EmailField(max_length=50)
  city = models.CharField(max_length=30)
  contact = models.SmallIntegerField()
  course = models.ForeignKey(Course,null=True,on_delete=models.SET_NULL,related_name='students')

  def __str__(self):
    return str(self.course)