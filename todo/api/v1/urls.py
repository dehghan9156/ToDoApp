from django.urls import path,include
from . import views
from rest_framework import routers
from rest_framework.routers import DefaultRouter

app_name='api-v1'

router = DefaultRouter()

router.register(r'todo',views.ToDoListViewSet,basename='todo')
urlpatterns = [
    path('', include(router.urls)),
]