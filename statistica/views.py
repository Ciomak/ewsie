# -*- coding: utf-8 -*-

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render_to_response
from django.template.context_processors import csrf
from django.views.generic import View

from .forms import LoginForm
from django.http import HttpResponse
from django.http.response import HttpResponseRedirect


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
                    return HttpResponse('Zostałeś zalogowany')
                    # here will be redirect to page with charts