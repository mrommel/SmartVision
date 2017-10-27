# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-27 06:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vision', '0015_auto_20171027_0650'),
    ]

    operations = [
        migrations.AddField(
            model_name='button',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vision.Container'),
        ),
        migrations.AddField(
            model_name='imageview',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vision.Container'),
        ),
        migrations.AddField(
            model_name='label',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vision.Container'),
        ),
    ]
