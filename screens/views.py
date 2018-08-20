# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import RequestContext, loader
from django.template.loader import render_to_string

from .models import *

# Create your views here.

def index(request):

	project_list = Project.objects.all()

	return HttpResponse(render_to_string('screens/index.html', {
		'project_list': project_list,
	}))
	
def project(request, project_id):
	
	try:
		project = Project.objects.get(id=project_id)
	except Project.DoesNotExist:
		raise Http404("Project does not exist")
		
	return HttpResponse(render_to_string('screens/project.html', {
		'project': project,
	}))
	
def layout(request, layout_id):
	
	try:
		layout = Layout.objects.get(id=layout_id)
	except Layout.DoesNotExist:
		raise Http404("Layout does not exist")
		
	return HttpResponse(render_to_string('screens/layout.html', {
		'layout': layout,
	}))
	
def screen_svg(request, screen_id):

	try:
		screen = Screen.objects.get(id=screen_id)
	except Screen.DoesNotExist:
		raise HTTP404("Screen does not exist")
		
	return HttpResponse(render_to_string('svg.html', {
		'screen': screen,
	})) 