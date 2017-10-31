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
	initial_controller = project.initial_controller()
	
	scripts = ''
	for controller in controller_list:
		scripts = '%s%s' % (scripts, controller.script())
	
	return HttpResponse(render_to_string('vision/project.html', {'project': project, 'controller_list': controller_list, 'initial_controller': initial_controller, 'scripts': scripts, }))

"""
	shows content of a controller
"""
def controller(request, controller_id):
	try:
		controller = ViewController.objects.get(pk=controller_id)
	except ViewController.DoesNotExist:
		raise Http404("ViewController does not exist")
	
	view_list = controller.views()
	
	return HttpResponse(render_to_string('vision/controller.html', {'controller': controller, 'view_list': view_list,}))
	
"""
	returns a svg representation of the controller
"""
def controller_image(request, controller_id):
	
	try:
		controller = ViewController.objects.get(pk=controller_id)
	except ViewController.DoesNotExist:
		raise Http404("ViewController does not exist")
		
	controller_svg = controller.svg()
	
	return HttpResponse(controller_svg, content_type="image/svg+xml")
	
