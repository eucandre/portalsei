from django import forms

from .models import *

class Formtutorial(forms.ModelForm):
	titulo = forms.CharField(max_length = 150, widget=forms.TextInput(attrs={'class':'form-control'}))
	video = forms.FileField(required= False, widget=forms.ClearableFileInput(attrs={'multiple': True}))
	documento = forms.FileField(required= False, widget=forms.ClearableFileInput(attrs={'multiple': True}))
	conteudo = forms.CharField(max_length=100000, widget = forms.Textarea(attrs={'class':'form-control'}))
	class Meta:
		model = Tutorial
		fields = ('titulo','video','documento','conteudo')