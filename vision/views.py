# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import RequestContext, loader
from django.template.loader import render_to_string

from .models import *

def index(request):
	return HttpResponse(render_to_string('vision/index.html', {}))

def projects(request):
	projects_list = Project.objects.all
	return HttpResponse(render_to_string('vision/projects.html', {'projects_list': projects_list,}))

def project(request, project_id):
	
	try:
		project = Project.objects.get(pk=project_id)
	except Project.DoesNotExist:
		raise Http404("Project does not exist")
		
	controller_list = project.controllers()
	
	return HttpResponse(render_to_string('vision/project.html', {'project': project, 'controller_list': controller_list, }))

def controller(request, controller_id):
	try:
		controller = ViewController.objects.get(pk=controller_id)
	except ViewController.DoesNotExist:
		raise Http404("ViewController does not exist")
	
	return HttpResponse(render_to_string('vision/controller.html', {'controller': controller,}))
	
def controller_image(request, controller_id):
	return HttpResponse("<!--?xml version=\"1.0\" standalone=\"no\"?--><svg width=\"5cm\" height=\"4cm\" version=\"1.1\" xmlns:xlink=\"http://www.w3.org/1999/xlink\"><image xlink:href=\"firefox.jpg\" x=\"0\" y=\"0\" height=\"50px\" width=\"50px\"></image></svg>", content_type="image/svg+xml")