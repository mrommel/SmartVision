# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from colorfield.fields import ColorField

class Project(models.Model):
	name = models.CharField(max_length=50)
	image = models.FileField(upload_to='projects/', null=True, blank=True)
	
	def layouts(self):
		return Layout.objects.filter(project=self)
	
	def __unicode__(self): 
		return self.name


class Layout(models.Model):
	name = models.CharField(max_length=50)
	project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True, blank=True)
	
	def screens(self):
		return LayoutScreenRelation.objects.filter(layout=self)
		
	def screen_table(self):
		
		rows = LayoutRow.objects.filter(layout=self)	
		table = []
		
		for layout_row in rows:
			screens = []
			values = LayoutScreenRelation.objects.filter(layout=self,row=layout_row.row)
			for value in values:
				screens.append(value.screen)
			
			row = [layout_row.name]
			row.extend(screens)
			table.append(row)
			
		return table
	
	def __unicode__(self): 
		return self.name


class LayoutRow(models.Model):
	name = models.CharField(max_length=50)
	layout = models.ForeignKey(Layout, on_delete=models.CASCADE)
	row = models.IntegerField(default=0)
	
	def __unicode__(self): 
		return self.name
	

class Screen(models.Model):
	name = models.CharField(max_length=50)
	layout = models.ForeignKey(Layout, on_delete=models.CASCADE, null=True, blank=True)
	
	def layers(self):
		return ScreenLayerRelation.objects.filter(screen=self)
	
	def __unicode__(self): 
		return self.name


LAYER_TYPES = (
    ('B', 'Background'),
    ('I', 'Image'),
    ('U', 'User'),
)

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
		
		
class ScreenLayerRelation(models.Model):
	screen = models.ForeignKey(Screen)
	layer = models.ForeignKey(Layer)
	level = models.IntegerField()
	
	def __unicode__(self): 
		return '%s - %s' % (self.screen.name, self.layer.name)
		
	
class LayoutScreenRelation(models.Model):
	layout = models.ForeignKey(Layout)
	screen = models.ForeignKey(Screen)
	row = models.IntegerField(default=0)
	col = models.IntegerField(default=0)
	
	def __unicode__(self): 
		return '%s - %s' % (self.layout.name, self.screen.name)
		