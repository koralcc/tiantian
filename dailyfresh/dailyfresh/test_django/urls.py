from django.urls import path,re_path
from . import views
app_name = 'test_django'
urlpatterns = [
    re_path(r'^login/',views.login,name ='login'),
    re_path(r'^login_handle/',views.login_handle),
    re_path(r'^userinfo/',views.showdetail),
    re_path(r'^deletesession/',views.deletesession,name='deletesession')

]