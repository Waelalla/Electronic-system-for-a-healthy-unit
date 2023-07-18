from . import views
from django.urls import re_path as url
from .views import signup , user_activte
from django.urls import path,include,re_path


app_name='accounts'

urlpatterns = [
    path('signup/',signup,name='signup'),
]


