from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from .models import Task

# Create your views here.
def task_list(request):
    tasks = Task.objects.all()
    # return HttpResponse({tasks})
    # return HttpResponse(f"List of Tasks: {tasks}")
    return render(request, 'todolist/todo_list.html', {'tasks': tasks})

def task_detail(request, id):
    task = get_object_or_404(Task, pk=id)
    return HttpResponse(f"Task detail: {task}")

def task_delete(request, id):
    task = get_object_or_404(Task, pk=id)
    if request.method == "POST":
        task.delete()
        return redirect("task_list")
    return HttpResponse(f"Task Delete: {task}")
