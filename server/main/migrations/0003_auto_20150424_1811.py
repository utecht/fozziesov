# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20150424_1524'),
    ]

    operations = [
        migrations.AlterField(
            model_name='controlnode',
            name='control',
            field=models.ForeignKey(to='main.Alliance', default=1, blank=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='event',
            name='time',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='systemevent',
            name='time',
            field=models.DateTimeField(),
        ),
    ]
