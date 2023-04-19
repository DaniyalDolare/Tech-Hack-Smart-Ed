from django.urls import path,include
from . import views

app_name = 'accounts'

urlpatterns = [
    path('signup-teacher/',views.SignupTeacherView.as_view(),name='signup-teacher'),
    path('signup-student/',views.SignupStudentView.as_view(),name='signup-student'),
    path('login/',views.LoginView.as_view(),name='login' ),
    path('home/',views.HomeView.as_view(),name='home' ),

]
