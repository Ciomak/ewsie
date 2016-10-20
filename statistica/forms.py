# -*- coding: utf-8 -*-

from django.forms import ModelForm
from django.contrib.auth.models import User
from django.forms.widgets import TextInput, PasswordInput, RadioSelect
from django.forms.forms import Form
from django.forms.fields import ChoiceField, IntegerField
from stopnie.models import Stopien, Kierunek

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
        
class GenderAgeForm(Form):
    stopien_id = ChoiceField(widget=RadioSelect())
    kierunek_id = ChoiceField(widget=RadioSelect())
    
    def __init__(self,*args, **kwargs):
        super(GenderAgeForm, self).__init__(*args, **kwargs)
        
        self.fields['stopien_id'].choices = [(st.id, st.title) for st in Stopien.objects.all().order_by('id')]
        self.fields['stopien_id'].choices.append((0, 'Total'))
        self.fields['kierunek_id'].choices = [(ki.id, ki.name) for ki in Kierunek.objects.all().order_by('id')]
        self.fields['kierunek_id'].choices.append((0,'Total'))
        
        self.fields['stopien_id'].label = 'Stopień'
        self.fields['kierunek_id'].label = 'Kierunek'
        
class RegistrationTimeForm(Form):
    choices_data = ((360, '360 dni'),
                    (180, '180 dni'),
                    (90, '90 dni'),
                    (30, '30 dni'),
                    (7, '7 dni'),
                    (0, 'Total')
                    )
    
    choices_group = (
                     ('D', 'Dzień'),
                     ('W', 'Tydzień'),
                     ('M', 'Miesiąc'),
                     ('Q', 'Kwartał'),
                     ('Y', 'Rok')
                    )
    
    data_rej = ChoiceField(choices=choices_data, label='Okres', initial=0)
    grupowanie = ChoiceField(choices=choices_group, label='Grupowanie okresów')
    kierunek_id = ChoiceField(label='Kierunek')
    
    def __init__(self, *args, **kwargs):
        super(RegistrationTimeForm, self).__init__(*args, **kwargs)
        
        self.fields['kierunek_id'].choices = [(ki.id, ki.name) for ki in Kierunek.objects.all().order_by('id')]
        self.fields['kierunek_id'].choices.append((0, 'Wszystkie kierunki'))
        self.fields['kierunek_id'].initial = 0