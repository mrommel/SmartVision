# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# 750x1334px
class ViewController(models.Model):
	name = models.CharField(max_length=50)
	pub_date = models.DateTimeField('date published')
	
	def __unicode__(self):              # __unicode__ on Python 2
		return self.name

class View(models.Model):
	viewController = models.ForeignKey(ViewController, on_delete=models.CASCADE)
	name = models.CharField(max_length=50)
	x = models.IntegerField(default=0)
	y = models.IntegerField(default=0)
	width = models.IntegerField(default=40)
	height = models.IntegerField(default=40)
	z = models.IntegerField(default=-1)

	class Meta:
		abstract = True


class Image(models.Model):
	name = models.CharField(max_length=50)
	image = models.FileField(upload_to='documents/%Y/%m/%d')

	def __unicode__(self):              # __unicode__ on Python 2
		return self.name
	
	
class ImageView(View):
	image = models.ForeignKey(Image, on_delete=models.CASCADE)
	

class Button(View):
	normal = models.ForeignKey(Image, related_name='button_normal', on_delete=models.CASCADE)
	hover = models.ForeignKey(Image, related_name='button_hover', on_delete=models.CASCADE, blank=True, null=True)
	pressed = models.ForeignKey(Image, related_name='button_pressed', on_delete=models.CASCADE, blank=True, null=True)