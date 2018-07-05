## 配置子url
from django.urls import path,re_path
from . import views

app_name ='user'
urlpatterns = [
    re_path(r'^index$',views.index),
    re_path(r'^register$',views.register),
    re_path(r'^register_handle$',views.register_handle),
    re_path(r'^login$',views.login,name='login'),
    re_path(r'^login_handle$',views.login_handle),
]