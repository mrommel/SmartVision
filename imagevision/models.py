# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import uuid
from django.db import models
from django.contrib.staticfiles import finders

# Create your models here.

class Tag(models.Model):
	name = models.CharField(max_length=50)
	
	def __str__(self):
		return self.name
	
	class Meta:
		ordering = ('name',)


class Image(models.Model):
	unique_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
	filename = models.CharField(max_length=50)
	title = models.CharField(max_length=50, blank=True, null=True)
	folder = models.CharField(max_length=200, blank=True, null=True)
	tags = models.ManyToManyField(Tag)
	
	def __str__(self):
		return self.filename
	
	class Meta:
		ordering = ('filename',)
	
