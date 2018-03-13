# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import *


class Tutorial(models.Model):
	titulo = models.CharField(max_length = 150)
	video = models.FileField(upload_to="Guia_implantacao/videos/%Y/%m/%d/", null= True)
	documento = models.FileField(upload_to="Guia_implantacao/documentos/%Y/%m/%d/", null= True)
	conteudo = models.TextField()
	user = models.ForeignKey(User)

	def __unicode__(self):
		return self.titulo.__str__()