from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm, RegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def task(request):
    if request.user.is_authenticated: 
        tasks = Task.objects.filter(username=request.user)
    else:
        tasks = Task.objects.none()

    context = {
        'tasks':tasks
    }
    return render(request, 'todo/task_list.html', context)

@login_required
def detail(request, pk):
    task = Task.objects.get(pk=pk)
    context = {
        'task':task,
    }
    return render(request, 'todo/detail.html', context) 

@login_required
def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST or None)
        if form.is_valid():
            task = form.save()
            task.username = request.user
            task.save()
            return redirect('todo:task')
    else:
        form = TaskForm()

    context = {
        'form':form
    }
    return render(request, 'todo/task-form.html', context)

@login_required
def update_task(request, pk):
    task = Task.objects.get(pk=pk)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('todo:detail', task.pk)
    else:
        form = TaskForm(instance=task)
    
    context = {
        'task':task, 'form':form
    }

    return render(request, 'todo/task-form.html', context)

@login_required
def delete_task(request, pk):
    task = Task.objects.get(pk=pk)

    if request.method == 'POST':
        task.delete()
        return redirect('todo:task')
    
    context = {
        'task':task,
    }
    
    return render(request, 'todo/item-delete.html', context)


def register(request):
    if request.method =='POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Welcome {username}, your account is created!')
            return redirect('todo:login')
    else:
        form = RegisterForm()

    context = {
        'form':form
    }
    return render(request, 'todo/register.html', context)


