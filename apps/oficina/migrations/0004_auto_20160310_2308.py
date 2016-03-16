# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oficina', '0003_remove_oficina_estado_atencion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='oficina',
            name='nombre',
            field=models.CharField(help_text=b'Nombre', unique=True, max_length=120),
        ),
    ]
