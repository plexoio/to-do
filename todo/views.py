from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
# Create your views here.

#  READ


def get_my_list(request):
    tasks = Task.objects.all()
    context = {
        'task': tasks
    }
    return render(request, 'todo/todo_list.html', context)

# CREATE


def add_task(request):
    if request.method == "POST":
        name = request.POST.get('name')
        completed = 'completed' in request.POST
        Task.objects.create(name=name, completed=completed)
        return redirect('get_my_list')
    return render(request, 'todo/todo_add.html')

# UPDATE
# Get to READ & then UPDATE


def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    context = {
        'tasks': task
    }

    if request.method == "POST":
        task.name = request.POST.get('name')
        task.completed = 'completed' in request.POST
        task.save()
        return redirect('get_my_list')

    return render(request, 'todo/todo_edit.html', context)

# TOGGLE update


def toggle_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.completed = not task.completed
    task.save()
    return redirect('get_my_list')

# DELETE


def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('get_my_list')
