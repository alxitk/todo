from django import forms
from django.views import generic

from app.models import Tag, Task


class TaskForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.SelectMultiple(
            attrs={
                "class": "form-control",
            }
        ),
        required=False,
    )

    class Meta:
        model = Task
        fields = ("content", "tags", "deadline", "is_done")
        widgets = {
            "content": forms.TextInput(
                attrs={
                    "placeholder": "Enter task name...",
                    "class": "form-control",
                }
            ),
            "deadline": forms.DateTimeInput(
                attrs={
                    "type": "datetime-local",
                    "class": "form-control",
                }
            ),
            "is_done": forms.CheckboxInput(
                attrs={
                    "class": "form-check-input",
                }
            ),
        }


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = "__all__"
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "placeholder": "Enter tag name...",
                    "class": "form-control",
                }
            ),
        }