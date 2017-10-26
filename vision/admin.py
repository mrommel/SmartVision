# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import View, ViewController

admin.site.register(View)
admin.site.register(ViewController)