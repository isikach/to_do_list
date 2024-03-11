from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from .models import Tag, Task


class TaskListView(ListView):
    model = Task
    template_name = "to_do/index.html"
    context_object_name = "task_list_all"

    def get_queryset(self):
        return Task.objects.order_by('done', 'deadline')


class TagListView(ListView):
    model = Tag
    context_object_name = "tag_list_all"
    template_name = "to_do/tag_list.html"


class TaskCreateView(CreateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("todo:index")
    template_name = "to_do/task_form.html"


class TaskUpdateView(UpdateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("todo:index")
    template_name = "to_do/task_form.html"

class TaskDeleteView(DeleteView):
    model = Task
    success_url = reverse_lazy("todo:index")
    template_name = "to_do/delete_confirm.html"


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
    template_name = "to_do/delete_confirm.html"

def task_toggle_status_view(request, pk):
    if request.method == 'POST':
        task = get_object_or_404(Task, pk=pk)
        task.done = not task.done
        task.save()
        return redirect("todo:index")
