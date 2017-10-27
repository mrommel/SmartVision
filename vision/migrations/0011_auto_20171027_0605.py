# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-27 06:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vision', '0010_auto_20171027_0558'),
    ]

    operations = [
        migrations.AddField(
            model_name='label',
            name='fontColor',
            field=models.CharField(default='#eeeeee', max_length=7),
        ),
        migrations.AlterField(
            model_name='button',
            name='color',
            field=models.CharField(default='#000000', max_length=7),
        ),
        migrations.AlterField(
            model_name='imageview',
            name='color',
            field=models.CharField(default='#000000', max_length=7),
        ),
        migrations.AlterField(
            model_name='label',
            name='color',
            field=models.CharField(default='#000000', max_length=7),
        ),
    ]
