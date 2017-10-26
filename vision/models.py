# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class ViewController(models.Model):
    question_text = models.CharField(max_length=200)
    name = models.CharField(max_length=50)
    pub_date = models.DateTimeField('date published')


class View(models.Model):
    viewController = models.ForeignKey(ViewController, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)