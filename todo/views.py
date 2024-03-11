from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Tag, Task


class TaskListView(ListView):
    model = Task
    template_name = "to_do/index.html"
    context_object_name = "task_list_all"


class TaskDetailView(DetailView):
    model = Task


class TagListView(ListView):
    model = Tag