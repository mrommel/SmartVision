# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-27 13:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vision', '0020_auto_20171027_1021'),
    ]

    operations = [
        migrations.RenameField(
            model_name='button',
            old_name='action',
            new_name='event',
        ),
        migrations.RenameField(
            model_name='container',
            old_name='action',
            new_name='event',
        ),
        migrations.RenameField(
            model_name='imageview',
            old_name='action',
            new_name='event',
        ),
        migrations.RenameField(
            model_name='label',
            old_name='action',
            new_name='event',
        ),
        migrations.AddField(
            model_name='action',
            name='duration',
            field=models.IntegerField(default=5),
        ),
        migrations.AddField(
            model_name='action',
            name='start',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='action',
            name='targetContainer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vision.Container'),
        ),
        migrations.AddField(
            model_name='action',
            name='targetImageView',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vision.ImageView'),
        ),
        migrations.AddField(
            model_name='action',
            name='targetLabel',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vision.Label'),
        ),
        migrations.AddField(
            model_name='action',
            name='to',
            field=models.IntegerField(default=40),
        ),
        migrations.AlterField(
            model_name='action',
            name='actionType',
            field=models.CharField(choices=[('v', 'Goto ViewController'), ('x', 'Slide View on x-Axis'), ('y', 'Slide View on y-Axis')], max_length=1),
        ),
    ]