from django.urls import path

from app.views import (TasksListView,
                       TaskCreateView,
                       TaskUpdateView,
                       TaskDeleteView, task_toggle, )

app_name = "todo"

urlpatterns = [
    path("", TasksListView.as_view(), name="task-list", ),
    path("create/", TaskCreateView.as_view(), name="task-create", ),
    path("update/<int:pk>/", TaskUpdateView.as_view(), name="task-update", ),
    path("delete/<int:pk>/", TaskDeleteView.as_view(), name="task-delete", ),
    path("toggle/<int:pk>/", task_toggle, name="task_toggle", ),
]