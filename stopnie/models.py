#-*- coding: utf-8 -*-
import datetime

from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Stopien(models.Model):
	title = models.CharField(max_length=150, verbose_name="Tytul")
	content = models.TextField(verbose_name="Zawartosc")
	image = models.FileField(upload_to="images/", verbose_name="Obrazek")

	def __str__(self):
		return self.title

@python_2_unicode_compatible
class Rejestracja(models.Model):
	data_rej = models.DateTimeField(default=datetime.datetime.now())
	imie = models.CharField(max_length=150, verbose_name="Imie")
	nazwisko = models.CharField(max_length=150, verbose_name="Nazwisko")
	kierunek = models.CharField(max_length=250,verbose_name="Kierunek")
	telefon = models.CharField(max_length=20, verbose_name="Telefon")
	mail = models.EmailField(verbose_name="E-mail")
	lokalizacja = models.CharField(max_length=250,verbose_name="lokalizacja")
	pytanie = models.CharField(max_length=250,verbose_name="Skad o nas wiesz")
	rejestr = models.DateTimeField(verbose_name="Data rejestracji")
	stopien = models.ForeignKey(Stopien)
	

	def __str__(self):
		#return "%-15s   %-15s " % (self.imie, self.nazwisko)
		return '{0:15} {1:15}  |  E-mail: {2:20}  |  Tel.: {3:12}  |  {4:20}'.format(self.nazwisko, self.imie, self.mail, self.telefon, self.stopien)