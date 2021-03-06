# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-08-20 05:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('screens', '0005_auto_20180820_0531'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='screen',
            name='project',
        ),
        migrations.AddField(
            model_name='layout',
            name='project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='screens.Project'),
        ),
        migrations.AddField(
            model_name='screen',
            name='layout',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='screens.Layout'),
        ),
    ]
