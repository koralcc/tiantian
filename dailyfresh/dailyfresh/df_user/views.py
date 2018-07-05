# encoding: utf-8
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import User
import hashlib
import logging
logger = logging.getLogger(__name__)

# Create your views here.
def index(request):

    return render(request, 'index.html')

def register(request):

    return render(request,'user/register.html')

def login(request):
    return render(request,'user/login.html')

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
    user.password = str_to_sha1UTF8(cpwd)
    user.email = email
    user.save()
    # 注册成功跳转到login页面
    return redirect('/user/login')

def login_handle(request):
    post = request.POST
    name = post.get('username')
    password = post.get('pwd')

    # sha1为单向加密算法，没有解密方法，只能把数据库存储的sha加密密码与输入的密码进行加密后对比

    sha1pwd = str_to_sha1UTF8(password)
    pwd_d = User.objects.get(name = name).password
    logger.debug("hello, world")
    if pwd_d == sha1pwd:
        return redirect('/user/index')
    else :
        # return None
        pass

# 字符串转sha1
def str_to_sha1UTF8(strp):
    hash = hashlib.sha1()
    hash.update(str(strp).encode('utf-8'))
    return hash.hexdigest()



