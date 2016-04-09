# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oficina', '0005_auto_20160324_1705'),
    ]

    operations = [
        migrations.CreateModel(
            name='Visitante',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dni', models.CharField(unique=True, max_length=8, db_index=True)),
                ('nombres', models.CharField(help_text=b'Nombres', max_length=80)),
                ('apellidos', models.CharField(help_text=b'Apellidos', max_length=120)),
                ('fecha_registro', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='VisitanteOficina',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('feha_visita', models.DateTimeField(auto_now_add=True)),
                ('estado_atencion', models.BooleanField()),
                ('sesion', models.BooleanField()),
                ('oficina', models.ForeignKey(to='oficina.Oficina')),
                ('visitante', models.ForeignKey(to='recepcion.Visitante')),
            ],
        ),
        migrations.AddField(
            model_name='visitante',
            name='oficinas',
            field=models.ManyToManyField(to='oficina.Oficina', through='recepcion.VisitanteOficina'),
        ),
    ]
