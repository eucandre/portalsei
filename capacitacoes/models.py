# coding=utf-8
from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import *

class Evento(models.Model):
	titulo = models.CharField(max_length=150)
	data_realizacao = models.DateField()
	hora_realizacao = models.TimeField()
	video_promocional = models.FileField(upload_to="videos_capacitacoes/%Y/%m/%d/")
	Notas = models.TextField(help_text="acrescentar conteúdos explicativos com links e outros.")
	user = models.ForeignKey(User)
	
	def __unicode__(self):
		return self.titulo

	class Meta:
		verbose_name_plural = "Eventos de Capacitações do Portal SEI"

