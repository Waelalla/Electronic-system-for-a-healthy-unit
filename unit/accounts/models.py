from django.db import models
from django.contrib.auth.models import  User
from utils.genrate_code import genrate_code

# Create your models here.
class   Profile(models.Model):
    user = models.OneToOneField(User,related_name='user_profile' , on_delete=models.CASCADE)
    image = models.ImageField(upload_to='users')
    
    
    code = models.CharField(max_length=10,default=genrate_code)
    code_used = models.BooleanField(default=False)
    active = models.BooleanField(default=False)
    
    