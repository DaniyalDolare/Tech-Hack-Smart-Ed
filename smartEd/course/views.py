from django.shortcuts import render, redirect
from django.views.generic import View,ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from accounts.models import Student,Teacher
from .models import *
from django.http import Http404

# Create your views here.
# class CourseListView(LoginRequiredMixin,View):
#     template_name = 'courses.html'
#
#     def get(self,request):
#         user = self.request.user
#         courses = Course.objects.all()
#         if Teacher.objects.filter(user=user).exists():
#             teacher_courses = courses.filter(owner=Teacher.objects.get(user=user)).all()
#             print(teacher_courses)
#         elif Student.objects.filter(user=user).exists():
#             enrollments = Enrollment.objects.filter(student=user)
#             student_courses = [enrollment.course for enrollment in enrollments]
#             print(student_courses)
#        
#         return render(request, 'courses.html', {'courses': courses})

class CourseListView(LoginRequiredMixin, ListView):
    template_name = 'courses.html'
    context_object_name = 'courses'

    def get_queryset(self):
        user = self.request.user
        # print(user.is_student)
        if Student.objects.filter(user=user).exists():
            queryset = Enrollment.objects.filter(student__user=user).select_related('course')
            print(queryset)
            return [enrollment.course for enrollment in queryset]
        elif Teacher.objects.filter(user=user).exists():
            teacher = Teacher.objects.get(user=user)
            queryset = Course.objects.filter(owner=teacher).order_by('name')
            print(queryset)
            return queryset
        else:   
            return Course.objects.none()
        
class AddCourseView(LoginRequiredMixin,View):

    def get(self,request):
        if not Teacher.objects.filter(user = self.request.user):
            print("==========not a teacher=============")
            raise Http404("Not Authorised")
        return render(request,'add_course.html')