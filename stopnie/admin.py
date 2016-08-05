from django.contrib import admin
from stopnie.models import Stopien, Kandydat, Kierunek, Odpowiedz, Pytanie,\
    Choices

admin.site.register(Stopien)
admin.site.register(Kandydat)
admin.site.register(Kierunek)
admin.site.register(Odpowiedz)
admin.site.register(Pytanie)
admin.site.register(Choices)