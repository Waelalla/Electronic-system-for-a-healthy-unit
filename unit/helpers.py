from django.shortcuts import redirect
from logina.models import LoginUser


def checkAuth(request):
    if(request.user.is_authenticated):
        return True
    return False

def isAdmin(request):
    if(checkAuth(request=request)):
        profile=LoginUser.objects.get(user=request.user)
        if(profile and profile.role == 'admin'):
            return True
    return False

def isDoctor(request):
    if(checkAuth(request=request)):
        profile=LoginUser.objects.get(user=request.user)
        if(profile and profile.role == 'doctor'):
            return True
    return False


def isPatient(request):
    if(checkAuth(request=request)):
        profile=LoginUser.objects.get(user=request.user)
        if(profile and profile.role == 'patient'):
            return True
    return False
