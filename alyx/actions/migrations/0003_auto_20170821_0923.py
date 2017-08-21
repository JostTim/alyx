# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-08-21 08:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0003_auto_20170821_0923'),
        ('behavior', '0003_auto_20170821_0923'),
        ('electrophysiology', '0003_auto_20170821_0923'),
        ('imaging', '0003_auto_20170821_0923'),
        ('actions', '0002_experiment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='experiment',
            name='parent_experiment',
        ),
        migrations.RemoveField(
            model_name='experiment',
            name='session',
        ),
        migrations.AddField(
            model_name='session',
            name='parent_session',
            field=models.ForeignKey(blank=True, help_text='Hierarchical parent to this session', null=True, on_delete=django.db.models.deletion.CASCADE, to='actions.Session'),
        ),
        migrations.DeleteModel(
            name='Experiment',
        ),
    ]
