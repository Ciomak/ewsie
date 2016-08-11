# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from .models import Kandydat, Kierunek, Stopien, Pytanie, Odpowiedz
import random
import datetime

PLEC = [u'Mężczyzna', u'Kobieta']

IMIE_M = [u'Kamil', u'Adam', u'Mateusz', u'Emil', u'Piotr', u'Marcin', u'Łukasz', u'Rafał', u'Arkadiusz', u'Sebastian', u'Daniel', u'Adrian', u'Paweł', u'Sławomir']
IMIE_K = [u'Anna', u'Joanna', u'Katarzyna', u'Irmina', u'Karolina', u'Kamila', u'Martyna', u'Beata', u'Justyna', u'Teresa', u'Dorota', u'Hanna', u'Agnieszka', u'Aneta', u'Marta']

NAZWISKO = [u'Ciomcia', u'Łazarczyk', u'Książyk', u'Przybysz', u'Filipiak', u'Kulesza', u'Pisarek', u'Michulec', u'Żok', u'Dzik', u'Kolano', u'Mrówka', u'Kaczmarzyk', u'Zając', u'Monik', u'Bielec',
            u'Stasiak', u'Łoś', u'Van Damme', u'Stallone', u'Shwarzeneger', u'Crowe', u'Russell', u'Wilk', u'Basior', u'Pawelec']

LOKALIZACJA = [u'Warszawa', u'Wrocław', u'Wołomin', u'Kobyłka', u'Pruszków', u'Ząbki', u'Zielonka', u'Piastów', u'Zagościniec']

WIEK = [18, 65]

MAIL = [u'@gmail.com', u'@interia.pl', u'@o2.pl', u'@wp.pl', u'@onet.pl']

KIERUNEK = Kierunek.objects.all()

BOOL = [True, False]

def import_data():

    for i in range(0,random.randint(1000, 5000)):
        a = Kandydat()
        a.data_rej = datetime.datetime.now() - datetime.timedelta(days=random.randint(0, 180))
        a.imie = random.choice(IMIE_M)
        a.nazwisko = random.choice(NAZWISKO)
        a.telefon = ''.join([str(random.randint(0,9)) for x in range(0,10)])
        a.mail = ''.join([a.imie.lower(), '.', a.nazwisko.lower(), random.choice(MAIL)])
        a.lokalizacja = random.choice(LOKALIZACJA)
        a.zgoda = random.choice(BOOL)
        a.stopien = Stopien.objects.get(id=1)
        a.kierunek = random.choice(KIERUNEK)
        a.save()

    for i in range(0, random.randint(1000, 5000)):
        a = Kandydat()
        a.data_rej = datetime.datetime.now() - datetime.timedelta(days=random.randint(1, 180))
        a.imie = random.choice(IMIE_K)
        a.nazwisko = random.choice(NAZWISKO)
        a.telefon = ''.join([str(random.randint(0,9)) for x in range(0,10)])
        a.mail = ''.join([a.imie.lower(), '.', a.nazwisko.lower(), random.choice(MAIL)])
        a.lokalizacja = random.choice(LOKALIZACJA)
        a.zgoda = random.choice(BOOL)
        a.stopien = Stopien.objects.get(id=1)
        a.kierunek = random.choice(KIERUNEK)
        a.save()

    for i in range(0, random.randint(1000, 5000)):
        a = Kandydat()
        a.data_rej = datetime.datetime.now() - datetime.timedelta(days=random.randint(1, 180))
        a.imie = random.choice(IMIE_M)
        a.nazwisko = random.choice(NAZWISKO)
        a.telefon = ''.join([str(random.randint(0,9)) for x in range(0,10)])
        a.mail = ''.join([a.imie.lower(), '.', a.nazwisko.lower(), random.choice(MAIL)])
        a.lokalizacja = random.choice(LOKALIZACJA)
        a.zgoda = random.choice(BOOL)
        a.stopien = Stopien.objects.get(id=2)
        a.kierunek = random.choice(KIERUNEK)
        a.save()

    for i in range(0, random.randint(1000, 5000)):
        a = Kandydat()
        a.data_rej = datetime.datetime.now() - datetime.timedelta(days=random.randint(1, 180))
        a.imie = random.choice(IMIE_K)
        a.nazwisko = random.choice(NAZWISKO)
        a.telefon = ''.join([str(random.randint(0,9)) for x in range(0,10)])
        a.mail = ''.join([a.imie.lower(), '.', a.nazwisko.lower(), random.choice(MAIL)])
        a.lokalizacja = random.choice(LOKALIZACJA)
        a.zgoda = random.choice(BOOL)
        a.stopien = Stopien.objects.get(id=2)
        a.kierunek = random.choice(KIERUNEK)
        a.save()



def import_survey():
    candidates = Kandydat.objects.all().filter(zgoda=1)
    pytania = Pytanie.objects.all()

    for candidate in candidates:
        for pytanie in pytania:
            a = Odpowiedz()

            if pytanie.alias == 'plec':
                if candidate.imie in IMIE_M:
                    a.odpowiedz == PLEC[0]
                elif candidate.imie in IMIE_K:
                    a.odpowiedz == PLEC[1]
            elif pytanie.alias == 'wiek':
                a.odpowiedz = random.randint(WIEK[0], WIEK[1])
            elif pytanie.alias == 'lok':
                a.odpowiedz = candidate.lokalizacja

            a.pytanie = pytanie

            a.save()

            a.kandydat.add(candidate)



def test():
    candidates = Kandydat.objects.all().filter(zgoda=1)
    pytania = Pytanie.objects.all()

    a = Odpowiedz()
    a.odpowiedz = u'Mężczyzna'
    a.pytanie = pytania[0]
    a.save()
    a.kandydat.add(candidates[1])