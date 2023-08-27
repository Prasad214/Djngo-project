from django.contrib import admin
from app1.models import Course,Student

# Register your models here.

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['id','cname','dur','fee','trainer']

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id','sname','email','city','contact','course']
