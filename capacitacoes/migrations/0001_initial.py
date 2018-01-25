# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-01-25 19:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=150)),
                ('data_realizacao', models.DateField()),
                ('hora_realizacao', models.TimeField()),
                ('video_promocional', models.FileField(upload_to='videos_capacitacoes/%Y/%m/%d/')),
                ('Notas', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Eventos de Capacita\xe7\xf5es do Portal SEI',
            },
        ),
    ]