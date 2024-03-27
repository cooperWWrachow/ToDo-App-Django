from datetime import date
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import Task
from .forms import TaskForm, RegisterForm
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import FormView
from django.contrib.auth import login
from django.utils import timezone

# Create your views here.

@login_required
def task(request):
    if request.user.is_authenticated: 
        tasks = Task.objects.filter(username=request.user)
        today_tasks = Task.objects.filter(due_date=timezone.now())
        today = date.today()
    else:
        tasks = Task.objects.none()

    context = {
        'tasks':tasks,
        'today_tasks':today_tasks,
        'today':today
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

class RegisterPage(FormView):
    template_name = 'todo/register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('todo:task')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)





