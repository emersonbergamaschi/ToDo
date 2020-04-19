from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.core.paginator import Paginator
from .forms import TaskForm
from .models import Task


def tasklist(request):
    tasks_list = Task.objects.all().order_by('-created_at')

    paginator = Paginator(tasks_list, 4)

    page = request.GET.get('page')

    tasks = paginator.get_page(page)

    return render(request, 'tasks/list.html', {'tasks': tasks})

def taskview(request, id):
    task = get_object_or_404(Task, pk=id)
    return render(request, 'tasks/task.html', {'task': task})

def newtask(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.done = 'doing'
            task.save()
            return redirect('/')
    else:
        form = TaskForm
        return render(request, 'tasks/addtask.html', {'form': form})

def edittask(request, id):
    task = get_object_or_404(Task, pk=id)
    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            task.save()
            return redirect('/')
        else:
            return render(request, 'tasks/edittask.html', {'form': form, 'task': task})
    else:
        return render(request, 'tasks/edittask.html', {'form': form, 'task': task})

def deletetask(request, id):
    task = get_object_or_404(Task, pk=id)
    task.delete()

    messages.info(request, 'Tarefa deletada com sucesso!')

    return redirect('/')

def helloword(request):
    return HttpResponse('Hello World!')

def yourname(request, name):
    return render(request, 'tasks/yourname.html', {'name': name})
