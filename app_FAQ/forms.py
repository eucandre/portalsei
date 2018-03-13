from django import forms

from .models import *

class FormDuvidas(forms.ModelForm):
	titulo = forms.CharField(max_length = 150, widget=forms.TextInput(attrs={'class':'form-control'}))
	tags = forms.	ModelMultipleChoiceField(queryset=Tag.objects.all(), widget= forms.SelectMultiple(attrs={'class':'form-control'}) )
	resposta = forms.CharField(max_length=100000, widget = forms.Textarea(attrs={'class':'form-control'}))
	class Meta:
		model = Duvidas
		fields = ('titulo', 'tags', 'resposta')