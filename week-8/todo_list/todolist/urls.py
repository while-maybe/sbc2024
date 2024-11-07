"""Define URL patterns for the tasks"""

from django.urls import path

from . import views

app_name = 'todolist'

urlpatterns = [
    path('', views.task_list, name='task_list'), # URL to list tasks
    path('task/<int:id>/', views.task_detail, name='task_detail'),
    path('task/<int:id>/delete', views.task_delete, name='task_delete'),
]
