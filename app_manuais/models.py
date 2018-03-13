# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import *


class Manual(models.Model):
	titulo = models.CharField(max_length = 150)
	arquivo = models.FileField(upload_to="manuais/%Y/%m/%d/")
	user = models.ForeignKey(User)

	def __unicode__(self):
		return self.titulo.__str__()

