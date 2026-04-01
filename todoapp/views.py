from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, get_object_or_404
from .models import Task,Category
from .forms import TaskForm
from todoapp.models import Category



# # Create your views here.



def card(request):
        if request.method == "POST":

           username = request.POST.get("email")
           password = request.POST.get("password")

           user = authenticate(request, username=username, password=password)

           if user is not None:
               login(request, user)
               return redirect("dashboard")


        return render(request,'card.html')



def signup_view(request):

    if request.method == "POST":

        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        User.objects.create_user(username=username,email=email,password=password)

        return redirect("card")

    return render(request,"signup.html")

def logout_view(request):

    logout(request)

    return redirect("card")


def dashboard(request):
    tasks = Task.objects.all()
        
    active_tasks=tasks.filter(is_completed=False).count()
    completed_tasks=tasks.filter(is_completed=True).count()
    categories=Category.objects.all()
    category_count=categories.count()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = TaskForm()

    return render(request, 'dashboard.html', {
        'tasks': tasks,
        'active_tasks': active_tasks,
        'completed_tasks': completed_tasks,
        'categories':categories,
        'category_count':category_count,
        'form': form
    })

Category.objects.create(name="Home")
Category.objects.create(name="Work")
Category.objects.create(name="Personal")
Category.objects.create(name="Client")

def addtask(request):
    categories = Category.objects.all()

    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        due_date = request.POST.get('due_date')
        time = request.POST.get('time')
        priority = request.POST.get('priority')
        category_id = request.POST.get('category') or None

        
        Task.objects.create(
            title=title,
            description=description,
            due_date=due_date,
            time=time,
            priority=priority,
            category_id=category_id
        )

        return redirect('dashboard')

    return render(request, 'addtask.html', {'categories': categories})

def updatetask(request, task_id):
    task = Task.objects.get(id=task_id)

    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = TaskForm(instance=task)

    return render(request, 'updatetask.html', {'form':form,})


def deletetask(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('dashboard')

def complete(request, task_id):
    task = Task.objects.get(id=task_id)

    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = TaskForm()

    return render(request, 'completetask.html', {'form':form,'task':task})


def completetask(request, task_id):
    task = Task.objects.get(id=task_id)
    task.is_completed = True
    task.save()
    return redirect('dashboard')
