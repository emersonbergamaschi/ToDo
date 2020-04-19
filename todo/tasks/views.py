from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Task


def tasklist(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/list.html', {'tasks': tasks})

def taskview(request, id):
    task = get_object_or_404(Task, pk=id)
    return render(request, 'tasks/task.html', {'task': task})

def helloword(request):
    return HttpResponse('Hello World!')

def yourname(request, name):
    return render(request, 'tasks/yourname.html', {'name': name})
