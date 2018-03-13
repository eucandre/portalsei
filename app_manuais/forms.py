from django import forms 

from .models import *

class FormManual(forms.ModelForm):
	titulo = forms.CharField(max_length = 150, widget=forms.TextInput(attrs = {'class':'form-control'}))
	class Meta:
		model = Manual
		fields = ('titulo','arquivo')