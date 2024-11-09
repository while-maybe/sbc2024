"""Define URL patterns for the tasks"""

from django.urls import path

from . import views

app_name = 'todolist'

urlpatterns = [
    path('', views.task_list, name='task_list'), # URL to list tasks
    path('task/<int:task_id>/', views.task_detail, name='task_detail'),
    path('task/delete/<int:task_id>', views.task_delete, name='task_delete'),
    path('task/edit/<int:task_id>', views.task_edit, name='task_edit'),
    path('task/new', views.new_task, name='new_task'),
]
