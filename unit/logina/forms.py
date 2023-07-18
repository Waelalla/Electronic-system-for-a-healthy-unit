from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *


    

class SignupForm(UserCreationForm):
    age = forms.IntegerField(required=False)
    NationalId = forms.CharField(max_length=200, required=False)
    address = forms.CharField(max_length=20, required=False)
    sons_cont = forms.IntegerField(required=False)
    man_cont = forms.IntegerField(required=False)
    girl_cont = forms.IntegerField(required=False)
    marital_status = forms.ChoiceField(choices=MARITAL_STATUS_CHOICES, required=False)
    image = forms.ImageField(required=False)
    phone = models.CharField(max_length=20, blank=True, null=True,)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'age', 'NationalId', 'address', 'sons_cont', 'man_cont', 'girl_cont', 'marital_status', 'image', )



class UserActivateForm(forms.Form):
    code = forms.CharField(max_length=8)

