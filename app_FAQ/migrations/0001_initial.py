# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-12 23:02
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app_documentos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Duvidas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('resposta', models.TextField()),
                ('tags', models.ManyToManyField(to='app_documentos.Tag')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Duvidas Frequentes dos Usu\xe1rios do Sei',
            },
        ),
    ]
