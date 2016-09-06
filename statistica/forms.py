# -*- coding: utf-8 -*-

from django.forms import ModelForm
from django.contrib.auth.models import User
from django.forms.widgets import TextInput, PasswordInput

class LoginForm(ModelForm):
    class Meta:
        model = User
        
        fields = [
                  'username', 
                  'password',
                  ]
        
        widgets = {
                   'username': TextInput(), 
                   'password': PasswordInput(),
                   }
        
        labels = {'username': 'Użytkownik',
                  'password': 'Hasło',
                  }