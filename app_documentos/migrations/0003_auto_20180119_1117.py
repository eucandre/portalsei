# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-01-19 13:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_documentos', '0002_noticias_credito_midia'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='noticias',
            name='credito_midia',
        ),
        migrations.AddField(
            model_name='noticias',
            name='credito_midia_imagem',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AddField(
            model_name='noticias',
            name='credito_midia_video',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]