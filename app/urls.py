from django.urls import path

from app.views import TasksListView, TaskCreateView

app_name = "todo"

urlpatterns = [
    path("", TasksListView.as_view(), name="task-list", ),
    path("create/", TaskCreateView.as_view(), name="task-create", ),
]