from django.shortcuts import render
from django.shortcuts import redirect
from .models import Task
from .forms import TaskCreationForm


def index(request):
    tasks = Task.objects.all()
    params = {
        'tasks': tasks,
    }
    return render(request, 'tasks/index.html', params)


def create(request):
    if (request.method == 'POST'):
        title = request.POST['title']
        content = request.POST['content']
        task = Task(title=title, content=content)
        task.save()
        return redirect('tasks:index')
    else:
        params = {
            'form': TaskCreationForm(),
        }
        return render(request, 'tasks/create.html', params)


def detail(request, task_id):
    task = Task.objects.get(id=task_id)
    params = {
        'task': task,
    }
    return render(request, 'tasks/detail.html', params)


def edit(request, task_id):
    task = Task.objects.get(id=task_id)
    if (request.method == 'POST'):
        task.title = request.POST['title']
        task.content = request.POST['content']
        task.save()
        return redirect('tasks:detail', task_id)
    else:
        form = TaskCreationForm(initial={
            'title': task.title,
            'content': task.content,
        })
        params = {
            'task': task,
            'form': form,
        }
        return render(request, 'tasks/edit.html', params)


def delete(request, task_id):
    task = Task.objects.get(id=task_id)
    if (request.method == 'POST'):
        task.delete()
        return redirect('tasks:index')
    else:
        params = {
            'task': task,
        }
        return render(request, 'tasks/delete.html', params)
