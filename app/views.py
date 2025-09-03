from django.shortcuts import render
from django.views import generic

from app.models import Task


class TasksListView(generic.ListView):
    model = Task
    context_object_name = "task_list"
    template_name = "app/task_list.html"
