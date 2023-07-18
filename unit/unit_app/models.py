from django.db import models
from django.db.models import DateTimeField, ExpressionWrapper,F
# Create your models here.
from django import forms


class sections(models.Model):
    name_sections = models.CharField(max_length=50)
    photo_sections = models.ImageField(upload_to='photos',null=True,blank=True)
    content = models.TextField()
    def __str__(self):
        return self.name_sections
    

 

class initiatives(models.Model):
    name_Services = models.CharField(max_length=50)
    def __str__(self):
        return self.name_Services 
    
marital_statusc=[
        ('اعزب','اعزب'),
        ('متزوج','متزوج'),
        ('مطلق','مطلق'),
        ('ارمل','ارمل'),

    ]
class login_user(models.Model):
    user_name = models.CharField(max_length=20,blank=True,null=True)
    age = models.IntegerField(blank=True,null=True)
    id_user = models.IntegerField(blank=True,null=True)
    address = models.CharField(max_length=20,blank=True,null=True)
    sons_cont =  models.IntegerField(null=True,blank=True)
    man_cont =  models.IntegerField(null=True,blank=True)
    girl_cont =  models.IntegerField(null=True,blank=True)
    marital_status = models.CharField(choices=marital_statusc,max_length=20,blank=True,null=True)
    def __str__(self):
        return self.user_name 

class login_admin(models.Model):
    user_name = models.CharField(max_length=20,)
    password = models.CharField(max_length=20,)
    def __str__(self):
        return self. user_name
    
class post(models.Model):
    name_post = models.CharField(max_length=50)
    content_post =  models.TextField()
    photo_post = models.ImageField(upload_to='photos',null=True,blank=True)
    author_post = models.CharField(max_length=50)
    date_post=models.DateField(null=True)
    def __str__(self):
        return self.name_post
    
class department(models.Model):
    dep_adress =models.CharField(max_length=50)
    imag =models.ImageField(upload_to='photos',null=True,blank=True)
    subjact = models.TextField(blank=True,null=True)
    #-----الديتيلز-----#
    dep_name=models.CharField(max_length=50)
    dep_imag=models.ImageField(upload_to='photos',null=True,blank=True)
    Thread_header=models.TextField(blank=True,null=True)
    the_topic=models.TextField(blank=True,null=True)
    the_topic_imag=models.ImageField(upload_to='photos',null=True,blank=True)
    #---الجزءالثاني
    Thread_header2=models.TextField(blank=True,null=True)
    the_topic2=models.TextField(blank=True,null=True)
    the_topic_imag2=models.ImageField(upload_to='photos',null=True,blank=True)
     #---الجزء الثالث
    Thread_header3=models.TextField(blank=True,null=True)
    the_topic3=models.TextField(blank=True,null=True)
    the_topic_imag3=models.ImageField(upload_to='photos',null=True,blank=True)
     #---الجزء الرابع
    Thread_header4=models.TextField(blank=True,null=True)
    the_topic4=models.TextField(blank=True,null=True)
    the_topic_imag4=models.ImageField(upload_to='photos',null=True,blank=True)
    #---الجزء الخامس
    Thread_header5=models.TextField(blank=True,null=True)
    the_topic5=models.TextField(blank=True,null=True)
    the_topic_imag5=models.ImageField(upload_to='photos',null=True,blank=True)
    
    
    
    
    
    
    
    
class accountForm(models.Model):
    names = forms.CharField(max_length=100)
    password= forms.CharField(widget=forms.PasswordInput) 
    message = forms.CharField(widget=forms.Textarea)

    
    
    
    
    
    
    
    
    
    
    
class services(models.Model):
    name_Services = models.CharField(max_length=50)
    #-----الديتيلز-----#
    dep_name=models.CharField(max_length=50)
    dep_imag=models.ImageField(upload_to='department',null=True,blank=True)
    Thread_header=models.TextField(blank=True,null=True)
    the_topic=models.TextField(blank=True,null=True)
    the_topic_imag=models.ImageField(upload_to='department',null=True,blank=True)
    #---الجزءالثاني
    Thread_header2=models.TextField(blank=True,null=True)
    the_topic2=models.TextField(blank=True,null=True)
    the_topic_imag2=models.ImageField(upload_to='department',null=True,blank=True)
     #---الجزء الثالث
    Thread_header3=models.TextField(blank=True,null=True)
    the_topic3=models.TextField(blank=True,null=True)
    the_topic_imag3=models.ImageField(upload_to='department',null=True,blank=True)
     #---الجزء الرابع
    Thread_header4=models.TextField(blank=True,null=True)
    the_topic4=models.TextField(blank=True,null=True)
    the_topic_imag4=models.ImageField(upload_to='department',null=True,blank=True)
    #---الجزء الخامس
    Thread_header5=models.TextField(blank=True,null=True)
    the_topic5=models.TextField(blank=True,null=True)
    the_topic_imag5=models.ImageField(upload_to='department',null=True,blank=True)
    def __str__(self):
        return self.name_Services 
    
   

