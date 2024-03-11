from django.urls import path, include

from .views import TagListView, TaskListView, TaskDetailView

urlpatterns = [
    path("", TaskListView.as_view(), name="index"),
    path("tags/", TagListView.as_view(), name="tag_list")
]

app_name = "todo"
