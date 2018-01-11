from django import forms
from .models import *

PRIORIDADE = ((u'ALTA', 'ALTA'),(u'MEDIA','MEDIA'),(u'BAIXA','BAIXA'))

TIPO_DOCUMENTO = ((u'MANUAL', 'MANUAL'), (u'PLANO_DE_COMUNICACAO', ('PLANO_DE_COMUNICACAO')),(u'DOCUMENTO_DE_APOIO','DOCUMENTO_DE_APOIO'))


class FormTipoDocumento(forms.ModelForm):
	nome = forms.ChoiceField(choices=TIPO_DOCUMENTO, widget=forms.Select(attrs={'class':'form-control'}))
	class Meta:
		model = Tipo_Documento
		fields = ('nome',)

class FormSetor(forms.ModelForm):
	nome = forms.CharField(max_length = 150, widget=forms.TextInput(attrs={'class':'form-control'}))
	class Meta:
		model = Setor
		fields = ('nome',)

class FormCliente(forms.ModelForm):
	nome = forms.CharField(max_length = 150, widget=forms.TextInput(attrs={'class':'form-control'}))
	matricula = forms.CharField(max_length=11, widget=forms.TextInput(attrs={'class':'form-control'}))
	cpf = forms.CharField(max_length=11, widget=forms.TextInput(attrs={'class':'form-control'}))
	cargo = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class':'form-control'}))
	setor_locacao = forms.ModelChoiceField(queryset=Setor.objects.all(), widget=forms.Select(attrs={'class':'form-control'}))
	class Meta:
		model = Cliente
		fields = ('nome', 'matricula','cpf', 'cargo','setor_locacao')

class FormDocumentos(forms.ModelForm):
	titulo = forms.CharField(max_length=300, widget=forms.TextInput(attrs={'class':'form-control'}))
	tipo = forms.ModelChoiceField(queryset=Tipo_Documento.objects.all(), widget=forms.Select(attrs={'class':'form-control'}))
	repositorio_documento = forms.FileField()
	descricao = forms.CharField(max_length=500, widget=forms.TextInput(attrs={'class':'form-control'}))
	class Meta:
		model = Documentos
		fields = ('titulo','tipo','repositorio_documento','descricao')

class FormHelpDesk(forms.ModelForm):
	titulo = forms.CharField(max_length=300, widget=forms.TextInput(attrs={'class':'form-control'}))
	setor_requisicao = forms.ModelChoiceField(queryset=Setor.objects.all(), widget=forms.Select(attrs={'class':'form-control'}))
	requisitor = forms.ModelChoiceField(queryset=Cliente.objects.all(), widget=forms.Select(attrs={'class':'form-control'}))
	data_requisicao = forms.DateField(widget=forms.TextInput(attrs={'type':'date','class':'form-control'}))
	hora_requisicao = forms.TimeField(widget=forms.TextInput(attrs={'type':'time','class':'form-control'}))
	prioridade_da_acao = forms.ChoiceField(choices = PRIORIDADE,  widget=forms.Select(attrs={'class':'form-control'}))
	class Meta:
		model = Help_Desk
		fields = ('titulo','setor_requisicao','requisitor','data_requisicao','hora_requisicao','prioridade_da_acao')



