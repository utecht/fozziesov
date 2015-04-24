# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20150424_1811'),
    ]

    operations = [
        migrations.AlterField(
            model_name='controlnode',
            name='control',
            field=models.ForeignKey(to='main.Alliance', null=True, blank=True),
        ),
    ]
