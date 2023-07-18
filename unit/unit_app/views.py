from django.shortcuts import redirect, render ,get_object_or_404
from helpers import isAdmin, isDoctor

from logina.models import LoginUser
from  .models import *
from django.views.generic import ListView, DetailView
from django.conf import settings
from django.contrib.auth.models import  User
# Create your views here.
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect,HttpResponse
from .models import accountForm
from .form import formacc , departmentle , poste,servicese
from django.core.mail import send_mail




#-------الصفحه الرئيسيه------#
def demo(request):
    context = {
        'sectionss': sections.objects.all,
        'posts': post.objects.all,
        'initiativess': initiatives.objects.all,
        'services' : services.objects.all
    }
    return render(request, 'pages/index.html',context)
#-------النهايه---------#




#-------الاقسام ------#
    
class department_list(ListView):
    model=department
    
#-------النهايه---------#




#------- الاقسام------#

class department_Detail(DetailView):
    model=department 
        
#-------النهايه---------#



  
#-------الصفحه ------#

def p7(request):
    return render (request,'pages/pop.html',)

#-------النهايه---------#




#------- دليل الرائدة الريفية------#

def p8(request):
    return render (request,'pages/دليل الرائدة الريفية.html',)

#-------النهايه---------#




#------- التطعيمات------#

def p9(request):
    return render (request,'pages/التطعيمات.html',)

#-------النهايه---------#




#-------التواصل ------#

def p10(request):
    return render (request,'pages/التواصل.html',)

#-------النهايه---------#




#------- الخدمات------#

class services_list(ListView):
    model=services

#-------النهايه---------#



    
#-------الخدمات  ------#

class services_Detail(DetailView):
    model=services     

#-------النهايه---------#



#-------صفحه تسجيل دخول المستخدم----#
def p2(request):
    username = request.POST.get('username')
    age = request.POST.get('age')
    id = request.POST.get('id')
    address= request.POST.get('address')
    sons = request.POST.get('sons')
    man = request.POST.get('man')
    girl = request.POST.get('girl')
    maritalstatus = request.POST.get('maritalstatus')
    data = login_user(user_name=username,
                      age=age,
                      id_user=id,
                      address=address,
                      sons_cont=sons,
                      man_cont=man,
                      girl_cont=girl,
                      marital_status=maritalstatus)
    data.save()
    return render (request,'pages/تسجيل دخول مريض.html',)
#-------النهايه---------#


#-----صفحه تسجيل دخول الجميع-----#
def p1(request):
    return render (request,'pages/تسجيل دخول الجميع.html',)
#-------النهايه---------#

#------صفحه تسجيل الطبيب-----#
def p3(request):
    return render (request,'pages/تسجيل دخول دكتور.html',)
#-------النهايه---------#

#------  نبذه عن-----#
def نبذة_عن(request):
    return render (request,'pages/نبذة عن.html',)
#-------النهايه---------#


#------الادمن-----#
def الادمن(request):
    
    if(isAdmin(request=request)):
        if request.method == 'POST':
            add_departmentl = departmentle(request.POST,request.FILES)
            if add_departmentl.is_valid():
                add_departmentl.save()
                
            add_poste = poste(request.POST, request.FILES)
            if add_poste.is_valid():
                add_poste.save()
                
                
            add_poste = servicese(request.POST, request.FILES)
            if add_poste.is_valid():
                add_poste.save()

        context = {
            'form_departmente' : departmentle(),
            'form_post':poste( ),
            'form_services':servicese( )

        }

        return render (request,'pages/الادمن.html',context)
    return redirect('/accounts/main-login')

def sendMail(request):
    if(request.method == 'POST'):
        # user = User.objects.first(email=request.POST['email'])
        # if(user):
        senderEmail = request.POST['email']
        sendMsg = send_mail(
            "Health Unit",
            request.POST['msg'] + f"\nFrom : {senderEmail}",
            settings.EMAIL_HOST_USER,
            [settings.EMAIL_HOST_USER],
            fail_silently=False)
    
        if(sendMsg):
            return redirect('/')   
    return redirect('/')   

#-------النهايه---------#

#-------الصفحه ------#

def التعديل_والحذف_للأقسام(request):
    return render (request,'pages/التعديل والحذف للأقسام.html',)

#-------النهايه---------#

#-------الصفحه ------#

def التعديل_والحذف_للخدمات(request):
    return render (request,'pages/التعديل والحذف للخدمات.html',)

#-------النهايه---------#

#-------الصفحه ------#

def التعديل_والحذف_للمنشورات(request):
    return render (request,'pages/التعديل والحذف للمنشورات.html',)

#-------النهايه---------#


#-------الصفحه ------#

def السجلات(request):
    if(isDoctor(request=request)):
        patients = LoginUser.objects.filter(role='patient')
        return render (request,'pages/السجلات.html',{'patients':patients})
    return redirect('/')

#-------النهايه---------#

#-------الصفحه ------#

def doctorHome(request):
    if(isDoctor(request=request) or isAdmin(request=request)):
        return render (request,'pages/doctor-home.html')
    return redirect('/accounts/main-login')
    
#-------النهايه---------#







def update_post(request, id):
    books_id = post.objects.get(id=id)
    if request.method == 'POST':
        book_save = poste( request.POST, request.FILES,  instance=books_id)
        if book_save.is_valid():
            book_save.save()
            return redirect('/')
    else:
        book_save= poste(instance=books_id)
    context ={
        'form':book_save,
    }            
    return render(request, 'pages/update_post.html', context)



def delete_post(request,id):
    book_delete = get_object_or_404(post, id=id)
    if request.method == 'POST':
        book_delete.delete()
        return redirect('/')
    
    return render(request, 'pages/delete_post.html')


















def update_department(request, id):
    books_id = department.objects.get(id=id)
    if request.method == 'POST':
        book_save = departmentle( request.POST, request.FILES,  instance=books_id)
        if book_save.is_valid():
            book_save.save()
            return redirect('/')
    else:
        book_save= departmentle(instance=books_id)
    context ={
        'form':book_save,
    }            
    return render(request, 'pages/update_departmentle.html', context)



def delete_department(request,id):
    book_delete = get_object_or_404(department, id=id)
    if request.method == 'POST':
        book_delete.delete()
        return redirect('/')
    
    return render(request, 'pages/delete_department.html')


def التعديل_والحذف_للمنشورات(request):
    
    context = {
        'poste':post.objects.all(),

    }
    return render(request, 'pages/التعديل والحذف للمنشورات.html',context)


def التعديل_والحذف_للأقسام(request):
    
    context = {
        'departmentse':department.objects.all(),

    }
    return render(request, 'pages/التعديل والحذف للأقسام.html',context)



def التعديل_والحذف_للخدمات(request):
    
    context = {
        'servicese':services.objects.all(),

    }
    return render(request, 'pages/التعديل والحذف للخدمات.html',context)



def update_services(request, id):
    books_id = services.objects.get(id=id)
    if request.method == 'POST':
        book_save = servicese( request.POST, request.FILES,  instance=books_id)
        if book_save.is_valid():
            book_save.save()
            return redirect('/')
    else:
        book_save= servicese(instance=books_id)
    context ={
        'form':book_save,
    }            
    return render(request, 'pages/update_services.html', context)



def delete_Services(request,id):
    book_delete = get_object_or_404(services, id=id)
    if request.method == 'POST':
        book_delete.delete()
        return redirect('/')
    
    return render(request, 'pages/delete_Services.html')

