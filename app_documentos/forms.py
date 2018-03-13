from django import forms
from .models import *
from froala_editor.widgets import FroalaEditor

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
	descricao = forms.CharField(max_length=500, widget=forms.Textarea(attrs={'class':'form-control'}))
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


class FormNoticias(forms.ModelForm):
	
	titulo = forms.CharField(max_length=300, widget=forms.TextInput(attrs={'class':'form-control'}))
	categoria_da_noticia = forms.ModelChoiceField(queryset=Categoria_noticia.objects.all(), widget=forms.Select(attrs={'class':'form-control'}))
	#data_publicacao = forms.DateField(widget=forms.TextInput(attrs={'type':'date','class':'form-control'}))
	destaque = forms.BooleanField()
	publicado = forms.BooleanField()
	tags_lista = forms.ModelMultipleChoiceField(queryset=Tag.objects.all(), widget=forms.SelectMultiple(attrs={'class':'form-control'}))
	imagem = forms.FileField()
  
	credito_midia_imagem = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class':'form-control'}))
	video = forms.FileField()
	credito_midia_video = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class':'form-control'}))
	legenda_do_video = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class':'form-control'}))
	legenda_do_imagem = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class':'form-control'}))
	# documentos_complementares = forms.FileField()
	chapeu = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class':'form-control'}))
	bigode = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class':'form-control'}))
	reporter = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class':'form-control'}))
	nota  = forms.CharField(widget=FroalaEditor)
	class Meta:
		model = Noticias
		fields = ('titulo', 'categoria_da_noticia','destaque','publicado',
			'imagem','video','documentos_complementares','chapeu',
			'bigode','reporter','tags_lista', 'nota',
			'credito_midia_imagem','legenda_do_video','legenda_do_imagem','credito_midia_video' )

class FormCategoria(forms.ModelForm):
	titulo = forms.CharField(max_length=300, widget=forms.TextInput(attrs={'class':'form-control'}))
	class Meta:
		model = Categoria_noticia
		fields = ('titulo',)

class FormTag(forms.ModelForm):
	tag_nome = forms.CharField(max_length=300, widget=forms.TextInput(attrs={'class':'form-control'}))
	class Meta:
		model = Tag
		fields = ('tag_nome',)
