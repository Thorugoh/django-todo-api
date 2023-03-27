from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.urls import reverse_lazy

from .models import Task

"""
API Overview
"""
@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List' : '/task-list/',
        'Detail View' : '/task-detail/<str:pk>/',
        'Create' : '/task-create/',
        'Update' : '/task-update/<str:pk>/',
        'Delete' : '/task-delete/<str:pk>/',
    }
    return Response(api_urls)


class TaskList(ListView):
    model = Task
    context_object_name ='tasks'
    
class TaskDetail(DetailView):
    model = Task
    context_object_name ='task'
    template_name = 'api/task.html'
    
class TaskCreate(CreateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasks')
    
class TaskUpdate(UpdateView): 
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasks')
    
class TaskDelete(DeleteView): 
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')