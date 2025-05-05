from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.homepage, name='homepage'),

    path('tasks/', views.tasks, name='tasks'),
    path('tasks/create_task/', views.create_task, name='create_task'),
    path('tasks/<int:task_id>/delete/', views.delete_task, name="task_delete"),
    path('tasks/<int:task_id>/toggle/', views.toggle_task_completion, name="task_toggle"),
    path('tasks/<int:task_id>/view/', views.view_task, name="view_task"),
    path('tasks/<int:task_id>/edit/', views.edit_task, name="edit_task"),

    path('search/', views.SearchResults.as_view(), name='search_results'),
]
