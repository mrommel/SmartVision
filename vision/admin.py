# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import *

admin.site.register(Project)
admin.site.register(ViewController)
admin.site.register(Image)

"""
	container can be saved as
"""
class ContainerAdmin(admin.ModelAdmin):
    save_as=True
    
admin.site.register(Container, ContainerAdmin)

"""
	label can be saved as
"""
class LabelAdmin(admin.ModelAdmin):
    save_as=True
    
admin.site.register(Label, LabelAdmin)

admin.site.register(ImageView)
admin.site.register(Button)

"""
	action can be saved as
"""
class ActionAdmin(admin.ModelAdmin):
    save_as=True
    
admin.site.register(Action, ActionAdmin)