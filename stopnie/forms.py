# -*- coding: utf-8 -*-

from django import forms

from models import Kierunek


class RejestracjaForm(forms.Form):
	imie = forms.CharField(max_length=150, label='Imię')
	nazwisko = forms.CharField(max_length=150, label='Nazwisko')
	kierunek = forms.ChoiceField(Kierunek.objects.all().name)
	lokalizacja = forms.CharField(max_length=150)
	mail = forms.EmailField(label='E-mail')
	telefon = forms.CharField(max_length=20, label='Telefon')
	zgoda = forms.BooleanField(label='Wyrażam zgodę na przeprowadzenie ankiety')
	
	
		
class AnkietaForm(forms.ModelForm):
	pass