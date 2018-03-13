# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from app_documentos.models import *
from django.contrib.auth.models import *


class Duvidas(models.Model):
	titulo = models.CharField(max_length = 200)
	tags = models.ManyToManyField(Tag)
	resposta = models.TextField()
	user = models.ForeignKey(User)
	
	def __unicode__(self):
		return self.titulo.__str__()

	class Meta:
		verbose_name_plural = 'Duvidas Frequentes dos Usuários do Sei'


