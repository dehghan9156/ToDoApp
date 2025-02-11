from django.contrib import admin
from django.urls import path
from . import views

app_name='todo'

urlpatterns = [
    path('',views.ListToDoView.as_view(),name='list_todo'),
    path('create/', views.CreateToDoView.as_view(), name='create_todo'),
    path('delete/<int:pk>/',views.DeleteToDoView.as_view(),name='delete_todo'),
    path('update/<int:pk>/',views.UpdateToDoView.as_view(),name='update_todo'),
    path('done/<int:pk>/',views.DoneStateView.as_view(),name='done_todo'),
]