# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-08-17 20:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('screens', '0003_auto_20180817_2012'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='screenrelation',
            name='layer',
        ),
        migrations.AddField(
            model_name='screenrelation',
            name='layer',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='screens.Layer'),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='screenrelation',
            name='screen',
        ),
        migrations.AddField(
            model_name='screenrelation',
            name='screen',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='screens.Screen'),
            preserve_default=False,
        ),
    ]