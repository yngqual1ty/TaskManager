from django.urls import path
from .views import TaskListCreateView, TaskDetailView


app_name = 'api'

urlpatterns = [
    path('tasks/', TaskListCreateView.as_view(), name='task-list'),
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),

]