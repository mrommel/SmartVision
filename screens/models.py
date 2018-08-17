# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from colorfield.fields import ColorField

class Project(models.Model):
	name = models.CharField(max_length=50)
	
	def __unicode__(self): 
		return self.name

LAYER_TYPES = (
    ('B', 'Background'),
    ('I', 'Image'),
    ('U', 'User'),
)

class Screen(models.Model):
	name = models.CharField(max_length=50)
	project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True, blank=True)
	
	def __unicode__(self): 
		return self.name


class Layer(models.Model):
	name = models.CharField(max_length=50)
	type = models.CharField(max_length=1, choices=LAYER_TYPES, default='B', )
	color = ColorField(default='#FF0000')
	image = models.FileField(upload_to='uploads/', null=True, blank=True)
	x_offset = models.IntegerField(default=0)
	y_offset = models.IntegerField(default=0)
	
	
	def __unicode__(self): 
		return self.name
	
	class Meta:
		ordering = ('name', 'type', )
		
		
class ScreenRelation(models.Model):
	screen = models.ForeignKey(Screen)
	layer = models.ForeignKey(Layer)
	level = models.IntegerField()
	
	def __unicode__(self): 
		return '%s - %s' % (self.screen.name, self.layer.name)