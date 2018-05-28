from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.

def login(request):
    # name = request.POST.get('name')
    # request.session['uname'] =  name
    return render(request,'test_django/login.html')

def login_handle(request):

    name = request.POST.get('name')
    request.session['uname'] = name
    return redirect('/test/userinfo')

def showdetail(request):
    name = request.session.get('uname','未登录')
    context = {'myname':name}
    return render(request, 'test_django/userinfo.html', context)

def deletesession(request):
    del request.session['uname']
    return redirect('/test/userinfo')
