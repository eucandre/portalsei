# coding=utf-8
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .forms import LoginForm

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'],
                   password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Autenticado','sucesso!')
                else:
                    return HttpResponse('conta desabilitada')
            else:
                return HttpResponse('Login inválido, tente novamente')
    else:
        form = LoginForm()
    return render(request, 'app_usuario/login.html', {'form': form})