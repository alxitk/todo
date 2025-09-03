from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=100)

class Task(models.Model):
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(auto_now=True)
    is_done = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag)
