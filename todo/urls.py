from django.urls import path, include

from .views import (
            TaskListView,
            TaskCreateView,
            TagListView,
            TagCreateView,
            TagUpdateView,
            TagDeleteView,
)

urlpatterns = [
    path("", TaskListView.as_view(), name="index"),
    path("create_task/", TaskCreateView.as_view(), name="task-create"),
    path("tags/", TagListView.as_view(), name="tag-list"),
    path("tags/create/", TagCreateView.as_view(), name="tag-create"),
    path("tags/<int:pk>/update/", TagUpdateView.as_view(), name="tag-update"),
    path("tags/<int:pk>/delete/", TagDeleteView.as_view(), name="tag-delete"),
]

app_name = "todo"
