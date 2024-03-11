from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Tag, Task


class TaskListView(ListView):
    model = Task
    template_name = "to_do/index.html"
    context_object_name = "task_list_all"


class TagListView(ListView):
    model = Tag
    context_object_name = "tag_list_all"
    template_name = "to_do/tag_list.html"


class TaskCreateView(CreateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("")
    template_name = "to_do/task_form.html"


class TagCreateView(CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo:tag-list")
    template_name = "to_do/tag_form.html"


class TagUpdateView(UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo:tag-list")
    template_name = "to_do/tag_form.html"


class TagDeleteView(DeleteView):
    model = Tag
    success_url = reverse_lazy("todo:tag-list")
    template_name = "to_do/tag_delete_confirm.html"
