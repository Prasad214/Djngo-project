from django.urls import path
from app1 import views

app_name = 'app1'

urlpatterns = [
    path('newcourse',views.MyCourse.as_view(),name='newcourse'),
    path('updatecourse/<int:id>',views.MyCourse.as_view(),name='updatecourse'),
    path('deletecourse/<int:pk>',views.DeleteCourse.as_view(),name='deletecourse'),
]
