# coding=utf-8
from django import forms
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username = forms.CharField(label = 'Nome do usuário',widget=forms.TextInput(attrs={"class":"form-control"}))
    password = forms.CharField(label = 'Senha',widget=forms.PasswordInput(attrs={"class":"form-control"}))