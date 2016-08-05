from django.http import HttpResponseRedirect
from django.http.response import HttpResponse
from django.shortcuts import render_to_response
from django.template import loader
from django.template.context_processors import csrf
from django.utils import timezone

from forms import KandydatForm, AnkietaForm
from stopnie.models import Stopien, Kandydat, Pytanie, Choices


def stopnie(request):
	stopnie = Stopien.objects.all()
	template = loader.get_template('stopnie/stopnie.html')
	context = {
			'stopnie': stopnie
			}
	
	return HttpResponse(template.render(context, request))

def stopien(request, stopien_id):
	stopien = Stopien.objects.get(id=stopien_id)
	template = loader.get_template('stopnie/stopien.html')
	context = {
			'stopien': stopien
			}
	
	return HttpResponse(template.render(context, request))

def add_rejestracja(request, stopien_id):
	
	r = Stopien.objects.get(id=stopien_id)

	if request.method == "POST":
		form = KandydatForm(request.POST)
		if form.is_valid():
			kandydat = form.save(commit=False)
			kandydat.data_rej = timezone.now()
			kandydat.stopien = r
			kandydat.save()
			
			if kandydat.zgoda:
				return HttpResponseRedirect('/stopnie/{0}/ankieta'.format(kandydat.id))
			else:
				return HttpResponseRedirect('/stopnie') #przekierowanie do strony glownej

	else:
		form = KandydatForm()

	args = {}
	args.update(csrf(request))
	args['stopien'] = r # Stopien studiow 
	args['form'] = form  # formularz

	return render_to_response('stopnie/add_rejestracja.html', args)

def add_ankieta(request, kandydat_id):
	kandydat = Kandydat.objects.get(id=kandydat_id)
	values = Choices.objects.all()
	
	if request.method == 'POST':
		pass
	
	args = {}
	args.update(csrf(request))
# 	args['fields'] = fields
	args['values'] = values
	args['kandydat'] = kandydat
	
	return render_to_response('stopnie/ankieta.html', args)