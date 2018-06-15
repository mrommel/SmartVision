# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
import sys

import os.path
from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import RequestContext, loader
from django.template.loader import render_to_string

from .models import *


def index(request):
	path="/Users/michael.rommel/365Farmnet/365Farmnet Icons/"
	folder_list=os.listdir(path)   
	folder_list.remove('.DS_Store')
	
	return HttpResponse(render_to_string('imagevision/index.html', {
		'folders': folder_list,
	}))
	
class ImageItem:

	def __init__(self):
		self.name = ''
		self.image = ''
		self.eps = ''
		self.pdf = ''
		self.svg = ''
		
class ImageItems:
	def __init__(self):
		self.items = []
		
	def addFile(self, folder, file_name):
		filename, file_extension = os.path.splitext(file_name)
		
		#print >>sys.stderr, 'Add file: %s => %s, %s' % (file_name, filename, file_extension)		
		updated = False
		
		for idx, item in enumerate(self.items):
			if item.name == filename:
			
				if file_extension == '.png':
					item.image = "/images/%s/%s" % (folder, file_name)
					item.image = item.image.replace(" ", "%20")
					
				if file_extension == '.eps':
					item.eps = "/images/%s/%s" % (folder, file_name)
					item.eps = item.eps.replace(" ", "%20")
					
				if file_extension == '.pdf':
					item.pdf = "/images/%s/%s" % (folder, file_name)
					item.pdf = item.pdf.replace(" ", "%20")
					
				if file_extension == '.svg':
					item.svg = "/images/%s/%s" % (folder, file_name)
					item.svg = item.svg.replace(" ", "%20")
					
				self.items[idx] = item
				
				updated = True
				
				#print >>sys.stderr, 'Updated'
				
		if updated == False:
			item = ImageItem()
			item.name = filename
			
			if file_extension == '.png':
				item.image = "/images/%s/%s" % (folder, file_name)
				item.image = item.image.replace(" ", "%20")
				
			if file_extension == '.eps':
				item.eps = "/images/%s/%s" % (folder, file_name)
				item.eps = item.eps.replace(" ", "%20")
				
			if file_extension == '.pdf':
				item.pdf = "/images/%s/%s" % (folder, file_name)
				item.pdf = item.pdf.replace(" ", "%20")
				
			if file_extension == '.svg':
				item.svg = "/images/%s/%s" % (folder, file_name)
				item.svg = item.svg.replace(" ", "%20")
				
			self.items.append(item)
			
			#print >>sys.stderr, 'Created'
	
def folder(request, folder_name):
	path="/Users/michael.rommel/365Farmnet/365Farmnet Icons/%s" % (folder_name)
	file_list=os.listdir(path)   
	#image_list.remove('.DS_Store')
	
	images = ImageItems()
	
	for file in file_list:
		if file <> '.DS_Store':
			images.addFile(folder_name, file)
		
	image_items = images.items
	image_items.sort(key=lambda x: x.name)
	
	for image_in_items in image_items:
		try:
			image = Image.objects.get(filename=image_in_items.name, folder=folder_name)
		except Image.DoesNotExist:
			image = Image(filename=image_in_items.name, folder=folder_name)
			image.save()
			
	image_list = Image.objects.filter(folder=folder_name)

	return HttpResponse(render_to_string('imagevision/folder.html', {
		'folder_name': folder_name,
		'image_list': image_list
	}))

def detail(request, identifier):
	try:
		image = Image.objects.get(unique_id=identifier)
	except Image.DoesNotExist:
		raise Http404("Image does not exist")
		
	return HttpResponse(render_to_string('imagevision/detail.html', {
		'image': image
	}))	
	
def tag(request, tag_id):
	try:
		tag = Tag.objects.get(id=tag_id)
	except Tag.DoesNotExist:
		raise Http404("Tag does not exist")
		
	image_list = Image.objects.filter(tags=tag)

	return HttpResponse(render_to_string('imagevision/tag.html', {
		'tag': tag,
		'image_list': image_list
	}))	
	
def image(request, identifier, extension, content_type):

	try:
		image = Image.objects.get(unique_id=identifier)
	except Image.DoesNotExist:
		raise Http404("Image does not exist")	
	
	image_path = "%s.%s" % (image.full_path(), extension)
	
	if os.path.isfile(image_path):
		try:
			image_file = open(image_path, "rb")
	
			image_data = image_file.read()
			return HttpResponse(image_data, content_type=content_type)
		except FileNotFoundError:
			raise Http404("could not read file")	
	else:
		raise Http404("Image of content_type does not exist")	
	
def image_png(request, identifier):

	return image(request, identifier, "png", "image/png")
	
def image_jpg(request, identifier):

	return image(request, identifier, "jpg", "image/jpg")

def image_eps(request, identifier):

	return image(request, identifier, "eps", "application/eps")

def image_pdf(request, identifier):

	return image(request, identifier, "pdf", "application/pdf")
	
def image_svg(request, identifier):

	return image(request, identifier, "svg", "image/svg+xml")
	

