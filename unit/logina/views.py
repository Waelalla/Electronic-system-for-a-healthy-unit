from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from helpers import isAdmin, isDoctor

from logina import Backend
from .models import Child, LoginUser,User
from django.core.mail import send_mail
from django.http import HttpResponse
from .forms import SignupForm ,UserActivateForm
import json
# Create your views here.
def mainLogin(request):
    if(isDoctor(request=request) or isAdmin(request=request)):
        return redirect('/')
    return render(request,'main-login.html')

def mainLogin_(request):
    if(request.method == 'POST'):
        if('username' in request.POST and 'password' in request.POST):
            user = authenticate(request,username=request.POST['username'],password=request.POST['password'])
            if(user):
                login(request,user)
                if(isDoctor(request=request) or isAdmin(request=request)):
                    return redirect('departments:doctor_home')
                else:
                    return redirect('/accounts/profile')
            return HttpResponse('Username and Password not matched')
    return redirect('/accounts/login-as-doctor-v')

def profile(request):
    if(request.user.is_authenticated ):
        user=LoginUser.objects.filter(user__username=request.user).first()
        if(user.role in ['admin','doctor'] and 'username' in request.GET ):
            user=LoginUser.objects.filter(user__username=request.GET.get('username'),role='patient').first()  
        if(not user):
            return redirect('/')
        childs = Child.objects.filter(parent_id=user.user_id)
        request_user=LoginUser.objects.filter(user__username=request.user).first()
        return render(request,'registration/profile.html',{'request_user':request_user,'profile':user,'childs':childs})
    return redirect('/')

def signup(request):
    if request.method =='POST' :
        form = SignupForm(request.POST)
        if form.is_valid(): 
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            NationalId = form.cleaned_data['NationalId']
            address = form.cleaned_data['address']
            marital_status = form.cleaned_data['marital_status']
            image = form.cleaned_data['image']
            age=form.cleaned_data['age']
            myform=form.save()
            


            MyProfile =LoginUser.objects.get(user__username=username)


            MyProfile.active = False
            MyProfile.NationalId=NationalId
            MyProfile.address=address
            MyProfile.image=image
            MyProfile.marital_status=marital_status
            MyProfile.age=age
            MyProfile.save()
            
            parent = User.objects.filter(username=username).first()
            if(parent):
                if( 'boys[0][name]' in request.POST):
                    i = 0
                    while f'boys[{i}][name]' in request.POST:
                        Child.objects.create(
                            parent=parent,
                            name=request.POST[f'boys[{i}][name]'],
                            age=request.POST[f'boys[{i}][age]'],
                            national_id=request.POST[f'boys[{i}][national_id]'],
                            gender='male'
                        )
                        i+=1
                if( 'girls[0][name]' in request.POST):
                    i = 0
                    while f'girls[{i}][name]' in request.POST:
                        Child.objects.create(
                            parent=parent,
                            name=request.POST[f'girls[{i}][name]'],
                            age=request.POST[f'girls[{i}][age]'],
                            national_id=request.POST[f'girls[{i}][national_id]'],
                            gender='female'
                        )
                        i+=1
            #send email
            send_mail(
                subject="رمز تفعل الحساب الخاص بك",
                message=f"  استخدم هذا الكود لتفعيل حسابك الشخصي {MyProfile.code} ",
                from_email="health.unit.awysh.alhajer@gmail.com",
                recipient_list=[email],
                fail_silently=False
            )
            return redirect(f'/accounts/{username}/activate')         
    else:
        form = SignupForm()
    return render(request,'registration/signup.html',{'form':form})
 


def user_activte(request,username):
    MyProfile =LoginUser.objects.get(user__username=username)
    if request.method =='POST':
        form = UserActivateForm(request.POST)
        if form.is_valid():
            code = form.cleaned_data['code']
            if MyProfile.code == code:
                MyProfile.activate = True
                MyProfile.code=''
                MyProfile.code_used =True
                return redirect('/accounts/login')
                
    else:
        form = UserActivateForm()
    return render(request,'registration/activation.html',{'form':form})
