from django.urls import path,include,re_path
from . import views
from django.urls import re_path as url
from django.contrib.auth import login , logout


app_name='unit_app'
urlpatterns = [
    path('',views.demo, name='home'),
    path('p8',views.p8, name='دليل الرائدة الريفية'),
    path('p9',views.p9, name='التطعيمات'),
    path('p10',views.p10, name='التواصل'),
    path('الجميع',views.p1, name='الجميع'),
    path('p2',views.p2, name='تسجيل دخول المريض'),
    path('p3',views.p3, name='تسجيل دخول دكتور'),
    
    path('التعديل_والحذف_للأقسام',views.التعديل_والحذف_للأقسام, name='التعديل_والحذف_للأقسام'),
    path('التعديل_والحذف_للخدمات',views.التعديل_والحذف_للخدمات, name='التعديل_والحذف_للخدمات'),
    path('التعديل_والحذف_للمنشورات',views.التعديل_والحذف_للمنشورات, name='التعديل_والحذف_للمنشورات'),
    path('السجلات',views.السجلات, name='السجلات'),
    path('doctor-home',views.doctorHome, name='doctor_home'),

    path('update_post/<int:id>',views.update_post, name='update_post'),
    path('delete_post/<int:id>',views.delete_post, name='delete_post'),
    
    path('update_department/<int:id>',views.update_department, name='update_department'),
    path('delete_department/<int:id>',views.delete_department, name='delete_department'),

    path('update_services/<int:id>',views.update_services, name='update_services'),
    path('delete_Services/<int:id>',views.delete_Services, name='delete_Services'),

    
    
    
    
    
    path('p5',views.department_list.as_view(), name='department_list'),
    path('p6/<int:pk>',views.department_Detail.as_view(), name='department_Detail'),

    
    
    path('p11',views.demo, name='services_list'),
    path('p12/<int:pk>',views.services_Detail.as_view(), name='services_Detail'),

    path('p7',views.p7, name='pop'),
    path('نبذة_عن',views.نبذة_عن, name='نبذة_عن'),
    path('الادمن',views.الادمن, name='admin'),
    path('send-mail',views.sendMail, name='sendmail')
    

]