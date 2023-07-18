from dataclasses import fields
from operator import contains
from pyexpat import model
from socket import fromshare
from turtle import title
from .models import accountForm as acf, department ,post,services
from django import forms

class formacc(forms.Form):
    class meta:
        model=acf 
        fields=['name','password']



class departmentle(forms.ModelForm):
    class Meta:
        enctype = 'multipart/form-data'
        model = department
        fields = [
            'dep_adress',
            'imag',
            'subjact',
            'dep_name',
            'dep_imag',
            'Thread_header',
            'the_topic',
            'the_topic_imag',
            'Thread_header2',
            'the_topic2',
            'the_topic_imag2',
            'Thread_header3',
            'the_topic3',
            'the_topic_imag3',
            'Thread_header4',
            'the_topic4',
            'the_topic_imag4',
            'Thread_header5',
            'the_topic5',
            'the_topic_imag5',

            ]
        widgets = {
            'dep_adress':forms.TextInput(attrs={'class':'form-control'}),
            'imag': forms.FileInput(attrs={'class':'form-control'}),
            'subjact':forms.TextInput(attrs={'class':'form-control'}),
            'dep_name':forms.TextInput(attrs={'class':'form-control'}),
            'dep_imag': forms.FileInput(attrs={'class':'form-control'}),
            'Thread_header':forms.TextInput(attrs={'class':'form-control'}),
            'the_topic':forms.TextInput(attrs={'class':'form-control'}),
            'the_topic_imag': forms.FileInput(attrs={'class':'form-control'}),
            'Thread_header2':forms.TextInput(attrs={'class':'form-control'}),
            
            
            'the_topic2':forms.TextInput(attrs={'class':'form-control'}),
            'the_topic_imag2': forms.FileInput(attrs={'class':'form-control'}),
            
            
            'Thread_header3':forms.TextInput(attrs={'class':'form-control'}),
            'the_topic3':forms.TextInput(attrs={'class':'form-control'}),
            'the_topic_imag3': forms.FileInput(attrs={'class':'form-control'}),
            'Thread_header4':forms.TextInput(attrs={'class':'form-control'}),
            'the_topic4':forms.TextInput(attrs={'class':'form-control'}),
            'the_topic_imag4': forms.FileInput(attrs={'class':'form-control'}),
            'Thread_header5':forms.TextInput(attrs={'class':'form-control'}),
            'the_topic5':forms.TextInput(attrs={'class':'form-control'}),
            'the_topic_imag5': forms.FileInput(attrs={'class':'form-control'}),
          
        }
        
        
        
class poste(forms.ModelForm):
    class Meta:
        enctype = 'multipart/form-data'        
        model = post
        fields=[
                'name_post',
                'content_post',
                'photo_post',
                'author_post',
                'date_post',
                ]      
        widgets = {
            'name_post':forms.TextInput(attrs={'class':'form-control'}),
            'content_post':forms.TextInput(attrs={'class':'form-control'}),
            'photo_post': forms.FileInput(attrs={'class':'form-control'}),
            'author_post':forms.TextInput(attrs={'class':'form-control'}),
            'date_post': forms.DateInput(attrs={'class': 'form-control'}),           
        }
        
        
        
        
class servicese(forms.ModelForm):
    class Meta:
        enctype = 'multipart/form-data'
        model = services
        fields = [
            'name_Services',
            'dep_name',
            'dep_imag',
            'Thread_header',
            'the_topic',
            'the_topic_imag',
            'Thread_header2',
            'the_topic2',
            'the_topic_imag2',
            'Thread_header3',
            'the_topic3',
            'the_topic_imag3',
            'Thread_header4',
            'the_topic4',
            'the_topic_imag4',
            'Thread_header5',
            'the_topic5',
            'the_topic_imag5',

            ]
        widgets = {
            'name_Services':forms.TextInput(attrs={'class':'form-control'}),
            'dep_name':forms.TextInput(attrs={'class':'form-control'}),
            'dep_imag': forms.FileInput(attrs={'class':'form-control'}),
            'Thread_header':forms.TextInput(attrs={'class':'form-control'}),
            'the_topic':forms.TextInput(attrs={'class':'form-control'}),
            'the_topic_imag': forms.FileInput(attrs={'class':'form-control'}),
            'Thread_header2':forms.TextInput(attrs={'class':'form-control'}),
            
            
            'the_topic2':forms.TextInput(attrs={'class':'form-control'}),
            'the_topic_imag2': forms.FileInput(attrs={'class':'form-control'}),
            
            
            'Thread_header3':forms.TextInput(attrs={'class':'form-control'}),
            'the_topic3':forms.TextInput(attrs={'class':'form-control'}),
            'the_topic_imag3': forms.FileInput(attrs={'class':'form-control'}),
            'Thread_header4':forms.TextInput(attrs={'class':'form-control'}),
            'the_topic4':forms.TextInput(attrs={'class':'form-control'}),
            'the_topic_imag4': forms.FileInput(attrs={'class':'form-control'}),
            'Thread_header5':forms.TextInput(attrs={'class':'form-control'}),
            'the_topic5':forms.TextInput(attrs={'class':'form-control'}),
            'the_topic_imag5': forms.FileInput(attrs={'class':'form-control'}),
          
        }
        