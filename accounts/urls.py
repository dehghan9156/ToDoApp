from django.contrib import admin
from django.urls import path
from . import views

app_name='accounts'

urlpatterns = [
    path('register/',views.RegisterUserView.as_view(),name='register_user'),
    path('login/',views.LoginUserView.as_view(),name='login_user'),
    path('logout/',views.LogoutUserView.as_view(),name='logout_user'),
]