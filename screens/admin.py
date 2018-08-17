# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import *

admin.site.register(Project)
admin.site.register(Screen)
admin.site.register(Layer)
admin.site.register(ScreenRelation)
