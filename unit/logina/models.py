from django.db import models
from django.db.models import DateTimeField, ExpressionWrapper,F
# Create your models here.
from django import forms
from django.contrib.auth.models import  User
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth import authenticate, login,logout
from utils.genrate_code import genrate_code


# تعريف الخيارات لحالة الزواج
MARITAL_STATUS_CHOICES = (
    ('1', 'أعزب'),
    ('2', 'متزوج'),
    ('3', 'مطلق'),
    ('4', 'أرمل')
) 
    # تعريف الكلاس LoginUser
class LoginUser(models.Model):
    user=models.OneToOneField(User,related_name='userprofile',on_delete=models.CASCADE)    
    age = models.IntegerField(blank=True, null=True)
    role=models.CharField(choices=[('admin','الادمن'),('doctor','دكتور'),('patient','مريض')], max_length=20, blank=True, null=True,default='patient')
    phone = models.CharField(max_length=20, blank=True, null=True)

    email = models.EmailField(max_length=254, blank=True, null=True)

    NationalId = models.CharField(max_length=200)
    
    address = models.CharField(max_length=20, blank=True, null=True)
    
    sons_cont = models.IntegerField(null=True, blank=True,)
    
    man_cont = models.IntegerField(null=True, blank=True,)
    
    girl_cont = models.IntegerField(null=True, blank=True,)
    
    marital_status = models.CharField(choices=MARITAL_STATUS_CHOICES, max_length=20, blank=True, null=True)
    
    image = models.ImageField(upload_to='photos', blank=True, null=True, default='photos/default.png')
 
    code = models.CharField(max_length=10,default=genrate_code)
    code_used = models.BooleanField(default=False)
    active = models.BooleanField(default=False)
    def __str__(self):
        return self.user.username
    
@receiver(post_save,sender=User)
def create_profile(sender,instance,created,**kwargs):
    if created:
        LoginUser.objects.create(user=instance)
    
    
    
    
    
class Child(models.Model):
    parent=models.ForeignKey(User,verbose_name=('user'), related_name='child',on_delete=models.SET_NULL,null=True,blank=True)
    name = models.CharField(max_length=20)
    age= models.IntegerField()
    national_id = models.CharField(max_length=14)
    gender = models.CharField(choices=[('male','ذكر'),('female','انثى')],max_length=20,blank=True,null=True)


pressure_level =(
        ('natural', 'طبيعي'),
        ('low', 'منخفض'),
        ('high', 'مرتفع'),
)

sugar_level =(
        ('natural', 'طبيعي'),
        ('low', 'منخفض'),
        ('high', 'مرتفع'),
)

blood_type =(
        ('o+', 'o+'),
        ('a+', 'a+'),
        ('b+', 'b+'),
        ('ab+', 'ab+'),
        ('o-', 'o-'),
        ('a-', 'a-'),
        ('b-', 'b-'),
        ('ab-', 'ab-'),
)



class chronic_diseases(models.Model):
    pressure_level=models.CharField(choices=pressure_level, max_length=20, blank=True, null=True)
    sugar_level=models.CharField(choices=sugar_level, max_length=20, blank=True, null=True)
    blood_type=models.CharField(choices=blood_type, max_length=20, blank=True, null=True)
    Genetic_diseases=models.CharField(max_length=20, blank=True, null=True)
    chronic_diseases=models.CharField(max_length=20, blank=True, null=True)
    Drugs=models.CharField(max_length=20, blank=True, null=True)
    
    
    
    
    
    
    
class Vaccinations(models.Model):
    vaccination_type = models.CharField(max_length=20, blank=True, null=True)
    doctors_note = models.CharField(max_length=20, blank=True, null=True)
    pharmaceutical = models.CharField(max_length=20, blank=True, null=True)
    the_date = models.DateField(blank=True, null=True)
    
    
class esoteric(models.Model):
    vaccination_type=models.CharField(max_length=20, blank=True, null=True)
    Doctors_note =models.CharField(max_length=20, blank=True, null=True)
    pharmaceutical=models.CharField(max_length=20, blank=True, null=True)
    the_date=models.CharField(max_length=20, blank=True, null=True)
    
class conjunctivitis(models.Model):
    vaccination_type=models.CharField(max_length=20, blank=True, null=True)
    Doctors_note =models.CharField(max_length=20, blank=True, null=True)
    pharmaceutical=models.CharField(max_length=20, blank=True, null=True)
    the_date=models.CharField(max_length=20, blank=True, null=True)
    
class rays(models.Model):
    vaccination_type=models.CharField(max_length=20, blank=True, null=True)
    Doctors_note =models.CharField(max_length=20, blank=True, null=True)
    pharmaceutical=models.CharField(max_length=20, blank=True, null=True)
    the_date=models.CharField(max_length=20, blank=True, null=True)
    
class analyzes(models.Model):
    vaccination_type=models.CharField(max_length=20, blank=True, null=True)
    Doctors_note =models.CharField(max_length=20, blank=True, null=True)
    pharmaceutical=models.CharField(max_length=20, blank=True, null=True)
    the_date=models.CharField(max_length=20, blank=True, null=True)
    
class teeth(models.Model):
    vaccination_type=models.CharField(max_length=20, blank=True, null=True)
    Doctors_note =models.CharField(max_length=20, blank=True, null=True)
    pharmaceutical=models.CharField(max_length=20, blank=True, null=True)
    the_date=models.CharField(max_length=20, blank=True, null=True)
    
