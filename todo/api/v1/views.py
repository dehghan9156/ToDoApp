from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from .serializer import ToDoSerializer
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated
from ... models import ToDo
from .permissions import IsOwnerOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend,OrderingFilter
from rest_framework import filters
from .pagination import DefaultPagination

class ToDoListViewSet(viewsets.ModelViewSet):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer
    permission_classes = [IsAuthenticated,IsOwnerOrReadOnly]
    filter_backends = [DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter]
    filterset_fields = ['title','complate']
    search_fields =['title']
    ordering_fields = ['complate']
    pagination_class = DefaultPagination

