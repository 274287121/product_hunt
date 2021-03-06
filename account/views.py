from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth


# Create your views here.


def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html')
    elif request.method == 'POST':
        user_name = request.POST['用户名']
        possword1 = request.POST['密码']
        possword2 = request.POST['确认密码']
        try:
            User.objects.get(username=user_name)
            return render(request, 'signup.html', {'用户名错误': '用户名已存在！'})
        except User.DoesNotExist:
            if possword1 != possword2:
                return render(request, 'signup.html', {'密码错误': '输入的密码不一致！'})
            else:
                User.objects.create_user(
                    username=user_name, password=possword1)
                return redirect('主页')


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        user_name = request.POST['用户名']
        possword = request.POST['密码']
        user = auth.authenticate(username=user_name, password=possword)
        if user is None:
            return render(request, 'login.html', {'错误': '用户或密码错误'})

        else:
            auth.login(request, user)
            return redirect('主页')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('主页')
