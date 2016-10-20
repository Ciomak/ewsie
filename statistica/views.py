# -*- coding: utf-8 -*-

import datetime
import functools

from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.http.response import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template.context_processors import csrf
from django.views.generic import View
from pygal import Bar

import pandas as pd
from statistica.forms import RegistrationTimeForm
from statistica.models import Variables
from stopnie.models import Kandydat, Stopien, Kierunek

from .forms import LoginForm
import pygal


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
                    
class GenderAgeView(View):
    template_name = 'statistica/charts.html'
    variables = Variables.objects.all()
    
    def get(self, request, *args, **kwargs):
        args = {}
        args.update(csrf(request))
        args['form'] = RegistrationTimeForm()
        args['variables'] = self.variables
        
        return render_to_response(self.template_name, context=args)
    
    def post(self, request, *args, **kwargs):
        args = {}
        args.update(csrf(request))
        args['variables'] = self.variables
        args['form'] = RegistrationTimeForm(request.POST)
        if args['form'].is_valid():
            ccd = args['form'].cleaned_data
            
            args['data'] = ccd
            print(ccd)
            
            df = self.filterDataFrame(self.createDataFrame(), **ccd)
             
            grouped = df.groupby([df.title, pd.Grouper(key='data_rej', freq=ccd['grupowanie']), df.name])
             
            chart = pygal.Line()
            chart.add('', grouped.zgoda.count())
             
            args['chart'] = chart
        
        return render_to_response(self.template_name, context=args)
    
    def createDataFrame(self):
        kandydat = pd.DataFrame.from_records(Kandydat.objects.all().values())
        stopien = pd.DataFrame.from_records(Stopien.objects.all().values())
        kierunek = pd.DataFrame.from_records(Kierunek.objects.all().values())
        
        df = kandydat.merge(stopien, left_on='stopien_id', right_on='id').merge(kierunek, left_on='kierunek_id', right_on='id')
        
        return df
    
    def filterDataFrame(self, df, **kwargs):
        criterias = []
        for key, value in kwargs.iteritems():
            if key == 'kierunek_id':
                if value != 0:
                    criterias.append(df[key]==int(value))
            elif key == 'data_rej':
                if value != 0:
                    criterias.append(df[key] >= (datetime.datetime.now()-datetime.timedelta(days=int(value))))
                  
        if not criterias:
            return df
        
        allCrit = functools.reduce(lambda x,y: x & y, criterias)
        
        return df[allCrit]