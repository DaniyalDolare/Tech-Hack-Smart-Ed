from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.views import View
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin



class SignupView(View):
    def get(self, request):
        return render(request, 'sign_up.html')
    
    def post(self, request):
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password')
        password2 = request.POST.get('password_confirm')
        
        if password1 != password2:
            messages.error(request, "Passwords do not match")
            return redirect('accounts:signup')
        
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken")
            return redirect('accounts:signup')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists")
            return redirect('accounts:signup')
        
        user = User.objects.create_user(username=username, email=email, password=password1)
        user.save()
        messages.success(request, "Account created successfully!")
        return redirect('accounts:login')
    


class LoginView(View):
    template_name = 'login.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('accounts:home')
        else:
            messages.error(request, "Invalid login credentials")
            return redirect('accounts:login')


class HomeView(LoginRequiredMixin,View):
    template_name = 'home.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
