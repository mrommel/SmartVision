# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
import sys

from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import RequestContext, loader
from django.template.loader import render_to_string


def index(request):
	path="/Users/michael.rommel/365Farmnet/365Farmnet Icons/"
	folder_list=os.listdir(path)   
	folder_list.remove('.DS_Store')
	
	return HttpResponse(render_to_string('imagevision/index.html', {
		'folders': folder_list,
	}))
	
class Image:

	def __init__(self):
		self.name = ''
		self.image = ''
		self.eps = ''
		self.pdf = ''
		self.svg = ''
		
class Images:
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
			item = Image()
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
	
	images = Images()
	
	for file in file_list:
		if file <> '.DS_Store':
			images.addFile(folder_name, file)
		
	image_list = images.items
	image_list.sort(key=lambda x: x.name)

	return HttpResponse(render_to_string('imagevision/folder.html', {
		'folder_name': folder_name,
		'image_list': image_list
	}))
	
def detail(request, folder_name, image_name):

	path="/Users/michael.rommel/365Farmnet/365Farmnet Icons/%s" % (folder_name)
	file_list=os.listdir(path)   
	#image_list.remove('.DS_Store')
	
	images = Images()
	
	for file in file_list:
		if file <> '.DS_Store':
			images.addFile(folder_name, file)
		
	image_list = images.items
	image_item = next((x for x in image_list if x.name == image_name), None)

	return HttpResponse(render_to_string('imagevision/detail.html', {
		'image_list': image_list,
		'image_name': image_name,
		'folder_name': folder_name,
		'image_item': image_item
	}))
	
	
def image(request, folder_name, image_name):

	print >>sys.stderr, 'image: %s, %s' % (folder_name, image_name)	
	path="/Users/michael.rommel/365Farmnet/365Farmnet Icons/%s/%s.png" % (folder_name, image_name)
	print >>sys.stderr, 'path: %s' % (path)	
	
	image_data = open(path, "rb").read()
	return HttpResponse(image_data, content_type='image/png')

def image_eps(request, folder_name, image_name):

	print >>sys.stderr, 'image: %s, %s' % (folder_name, image_name)	
	path="/Users/michael.rommel/365Farmnet/365Farmnet Icons/%s/%s.eps" % (folder_name, image_name)
	print >>sys.stderr, 'path: %s' % (path)	
	
	image_data = open(path, "rb").read()
	return HttpResponse(image_data, content_type='application/eps')
	
def image_pdf(request, folder_name, image_name):

	print >>sys.stderr, 'image: %s, %s' % (folder_name, image_name)	
	path="/Users/michael.rommel/365Farmnet/365Farmnet Icons/%s/%s.pdf" % (folder_name, image_name)
	print >>sys.stderr, 'path: %s' % (path)	
	
	image_data = open(path, "rb").read()
	return HttpResponse(image_data, content_type='application/pdf')
	
def image_svg(request, folder_name, image_name):

	print >>sys.stderr, 'image: %s, %s' % (folder_name, image_name)	
	path="/Users/michael.rommel/365Farmnet/365Farmnet Icons/%s/%s.svg" % (folder_name, image_name)
	print >>sys.stderr, 'path: %s' % (path)	
	
	image_data = open(path, "rb").read()
	return HttpResponse(image_data, content_type='image/svg+xml')
