from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic import DetailView,FormView,CreateView,UpdateView,DeleteView,View
from . models import ToDo
from .forms import ToDoCreateForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


class ListToDoView(ListView):
    model = ToDo
    context_object_name = 'todos'
    template_name = 'todo/listtodo.html'
    ordering = 'complate','created_date'
class CreateToDoView(LoginRequiredMixin,CreateView):
    model = ToDo
    # fields = ['title']
    form_class = ToDoCreateForm
    success_url = reverse_lazy("todo:list_todo")
    template_name = 'todo/createtodo.html'
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class DeleteToDoView(LoginRequiredMixin,DeleteView):
    model = ToDo
    success_url = reverse_lazy('todo:list_todo')
    template_name = 'todo/deletetodo.html'

class UpdateToDoView(LoginRequiredMixin,UpdateView):
    model = ToDo
    form_class = ToDoCreateForm
    success_url = reverse_lazy('todo:list_todo')
    template_name = 'todo/createtodo.html'

class DoneStateView(LoginRequiredMixin,View):
    def get(self,request,*args,**kwargs):
        todo = ToDo.objects.get(pk=kwargs['pk'])
        todo.complate = True
        todo.save()
        return redirect('todo:list_todo')