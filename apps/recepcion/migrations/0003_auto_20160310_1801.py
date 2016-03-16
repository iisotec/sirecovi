# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recepcion', '0002_auto_20160310_1736'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visitante',
            name='dni',
            field=models.CharField(unique=True, max_length=8),
        ),
    ]
