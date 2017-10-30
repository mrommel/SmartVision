# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.staticfiles import finders

class Project(models.Model):
	name = models.CharField(max_length=50)
	description = models.CharField(max_length=200, blank=True, null=True)
	
	"""
		list of all controllers that share the same project
	"""
	def controllers(self):
		return ViewController.objects.filter(project = self)
	
	def initial_controller(self):
		return ViewController.objects.get(project = self, initial = True)
	
	def __unicode__(self):             
		return self.name

# 750x1334px
class ViewController(models.Model):
	name = models.CharField(max_length=50)
	description = models.CharField(max_length=200, blank=True, null=True)
	project = models.ForeignKey(Project, on_delete=models.CASCADE)
	pub_date = models.DateTimeField('date published')
	initial = models.BooleanField(default=False)
	
	def views(self):
		view_list = list(ImageView.objects.filter(viewController = self))
		view_list.extend(list(Button.objects.filter(viewController = self)))
		view_list.extend(list(Label.objects.filter(viewController = self)))
		view_list.extend(list(Container.objects.filter(viewController = self)))
		
		view_list.sort(key=lambda x: x.z, reverse=False)
		
		return view_list
	
	def script(self): 
		view_list = list(ImageView.objects.filter(viewController = self))
		view_list.extend(list(Button.objects.filter(viewController = self)))
		view_list.extend(list(Label.objects.filter(viewController = self)))
		view_list.extend(list(Container.objects.filter(viewController = self)))
		
		scriptStr = ''
		for view in view_list:
			scriptStr = '%s\n%s' % (scriptStr, view.script())
			
		return scriptStr
		
	"""
		svg representation of this whole view controller
	"""
	def svg(self):
		background = "<g><title>background</title><rect fill=\"#efeff4\" id=\"canvas_background\" width=\"375\" height=\"667\" y=\"0\" x=\"0\"/><g display=\"none\" overflow=\"visible\" y=\"0\" x=\"0\" height=\"100%\" width=\"100%\" id=\"canvasGrid\"><rect fill=\"url(#gridpattern)\" stroke-width=\"0\" y=\"0\" x=\"0\" width=\"375\" height=\"667\"/></g></g>"
		
		view_list = list(ImageView.objects.filter(viewController = self))
		view_list.extend(list(Button.objects.filter(viewController = self)))
		view_list.extend(list(Label.objects.filter(viewController = self)))
		view_list.extend(list(Container.objects.filter(viewController = self)))
		
		view_list.sort(key=lambda x: x.z, reverse=False)
		
		viewStr = ''
		for view in view_list:
			viewStr = '%s\n%s' % (viewStr, view.svg())
	
		return "<svg xmlns=\"http://www.w3.org/2000/svg\" xmlns:xlink=\"http://www.w3.org/1999/xlink\" width=\"375px\" height=\"667px\" viewBox=\"0 0 375 667\">%s%s</svg>" % (background, viewStr)
	
	def __unicode__(self):              
		return self.name

class Image(models.Model):
	name = models.CharField(max_length=50)
	image = models.FileField(upload_to='documents/%Y/%m/%d')

	def __unicode__(self):              
		return self.name


ACTIONCHOICE = (
    ('v', 'Goto ViewController'),
    ('x', 'Slide View on x-Axis'),
    ('y', 'Slide View on y-Axis'),
)

class Action(models.Model):
	name = models.CharField(max_length=50, default='default action')
	actionType = models.CharField(max_length=1, choices=ACTIONCHOICE)
	targetViewController = models.ForeignKey(ViewController, on_delete=models.CASCADE, blank=True, null=True)
	targetContainer = models.ForeignKey('Container', on_delete=models.CASCADE, blank=True, null=True)
	targetImageView = models.ForeignKey('ImageView', on_delete=models.CASCADE, blank=True, null=True)
	targetLabel = models.ForeignKey('Label', on_delete=models.CASCADE, blank=True, null=True)
	start = models.IntegerField(default=0)
	to = models.IntegerField(default=40)
	duration = models.IntegerField(default=5) # in seconds

	def __unicode__(self):              
		return self.name

class View(models.Model):
	viewController = models.ForeignKey(ViewController, on_delete=models.CASCADE, blank=True, null=True)
	name = models.CharField(max_length=50)
	x = models.IntegerField(default=0)
	y = models.IntegerField(default=0)
	width = models.IntegerField(default=40)
	height = models.IntegerField(default=40)
	z = models.IntegerField(default=-1)
	color = models.CharField(max_length=7, default='#f5f5f7')
	event = models.ForeignKey('Action', on_delete=models.CASCADE, blank=True, null=True)

	def uniqueIdentifier(self):
		return 'vc%dview%d' % (self.viewController.id, self.id)
				
	def svg(self):
		return 'svg: %s' % self.name
		
	def script(self):
		if self.event == None:
			return ''
	
		if self.event.actionType == 'v' and self.event.targetViewController <> None:
			return 'var %s = svg.getElementById("%s"); if(%s != null) { %s.onclick = function() { console.log("%s clicked"); var svgholder = document.getElementById("svgholder"); svgholder.src = "/vision/controller_image/%d/image.svg"; }; }' % (self.uniqueIdentifier(), self.uniqueIdentifier(), self.uniqueIdentifier(), self.uniqueIdentifier(), self.uniqueIdentifier(), self.event.targetViewController.id)
	
		if self.event.actionType == 'x':
			# $('#drawing g.my-group .my-element')
			# var svgholder = document.getElementById("svgholder");  works
			# var svg = svgholder.getSVGDocument(); console.log("some svg loaded " + svg); works
			#
			# var elem = document.getElementById("%s"); var element = svg.get("%s"); console.log("x %s clicked " + element + "/" + elem + "/" + svgholder);
			#
			# SVG.adopt(element).animate(2000).move(%d, 0).after(function(situation) { console.log("xani"); });
			#
			# , self.uniqueIdentifier(), self.uniqueIdentifier(), self.uniqueIdentifier(), (self.event.to - self.event.start)
			return 'var %s = svg.getElementById("%s"); if(%s != null) { %s.onclick = function() { SVG.adopt(%s).animate(2000).move(%d, 0) }; }' % (self.uniqueIdentifier(), self.uniqueIdentifier(), self.uniqueIdentifier(), self.uniqueIdentifier(), self.uniqueIdentifier(), (self.event.to - self.event.start))
			
		if self.event.actionType == 'y':
			return 'var %s = svg.getElementById("%s"); if(%s != null) { %s.onclick = function() { var element = SVG.get("%s"); console.log("y %s clicked " + element); SVG.adopt(element).animate(2000).move(0, %d).after(function(situation) { console.log("xani"); }); }; }' % (self.uniqueIdentifier(), self.uniqueIdentifier(), self.uniqueIdentifier(), self.uniqueIdentifier(), self.uniqueIdentifier(), self.uniqueIdentifier(), (self.event.to - self.event.start))
	
		return ''

	class Meta:
		abstract = True


class Container(View):
		
	def children(self):
		view_list = list(ImageView.objects.filter(parent = self))
		view_list.extend(list(Button.objects.filter(parent = self)))
		view_list.extend(list(Label.objects.filter(parent = self)))
		
		view_list.sort(key=lambda x: x.z, reverse=False)
		
		return view_list

	def script(self):
		view_str = super(Container, self).script()
		
		for view in self.children():
			view_str = '%s\n%s' % (view_str, view.script())
		
		return view_str

	def svg(self):
		container_content = ''

		for view in self.children():
			container_content = '%s\n%s' % (container_content, view.svg())
	
		return '<g><title>%s</title><rect fill="%s" x="%d" y="%d" width="%d" height="%d" id="%s"></rect></g><g transform="translate(%d,%d)"><title>container_content</title>%s</g>' % (self.name, self.color, self.x, self.y, self.width, self.height, self.uniqueIdentifier(), self.x, self.y, container_content)
	
	def __unicode__(self):              
		return self.name

class Label(View):
	parent = models.ForeignKey(Container, on_delete=models.CASCADE, blank=True, null=True)
	text = models.CharField(max_length=50)
	fontSize = models.IntegerField(default=14)
	fontColor = models.CharField(max_length=7, default='#000000')
	
	def uniqueIdentifier(self):
		if self.viewController <> None:
			return 'vc%dview%d' % (self.viewController.id, self.id)
		
		return '%sview%d' % (self.parent.uniqueIdentifier(), self.id)
	
	def svg(self):
		return '<g><title>%s</title><rect fill=\"%s\" x="%d" y="%d" width="%d" height="%d"></rect><text x="%d" y="%d" fill="%s" text-anchor="middle" alignment-baseline="central">%s</text><style><![CDATA[text{ font: %dpx SFUIText-Light, SFUIText-Regular, SanFranciscoText-Light, SFCompactText-Light, HelveticaNeue-Light Helvetica Neue, Helvetica, Verdana, Arial, sans-serif;}]]></style></g>' % (self.name, self.color, self.x, self.y, self.width, self.height, self.x + self.width / 2, self.y + self.height / 2, self.fontColor, self.text, self.fontSize)
	
	def __unicode__(self):              
		return self.name
	
class ImageView(View):
	parent = models.ForeignKey(Container, on_delete=models.CASCADE, blank=True, null=True)
	image = models.ForeignKey(Image, on_delete=models.CASCADE, blank=True, null=True)
	
	def uniqueIdentifier(self):
		if self.viewController <> None:
			return 'vc%dview%d' % (self.viewController.id, self.id)
		
		return '%sview%d' % (self.parent.uniqueIdentifier(), self.id)
	
	#def script(self):
	#	if self.event == None:
	#		return ''
	#
	#	if self.event.actionType == 'v':
	#		return 'var %s = svg.getElementById("%s"); if (%s != null) { %s.onclick = function() { console.log("%s clicked"); var svgholder = document.getElementById("svgholder"); svgholder.src = "/vision/controller_image/%d/image.svg"; }; }' % (self.uniqueIdentifier(), self.uniqueIdentifier(), self.uniqueIdentifier(), self.uniqueIdentifier(), self.uniqueIdentifier(), self.event.targetViewController.id)
	#		
	#	return ''
	
	def svg(self):
		if self.image <> None:
			image_url = self.image.image.url
			return '<g><title>%s</title><image x=\"%d\" y=\"%d\" width=\"%d\" height=\"%d\" xlink:href=\"%s\" id="%s" /></g>' % (self.name, self.x, self.y, self.width, self.height, image_url, self.uniqueIdentifier())
		else:
			return '<g><title>%s</title><rect id=\"svg_%d\" x=\"%d\" y=\"%d\" width=\"%d\" height=\"%d\" fill=\"%s\"/></g>' % (self.name, self.id, self.x, self.y, self.width, self.height, self.color)

	def __unicode__(self):              
		return self.name

class Button(View):
	parent = models.ForeignKey(Container, on_delete=models.CASCADE, blank=True, null=True)
	normal = models.ForeignKey(Image, related_name='button_normal', on_delete=models.CASCADE, blank=True, null=True)
	hover = models.ForeignKey(Image, related_name='button_hover', on_delete=models.CASCADE, blank=True, null=True)
	pressed = models.ForeignKey(Image, related_name='button_pressed', on_delete=models.CASCADE, blank=True, null=True)
	
	def uniqueIdentifier(self):
		if self.viewController <> None:
			return 'vc%dview%d' % (self.viewController.id, self.id)
		
		return '%sview%d' % (self.parent.uniqueIdentifier(), self.id)
	
	def svg(self):
		return 'svg: %s' % self.name
		
