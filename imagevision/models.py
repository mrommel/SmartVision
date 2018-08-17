# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import uuid
from django.db import models
from django.contrib.staticfiles import finders

# Create your models here.

class Tag(models.Model):
	name = models.CharField(max_length=50)
	
	def __unicode__(self): 
		return self.name
	
	class Meta:
		ordering = ('name',)


class Image(models.Model):
	unique_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
	filename = models.CharField(max_length=50)
	title = models.CharField(max_length=50, blank=True, null=True)
	folder = models.CharField(max_length=200, blank=True, null=True)
	tags = models.ManyToManyField(Tag, blank=True, null=True)
	related = models.ManyToManyField("self", blank=True)
	
	def full_path(self):
		return "/Users/michael.rommel/365Farmnet/365Farmnet Icons/%s/%s" % (self.folder, self.filename)
	
	def thumbnail(self):
		return '<img border="0" alt="" src="/images/images/%s.png" height="40" />' % ((self.unique_id))
	thumbnail.allow_tags = True
	
	def detailed(self):
		return '<img border="0" alt="" src="/images/images/%s.png" height="120" />' % ((self.unique_id))
	detailed.allow_tags = True
	
	def detail_link(self):
		return u'<a href="/images/detail/%s/">%s</a>' % (self.unique_id, self)
	detail_link.allow_tags = True
	detail_link.short_description = "Show" 
	
	def tag_list(self):
		str = ''
		
		for tag in self.tags.all():
			str = '%s, %s' % (str, tag.name)
		
		return str
		
	def related_links(self):
		related_str = ''
		
		for related_item in self.related.all():
			related_str = u'%s<a href="/admin/imagevision/image/%d/change/"><img border="0" alt="" src="/images/images/%s.png" height="40" /></a>, ' % (related_str, related_item.id, related_item.unique_id)
	
		return related_str
	related_links.allow_tags = True
	related_links.short_description = "Related"
	
	def __unicode__(self): 
		return self.filename
	
	class Meta:
		ordering = ('filename',)
	
