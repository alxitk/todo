from django.urls import path

from app.views import TasksListView

app_name = "app"

urlpatterns = [
    path("", TasksListView.as_view(), name="task-list", ),
]