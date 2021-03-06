# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-26 12:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vision', '0003_button'),
    ]

    operations = [
        migrations.AddField(
            model_name='button',
            name='hover',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='button_hover', to='vision.Image'),
        ),
        migrations.AddField(
            model_name='button',
            name='pressed',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='button_pressed', to='vision.Image'),
        ),
        migrations.AlterField(
            model_name='button',
            name='normal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='button_normal', to='vision.Image'),
        ),
    ]
