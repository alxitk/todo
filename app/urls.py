from django.urls import path

from app.views import (TasksListView,
                       TaskCreateView,
                       TaskUpdateView,
                       TaskDeleteView,
                       task_toggle,
                       TagListView,
                       TagCreateView,
                       TagUpdateView,
                       TagDeleteView)

app_name = "todo"

urlpatterns = [
    path("", TasksListView.as_view(), name="task-list", ),
    path("create/", TaskCreateView.as_view(), name="task-create", ),
    path("update/<int:pk>/", TaskUpdateView.as_view(), name="task-update", ),
    path("delete/<int:pk>/", TaskDeleteView.as_view(), name="task-delete", ),
    path("toggle/<int:pk>/", task_toggle, name="task_toggle", ),
    path("tags/", TagListView.as_view(), name="tags-list", ),
    path("tags/create/", TagCreateView.as_view(), name="tags-create", ),
    path("tags/update/<int:pk>/", TagUpdateView.as_view(), name="tags-update", ),
    path("tags/delete/<int:pk>/", TagDeleteView.as_view(), name="tags-delete", ),
]