from django.urls import path,include
from .views import *
app_name = 'course'


urlpatterns = [
    path('all/', CourseListView.as_view(),name='courses'),
    path('add/', AddCourseView.as_view(),name='add-course'),
]
