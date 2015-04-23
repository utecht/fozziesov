# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alliance',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('alliance_id', models.IntegerField()),
                ('name', models.CharField(max_length=200)),
                ('ticker', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='AllianceState',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('alliance', models.ForeignKey(to='main.Alliance')),
            ],
        ),
        migrations.CreateModel(
            name='Battle',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('character_id', models.IntegerField()),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Constellation',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('const_id', models.IntegerField()),
                ('region', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ControlNode',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('battle', models.ForeignKey(to='main.Battle')),
                ('control', models.ForeignKey(null=True, to='main.Alliance')),
            ],
        ),
        migrations.CreateModel(
            name='Corporation',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('corporation_id', models.IntegerField()),
                ('name', models.CharField(max_length=200)),
                ('ticker', models.CharField(max_length=5)),
                ('alliance', models.ForeignKey(to='main.Alliance')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('time', models.DateField()),
                ('text', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Stratop',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('constellation', models.ForeignKey(to='main.Constellation')),
                ('good_guys', models.ForeignKey(to='main.Alliance')),
            ],
        ),
        migrations.CreateModel(
            name='Structure',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('structure_id', models.IntegerField()),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='System',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('system_id', models.IntegerField()),
                ('name', models.CharField(max_length=50)),
                ('constellation', models.ForeignKey(to='main.Constellation')),
            ],
        ),
        migrations.CreateModel(
            name='SystemAllianceState',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('alliance', models.ForeignKey(to='main.Alliance')),
                ('stratop', models.ForeignKey(to='main.Stratop')),
                ('system', models.ForeignKey(to='main.System')),
            ],
        ),
        migrations.CreateModel(
            name='SystemEvent',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('time', models.DateField()),
                ('text', models.CharField(max_length=50)),
                ('stratop', models.ForeignKey(to='main.Stratop')),
                ('system', models.ForeignKey(to='main.System')),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='stratop',
            field=models.ForeignKey(to='main.Stratop'),
        ),
        migrations.AddField(
            model_name='controlnode',
            name='system',
            field=models.ForeignKey(to='main.System'),
        ),
        migrations.AddField(
            model_name='character',
            name='corporation',
            field=models.ForeignKey(to='main.Corporation'),
        ),
        migrations.AddField(
            model_name='battle',
            name='stratop',
            field=models.ForeignKey(to='main.Stratop'),
        ),
        migrations.AddField(
            model_name='battle',
            name='structure',
            field=models.ForeignKey(to='main.Structure'),
        ),
        migrations.AddField(
            model_name='battle',
            name='system',
            field=models.ForeignKey(to='main.System'),
        ),
        migrations.AddField(
            model_name='alliancestate',
            name='stratop',
            field=models.ForeignKey(to='main.Stratop'),
        ),
    ]
