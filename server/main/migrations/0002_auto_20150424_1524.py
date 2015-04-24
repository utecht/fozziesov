# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='stratop',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 24, 15, 24, 3, 629555, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='stratop',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, default=1),
            preserve_default=False,
        ),
    ]
