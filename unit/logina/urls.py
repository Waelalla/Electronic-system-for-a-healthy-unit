from django.urls import path,include,re_path

from . import views
from .views import profile
from django.urls import re_path as url
from .views import signup , user_activte


app_name='logina'

urlpatterns = [
    path('profile/',profile,name='profile'),
    path('main-login/',views.mainLogin,name='main_login'),
    path('main-login_/',views.mainLogin_,name='main_login_'),
    path('signup/',signup,name='signup'),
    path('<str:username>/activate' , user_activte, name='user_activte')
]


