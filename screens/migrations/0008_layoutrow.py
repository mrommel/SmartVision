# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-08-20 19:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('screens', '0007_layoutscreenrelation'),
    ]

    operations = [
        migrations.CreateModel(
            name='LayoutRow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('row', models.IntegerField(default=0)),
                ('layout', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='screens.Layout')),
            ],
        ),
    ]
