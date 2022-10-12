from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from todolist.models import Task
from django.core import serializers


@login_required(login_url='todolist:login')
def show_todolist(request):
    data_task = Task.objects.filter(user=request.user)
    context = {
        'task_list': data_task,
        'nama': request.user.username,
        'npm': '2106750906',
        'last_login': request.COOKIES['last_login'],
    }
    return render(request, 'todolist.html', context)


def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')

    context = {'form': form}
    return render(request, 'register.html', context)


def login_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)  # melakukan login terlebih dahulu
            response = HttpResponseRedirect(
                reverse("todolist:show_todolist"))  # membuat response
            # membuat cookie last_login dan menambahkannya ke dalam response
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Username atau Password salah!')

    context = {}
    return render(request, 'login.html', context)


def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response


@login_required(login_url='todolist:login')
def create_task(request):
    if request.method == "POST":
        user = request.user
        title = request.POST.get("title")
        description = request.POST.get("description")
        create_new_task = Task(user=user, title=title, description=description)
        create_new_task.save()
        return redirect('todolist:show_todolist')

    return render(request, "create_task.html")


def delete_task(request, id):
    task = Task.objects.get(id=id)
    task.delete()
    return redirect('todolist:show_todolist')


def update_task(request, id):
    task = Task.objects.get(id=id)
    task.is_finished = not task.is_finished
    task.save()
    return redirect('todolist:show_todolist')

# assignment 6


def show_todolist_json(request):
    # mengembalikan semua data task dalam bentuk json (Task 6)
    data = Task.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")


def create_task_modal(request):
    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')
        task = Task(user=request.user, title=title, description=description)
        task.save()
        return redirect('todolist:show_todolist')
    return render(request, 'create_task.html')
