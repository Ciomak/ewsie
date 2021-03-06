# -*- coding: utf-8 -*-
from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Stopien(models.Model):
    title = models.CharField(max_length=150, verbose_name="Tytul")
    image = models.FileField(upload_to="images/", verbose_name="Obrazek")

    def __str__(self):
        return self.title


@python_2_unicode_compatible
class Kierunek(models.Model):
    alias = models.CharField(max_length=100)
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Kandydat(models.Model):
    data_rej = models.DateTimeField()
    imie = models.CharField(max_length=150)
    nazwisko = models.CharField(max_length=150)
    telefon = models.CharField(max_length=20)
    mail = models.EmailField()
    lokalizacja = models.CharField(max_length=250)
    zgoda = models.BooleanField(default=False)
    stopien = models.ForeignKey(Stopien)
    kierunek = models.ForeignKey(Kierunek)

    def __str__(self):
        # return "%-15s   %-15s " % (self.imie, self.nazwisko)
        return '{0:15} {1:15}  |  E-mail: {2:20}  |  Tel.: {3:12}  |  {4:20}'.format(self.nazwisko, self.imie,
                                                                                     self.mail, self.telefon,
                                                                                     self.stopien)


@python_2_unicode_compatible
class Pytanie(models.Model):
    alias = models.CharField(max_length=50)
    name = models.TextField()
    widget = models.CharField(max_length=50)

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Odpowiedz(models.Model):
    kandydat = models.ManyToManyField(Kandydat)
    pytanie = models.ForeignKey(Pytanie)
    odpowiedz = models.TextField()

    def __str__(self):
        return self.odpowiedz


@python_2_unicode_compatible
class Choices(models.Model):
    choice = models.CharField(max_length=150)
    pytanie = models.ForeignKey(Pytanie)

    def __str__(self):
        return self.choice
