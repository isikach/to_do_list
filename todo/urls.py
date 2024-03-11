from django.urls import path, include

from .views import TagListView, TaskListView, TaskDetailView

urlpatterns = [
    path("", TaskListView.as_view(), name="index"),
]

app_name = "todo"
