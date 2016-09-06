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