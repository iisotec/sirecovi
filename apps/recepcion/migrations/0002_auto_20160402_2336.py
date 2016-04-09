# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recepcion', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='visitanteoficina',
            old_name='feha_visita',
            new_name='fecha_visita',
        ),
    ]
