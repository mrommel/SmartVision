# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import *

# Register your models here.

class ImageAdmin(admin.ModelAdmin):
	list_display = ('filename', 'title', 'folder', 'thumbnail', 'tag_list', 'detail_link',)
	
	fields = ('filename', 'title', 'folder', 'detailed', 'tags', 'related', 'detail_link', )
	readonly_fields = ('detailed', 'detail_link')

admin.site.register(Tag)
admin.site.register(Image, ImageAdmin)
