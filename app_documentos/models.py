# coding=utf-8

from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import *

PRIORIDADE = ((u'ALTA', 'ALTA'),(u'MEDIA','MEDIA'),(u'BAIXA','BAIXA'))

TIPO_DOCUMENTO = ((u'MANUAL', 'MANUAL'), (u'PLANO_DE_COMUNICACAO', ('PLANO_DE_COMUNICACAO')),(u'DOCUMENTO_DE_APOIO','DOCUMENTO_DE_APOIO'))


class Tipo_Documento(models.Model):
	nome = models.CharField(choices= TIPO_DOCUMENTO, max_length=150)
	user = models.ForeignKey(User)

	def __unicode__(self):
		return self.nome.__str__()

	class Meta:
		verbose_name_plural = "Tipo de Documento"

class Setor(models.Model):
	"""
		Classe para definição do setor na Secretaria ou no órgão.
	"""
	nome = models.CharField(max_length = 150)
	user = models.ForeignKey(User)

	class Meta:
		verbose_name_plural = "Setor da Secretaria ou de Órgão."

	def __unicode__(self):
		return self.nome

class Cliente(models.Model):
	"""
		Cliente para a seleção de ajuda, selecionando seu setor e identificando-se com
		matricula e cargo, como obrigação de preenchimento.
	"""
	nome = models.CharField(max_length=150)
	matricula = models.CharField(max_length = 11)
	cpf = models.CharField(max_length = 11)
	cargo = models.CharField(max_length=150)
	setor_locacao = models.ForeignKey(Setor)
	user = models.ForeignKey(User)

	def __unicode__(self):
		return self.nome

	class Meta:
		verbose_name_plural =  "Clientes para Solicitação de help Desk"

class Documentos(models.Model):
	"""
	Registro dos documentos que estarão distoníveis no portal.
	repositorio_documento o campo Salvara o documento na pasta documentos o ano
	 o mes o dia
	"""
	titulo = models.CharField(max_length = 300)
	tipo = models.ForeignKey(Tipo_Documento)
	repositorio_documento =  models.FileField(upload_to="documentos/%Y/%m/%d/")
	descricao = models.TextField()
	user = models.ForeignKey(User)

	class Meta:
		verbose_name_plural = "Documentos, help desk e materiais de apoio"

	def __unicode__(self):
		return self.titulo.__str__()

class Help_Desk(models.Model):
	"""
	Registra as reguisições dos clientes para determinadas demandas.
	"""
	titulo = models.CharField(max_length = 300)
	setor_requisicao = models.ForeignKey(Setor)
	requisitor = models.ForeignKey(Cliente)
	data_requisicao = models.DateField(help_text="Data da solicitação de ajuda")
	hora_requisicao = models.TimeField(help_text="Hora da solicitação de ajuda")
	prioridade_da_acao = models.CharField(max_length=5, choices=PRIORIDADE)
	user = models.ForeignKey(User)

	def __unicode__(self):
		return self.titulo.__str__()

	class Meta:
		verbose_name_plural = "Help_Desk, registros de solicitação de ajuda."

class Categoria_noticia(models.Model):
	"""
		Classe para categorizar as notícias, tipo se são de coletiva, se são Ação
		integrada, etc.
	"""
	titulo = models.CharField(max_length = 150)
	user = models.ForeignKey(User)

	def __unicode__(self):
		return self.titulo

	class Meta:
		verbose_name_plural = "Categoria das notícias."

class Noticias(models.Model):
	"""
		Classe destinada para a notificação como geral. Serão listadas notícias
	de até dois dias no template.
	"""
	titulo = models.CharField(max_length=300)
	categoria_da_noticia = models.ForeignKey(Categoria_noticia)
	data_publicacao = models.DateTimeField(auto_now=True)
	nota = models.TextField()
	user = models.ForeignKey(User)

	def __unicode__(self):
		return self.titulo

	class Meta:
		verbose_name_plural = "Notícias para disponibilizar no portal."

class Agenda(models.Model):
	evento = models.CharField(max_length=150)
	


	