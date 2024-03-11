from django.urls import path, include

from .views import (
    TaskListView,
    TaskCreateView,
    TaskUpdateView,
    TagListView,
    TagCreateView,
    TagUpdateView,
    TagDeleteView,
    task_toggle_status_view,
    TaskDeleteView,
)

urlpatterns = [
    path("", TaskListView.as_view(), name="index"),
    path("create_task/", TaskCreateView.as_view(), name="task-create"),
    path("tags/", TagListView.as_view(), name="tag-list"),
    path("tags/create/", TagCreateView.as_view(), name="tag-create"),
    path("<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"),
    path("tags/<int:pk>/update/", TagUpdateView.as_view(), name="tag-update"),
    path("tags/<int:pk>/delete/", TagDeleteView.as_view(), name="tag-delete"),
    path("tags/<int:pk>/delete/", TaskDeleteView.as_view(), name="task-delete"),
    path('task/<int:pk>/toggle-status/', task_toggle_status_view, name='task-toggle-status'),
]

app_name = "todo"
