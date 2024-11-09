from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django import forms

from .models import Task

# Create your views here.
def task_list(request):
    tasks = Task.objects.all()
    # return HttpResponse({tasks})
    # return HttpResponse(f"List of Tasks: {tasks}")
    context = {'tasks': tasks}
    return render(request, 'todolist/todo_list.html', context)

def task_detail(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    # return HttpResponse(f"Task detail: {task}")
    context = {'task': task}
    return render(request, 'todolist/task_detail.html', context)

def task_delete(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == "POST":
        task.delete()
        return redirect("todolist:task_list")
    # return HttpResponse(f"Task Delete: {task}")
    context = {'task': task}
    return render(request, 'todolist/task_detail.html', context)

def new_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            # 'converts' to True is checkbox has been clicked in form (value is 'on' for checked or 'None' for unchecked)
            task.completed = request.POST.get("completed") == 'on'
            task.save()
            return redirect('todolist:task_detail', task_id=task.id)
    else:
        form = TaskForm()
        context = {'form': form}
        return render(request, 'todolist/new_task.html', context)

def task_edit(request, task_id):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            # 'converts' to True is checkbox has been clicked in form (value is 'on' for checked or 'None' for unchecked)
            task.completed = request.POST.get("completed") == 'on'
            task.save()
            return redirect('todolist:task_detail', task_id=task.id)
    else:
        form = TaskForm()
        context = {'form': form}
        return render(request, 'todolist/new_task.html', context)

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('title', 'description', 'completed')
        

