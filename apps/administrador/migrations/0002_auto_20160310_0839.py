# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('administrador', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='oficina',
            name='usuario',
        ),
        migrations.RemoveField(
            model_name='oficina',
            name='visit_oficina',
        ),
        migrations.DeleteModel(
            name='Oficina',
        ),
        migrations.DeleteModel(
            name='Visitante',
        ),
    ]
