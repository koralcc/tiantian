from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import User
# Create your views here.
def index(request):

    return render(request, 'index.html')

def register(request):

    return render(request,'register.html')

def register_handle(request):

    # 接受用户输入
    post = request.POST
    user_name = post.get('user_name')
    pwd = post.get('pwd')
    cpwd = post.get('cpwd')
    email = post.get('email')
    if pwd != cpwd :
        print('密码不相等'+pwd+'&'+cpwd)
        return redirect('/user/register/')
    # 密码加锁
    # 创建对象
    user = User()
    user.name = user_name
    user.password = pwd
    user.email = email
    user.save()
    # 注册成功跳转到login页面
    return render(request,'/user/login/')
