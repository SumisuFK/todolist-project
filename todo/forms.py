from django.forms import ModelForm, forms
from .models import Todo
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms


class TodoForm(ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'description', 'important']
        
class CreationForm(UserCreationForm):
    username = forms.CharField(label='login')
    email = forms.EmailField()
    password1 = forms.CharField(label='Password')
    password2 = forms.CharField(label='Confirm your password')
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')