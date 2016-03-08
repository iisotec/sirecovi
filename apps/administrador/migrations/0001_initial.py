# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Oficina',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(help_text=b'Nombre', max_length=120)),
                ('estado', models.BooleanField(default=False)),
                ('usuario', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Visitante',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dni', models.CharField(max_length=8)),
                ('nombres', models.CharField(help_text=b'Nombres', max_length=80)),
                ('apellidos', models.CharField(help_text=b'Apellidos', max_length=120)),
                ('fecha_visita', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='oficina',
            name='visit_oficina',
            field=models.ManyToManyField(to='administrador.Visitante'),
        ),
    ]
