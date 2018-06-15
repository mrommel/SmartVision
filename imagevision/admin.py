# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import *

# Register your models here.

class ImageAdmin(admin.ModelAdmin):
    list_display = ('filename', 'folder', 'thumbnail', 'tag_list')

admin.site.register(Tag)
admin.site.register(Image, ImageAdmin)
