# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-01-09 15:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_documentos', '0003_auto_20171214_1841'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tipo_Documento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(choices=[('MANUAL', 'MANUAL'), ('PLANO_DE_COMUNICACAO', 'PLANO_DE_COMUNICACAO'), ('DOCUMENTO_DE_APOIO', 'DOCUMENTO_DE_APOIO')], max_length=150)),
            ],
            options={
                'verbose_name_plural': 'Tipo de Documento',
            },
        ),
        migrations.AlterModelOptions(
            name='categoria_noticia',
            options={'verbose_name_plural': 'Categoria das not\xedcias.'},
        ),
        migrations.AlterModelOptions(
            name='cliente',
            options={'verbose_name_plural': 'Clientes para Solicita\xe7\xe3o de help Desk'},
        ),
        migrations.AlterModelOptions(
            name='help_desk',
            options={'verbose_name_plural': 'Help_Desk, registros de solicita\xe7\xe3o de ajuda.'},
        ),
        migrations.AlterModelOptions(
            name='noticias',
            options={'verbose_name_plural': 'Not\xedcias para disponibilizar no portal.'},
        ),
        migrations.AlterModelOptions(
            name='setor',
            options={'verbose_name_plural': 'Setor da Secretaria ou de \xd3rg\xe3o.'},
        ),
        migrations.AddField(
            model_name='documentos',
            name='tipo',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app_documentos.Tipo_Documento'),
            preserve_default=False,
        ),
    ]