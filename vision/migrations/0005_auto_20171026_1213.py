# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-26 12:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vision', '0004_auto_20171026_1210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='button',
            name='z',
            field=models.IntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='imageview',
            name='z',
            field=models.IntegerField(default=-1),
        ),
    ]
