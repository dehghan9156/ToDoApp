from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from .forms import RegisterUserForm,UserLogin


class RegisterUserView(View):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('todo:list_todo')
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        form = RegisterUserForm()
        return render(request, 'accounts/user_register.html', {'form': form})

    def post(self, request):
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = User.objects.create_user(username=cd['username'], email=cd['email'], password=cd['password'])
            messages.success(request, 'User Register Successfully', 'success')
            return redirect('todo:list_todo')
        else:
            messages.error(request, 'User not found', 'error')
            return render(request, 'accounts/user_register.html', {'form': form})

class LoginUserView(View):
    def get(self, request):
        form = UserLogin()
        return render(request, 'accounts/user_login.html', {'form': form})

    def post(self, request):
        form = UserLogin(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user is not None:
                login(request, user)
                messages.success(request, 'User Login Successfully', 'success')
                return redirect('todo:list_todo')
            else:
                messages.error(request, 'User not found', 'error')
        else:
            messages.error(request, 'Invalid form submission', 'error')

        return render(request, 'accounts/user_login.html', {'form': form})

class LogoutUserView(View):
    def get(self, request):
        logout(request)
        messages.success(request, 'User Logout Successfully', 'success')
        return redirect('todo:list_todo')

