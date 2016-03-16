# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oficina', '0002_auto_20160310_1736'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='oficina',
            name='estado_atencion',
        ),
    ]
