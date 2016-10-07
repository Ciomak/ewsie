# -*- coding: utf-8 -*-

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.db.models.aggregates import Count
from django.http import HttpResponse
from django.http.response import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template.context_processors import csrf
from django.views.generic import View
from pygal import Bar

from stopnie.models import Kandydat

from .forms import LoginForm


# Create your views here.
class LoginView(View):
    
    template_name = 'statistica/login.html'
    form = LoginForm()
    
    def get(self, request):
        
        args = {}
        args.update(csrf(request))
        args['form'] = self.form
        args['comment'] = None

        return render_to_response(self.template_name, args)

    def post(self, request):
        form = LoginForm(request.POST)
        
        if form.is_valid():
            ccd = form.cleaned_data
            try:
                User.objects.get(username=ccd['username'])
            except ObjectDoesNotExist:
                return render_to_response(self.template_name, {'form': LoginForm(), 'comment': 'Użytkownik o pdanym loginie nie istnieje'})
            else:
                user = authenticate(username=ccd['username'], password=ccd['password'])
                if user is None:
                    return render_to_response(self.template_name, {'form': LoginForm(), 'comment': 'Podane hasło jest niepoprawne'})
                else:
                    login(request, user)
                    return HttpResponseRedirect('/statistica/charts')
                    # here will be redirect to page with charts
                    
class ChartsView(View):
    template_name = 'statistica/charts.html'
    
    def get(self, request, *args, **kwargs):
        
        q = Kandydat.objects.values('zgoda').annotate(Count('zgoda'))
        
        chart = Bar()
        chart.x_labels = ('False', 'True')
        chart.add('', q[0]['zgoda__count'])
        chart.add('', q[1]['zgoda__count'])
        
        return render_to_response(self.template_name, {'chart': chart})
    
    def post(self, request, *args, **kwargs):
        return self.get(request, *args, **kwargs)