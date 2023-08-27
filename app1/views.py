from django.shortcuts import render,HttpResponseRedirect
from django.views import View
from django.views.generic import DeleteView
from app1.models import Course
from app1.forms import CourseForm
from django.urls import reverse_lazy

# Create your views here.

def index(request):
    form = CourseForm()
    courses = Course.objects.all()
    context = {'courses':courses,'form':form}
    return render(request,'app1/index.html',context)

def courses(request):
    courses = Course.objects.all()
    context = {'courses':courses}
    return render(request,'app1/courses.html',context)

# def updateCourse(request,id):
#     print(request)
#     course = Course.objects.get(id=id)
#     form = CourseForm(instance=course)
#     context = {'form':form}
#     return render(request,'app1/updatecourse.html',context)

class MyCourse(View):

    def get(self,request,id=None):
        if id is None:
            form = CourseForm()
            context = {'form':form}
            return render(request,'app1/index.html',context)
        else:
            course = Course.objects.get(id=id)
            form = CourseForm(instance=course)
            context = {'form':form,'id':id}
            return render(request,'app1/updatecourse.html',context)

    def post(self,request,id=None):
        if id is None and request.POST:
            form = CourseForm(request.POST)
            if form.is_valid():
                form.save()
            else:
                print("Form data not valid")
        else:
            course = Course.objects.get(id=id)
            print(course)
            form = CourseForm(request.POST,instance=course)
            print(request.POST)
            if form.is_valid():
                form.save()
            else:
                print("Invalid Form Data")
        return HttpResponseRedirect('/')
    

class DeleteCourse(DeleteView):
    model = Course
    template_name = 'app1/index.html'
    success_url = reverse_lazy('index')



            



