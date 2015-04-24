# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20150424_1812'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alliance',
            name='alliance_id',
            field=models.IntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='character',
            name='character_id',
            field=models.IntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='constellation',
            name='const_id',
            field=models.IntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='corporation',
            name='corporation_id',
            field=models.IntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='structure',
            name='structure_id',
            field=models.IntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='system',
            name='system_id',
            field=models.IntegerField(unique=True),
        ),
    ]
