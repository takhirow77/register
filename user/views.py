from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .models import User
from django.contrib import messages
# Create your views here.
def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")
        if password == confirm_password and username and password and email and phone:
            # Создайте пользователя и установите его атрибуты
            user = User.objects.create_user(username=username, email=email, password=password)
            user.phone = phone
            user.save()

            # Аутентифицируйте пользователя и выполните вход
            user = authenticate(request=request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('profile', user.id)  # Перенаправьте на профиль пользователя

    return render(request, 'register.html', locals())


def index(request):
    return render(request, 'index.html', locals())

def profile(request,id):
    user = User.objects.get(id=id)
    return render(request, 'profile.html', locals())

def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(username = username)
        except:
            messages.error(request, 'Пользователь с таким именем не существует.')
            return redirect('login')
        user = authenticate(username=username, password = password)
        if user is not None:
            login(request, user)
            return redirect('profile', request.user.id)
        else:
            messages.error(request, 'Неправильный пароль')
            return redirect('login')
    return render(request, 'login.html', locals())