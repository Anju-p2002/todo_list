from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Task, Category
from .forms import TaskForm



# # Create your views here.

def example(request):
    return render(request,'example.html')

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

        username = request.POST.get("email")
        password = request.POST.get("password")

        User.objects.create_user(username=username,password=password)

        return redirect("login")

    return render(request,"signup.html")


def dashboard(request):

    if not request.user.is_authenticated:
        return redirect("login")

    return render(request,"dashboard.html")


def logout_view(request):

    logout(request)

    return redirect("card")


def dashboard(request):
    tasks = Task.objects.all()

    active_tasks = tasks.filter(is_completed=False).count()
    completed_tasks = tasks.filter(is_completed=False).count()
    categories = Category.objects.all()

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
        'categories_count': categories.count(),
        'form': form
    })


def addtask(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = TaskForm()

    return render(request, 'addtask.html', {'form': form})