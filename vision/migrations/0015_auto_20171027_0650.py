# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-27 06:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vision', '0014_auto_20171027_0622'),
    ]

    operations = [
        migrations.CreateModel(
            name='Container',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('x', models.IntegerField(default=0)),
                ('y', models.IntegerField(default=0)),
                ('width', models.IntegerField(default=40)),
                ('height', models.IntegerField(default=40)),
                ('z', models.IntegerField(default=-1)),
                ('color', models.CharField(default='#f5f5f7', max_length=7)),
                ('viewController', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vision.ViewController')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='rect',
            name='viewController',
        ),
        migrations.AlterField(
            model_name='button',
            name='color',
            field=models.CharField(default='#f5f5f7', max_length=7),
        ),
        migrations.AlterField(
            model_name='imageview',
            name='color',
            field=models.CharField(default='#f5f5f7', max_length=7),
        ),
        migrations.AlterField(
            model_name='label',
            name='color',
            field=models.CharField(default='#f5f5f7', max_length=7),
        ),
        migrations.DeleteModel(
            name='Rect',
        ),
    ]
