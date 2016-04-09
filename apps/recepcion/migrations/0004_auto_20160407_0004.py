# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recepcion', '0003_auto_20160403_0901'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visitante',
            name='oficinas',
            field=models.ManyToManyField(to='oficina.Oficina', through='recepcion.VisitanteOficina', blank=True),
        ),
    ]
