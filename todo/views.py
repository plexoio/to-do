from django.shortcuts import render
from .models import Task
# Create your views here.


def get_my_list(request):
    tasks = Task.objects.all()
    context = {
        'task': tasks
    }
    return render(request, 'todo/todo_list.html', context)