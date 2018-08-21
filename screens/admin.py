# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import *

class LayerInLine(admin.TabularInline):
    model = ScreenLayerRelation
    extra = 0

class ScreenAdmin(admin.ModelAdmin):
    list_display = ('name', 'layout', 'layer_list')
 
    inlines = [
        LayerInLine
    ]
 
    def layer_list(self, obj):
        return obj.layers().count()

class ScreenInLine(admin.TabularInline):
    model = LayoutScreenRelation
    extra = 0
    
class LayoutAdmin(admin.ModelAdmin):
    list_display = ('name', 'project', 'screen_list')
 
    inlines = [
        ScreenInLine
    ]
 
    def screen_list(self, obj):
        return obj.screens().count()

admin.site.register(Project)
admin.site.register(Layout, LayoutAdmin)
admin.site.register(Screen, ScreenAdmin)
admin.site.register(Layer)
admin.site.register(ScreenLayerRelation)
admin.site.register(LayoutScreenRelation)
admin.site.register(LayoutRow)
