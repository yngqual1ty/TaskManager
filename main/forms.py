from django.forms import ModelForm
from .models import Task
from django.contrib.auth.models import User

class CreateTaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'deadline', 'priority']
        labels = {
            'title': 'Задача',
            'description': 'Описание задачи',
            'deadline' : 'Срок выполнения',
            'priority' : 'Приоритет'
        }



class EditTaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'deadline', 'priority']
        labels = {
            'title': 'Задача',
            'description': 'Описание задачи',
            'deadline' : 'Срок выполнения',
            'priority' : 'Приоритет'
        }

