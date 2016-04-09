# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recepcion', '0002_auto_20160402_2336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visitanteoficina',
            name='estado_atencion',
            field=models.BooleanField(default=False),
        ),
    ]
