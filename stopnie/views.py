from django.http import HttpResponseRedirect
from django.http.response import HttpResponse
from django.shortcuts import render_to_response, render
from django.template import loader
from django.template.context_processors import csrf
from django.utils import timezone
from django.views.generic import View

from forms import KandydatForm, AnkietaForm
from stopnie.models import Stopien, Kandydat, Pytanie, Odpowiedz


class Stopnie(View):

    template = 'stopnie/stopnie.html'
    qs = Stopien.objects.all()

    def post(self, request, *args, **kwargs):
        context = {'stopnie': self.qs}
        return render_to_response(self.template, context)

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


class Stopien_(View):
    template = 'stopnie/stopien.html'

    def get(self, request, stopien_id, *args, **kwargs):
        return self.post(request, stopien_id, *args, **kwargs)

    def post(self, request, stopien_id, *args, **kwargs):
        context = {'stopien': self.get_qs(stopien_id)}
        return render_to_response(self.template, context)

    def get_qs(self, id):
        return Stopien.objects.get(id=id)


class Rejestracja(View):

    template_name = 'stopnie/add_rejestracja.html'

    def get(self, request, stopien_id, *args, **kwargs):
        form = KandydatForm()

        args={}
        args.update(csrf(request))
        args['stopien'] = self.get_qs(stopien_id)
        args['form'] = form

        return render_to_response(self.template_name, args)

    def post(self,request, stopien_id, *args, **kwargs):
        form = KandydatForm(request.POST)
        if form.is_valid():
            kandydat = form.save(commit=False)
            kandydat.data_rej = timezone.now()
            kandydat.stopien = self.get_qs(stopien_id)
            kandydat.save()

            if kandydat.zgoda:
                return HttpResponseRedirect('/stopnie/{0}/ankieta'.format(kandydat.id))
            else:
                return HttpResponseRedirect('/stopnie')  # przekierowanie do strony glownej

    def get_qs(self, id):
        return Stopien.objects.get(id=id)


class Ankieta(View):

    template_name = 'stopnie/ankieta.html'

    def get(self, request, kandydat_id, *args, **kwargs):

        fields = Pytanie.objects.all()

        args = {}
        args.update(csrf(request))
        args['fields'] = fields
        args['kandydat'] = self.get_qs(kandydat_id)

        return render_to_response(self.template_name, {'fields': fields})

    def post(self, request, kandydat_id, *args, **kwargs):
        pytania = Pytanie.objects.all()

        for pytanie in pytania:
            a = Odpowiedz()
            a.odpowiedz = request.POST[pytanie.alias]
            a.pytanie = pytanie
            a.save()
            a.kandydat.add(Kandydat.objects.get(id=kandydat_id))

        return HttpResponse('Thank you')

    def get_qs(self, id):
        return Kandydat.objects.get(id=id)

def add_ankieta(request, kandydat_id):
    kandydat = Kandydat.objects.get(id=kandydat_id)
    pytania = Pytanie.objects.all()

    if request.method == 'POST':
        pass

    args = {}
    args.update(csrf(request))
    args['pytania'] = pytania
    args['kandydat'] = kandydat

    return render_to_response('stopnie/ankieta.html', args)
