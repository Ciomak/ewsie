# -*- coding: utf-8 -*-

from django import forms

from models import Rejestracja


class RejestracjaForm(forms.Form):
	imie = forms.CharField(max_length=150, label='Imi�')
	nazwisko = forms.CharField(max_length=150, label='Nazwisko')
		
class AnkietaForm(forms.ModelForm):
	pass