# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oficina', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='oficina',
            old_name='estado',
            new_name='estado_atencion',
        ),
        migrations.AddField(
            model_name='oficina',
            name='estado_oficina',
            field=models.BooleanField(default=False),
        ),
    ]
