from django.forms import ModelForm, forms
from .models import Todo
from django.contrib.auth.forms import AuthenticationForm

class TodoForm(ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'description', 'important']
