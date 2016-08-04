# -*- coding: utf-8 -*-

from django.forms import ModelForm
from django.forms.widgets import Select

from stopnie.models import Kandydat


class KandydatForm(ModelForm):
	class Meta:
		model = Kandydat
		fields = ['imie', 'nazwisko', 'kierunek', 'lokalizacja', 'mail', 'telefon', 'zgoda']
		
		labels = {
				'zgoda': 'Wyrażam zgodę na przeprowadzenie ankiety',
				'mail': 'E-mail',
				}
		
		widgets = {
				'kierunek': Select()
				}

# 	imie = forms.CharField(max_length=150, label='Imię')
# 	nazwisko = forms.CharField(max_length=150, label='Nazwisko')
# 	kierunek = forms.ChoiceField(choices=[(k.id, k.name) for k in Kierunek.objects.all()])
# 	lokalizacja = forms.CharField(max_length=150)
# 	mail = forms.EmailField(label='E-mail')
# 	telefon = forms.CharField(max_length=20, label='Telefon')
# 	zgoda = forms.BooleanField(label='Wyrażam zgodę na przeprowadzenie ankiety', required=False)
	
	
		
class AnkietaForm(ModelForm):
	pass