from django.urls import path,include
from .views import *

app_name = 'accounts'

urlpatterns = [
    path('signup/',SignupView.as_view(),name='signup'),
    path('login/',LoginView.as_view(),name='login' ),
    path('home/',HomeView.as_view(),name='home' ),
    path('user_role/',OptionView.as_view(),name='user_role')

]
