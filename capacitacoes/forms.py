# coding=utf-8
from django import forms

from .models import *

from froala_editor.widgets import FroalaEditor

class FormEventos(forms.ModelForm):
	titulo = forms.CharField(label= 'Título',max_length = 150, widget=forms.TextInput(attrs={'class':'form-control'}))
	data_realizacao = forms.DateField(label= 'Data para a realização',widget=forms.TextInput(attrs={'type':'Date', 'class':'form-control'}))
	hora_realizacao = forms.TimeField(label= 'Hora para a realização',widget=forms.TextInput(attrs={'type':'Time', 'class':'form-control'}))
	video_promocional = forms.FileField(label= 'Vídeo',)
	Notas  = forms.CharField(label= 'Outro Conteúdo',widget=FroalaEditor)
	class Meta:
		model = Evento
		fields = ('titulo','data_realizacao','hora_realizacao','video_promocional','Notas')