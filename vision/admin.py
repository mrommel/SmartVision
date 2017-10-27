# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import *

admin.site.register(Project)
admin.site.register(ViewController)
admin.site.register(Image)

admin.site.register(Container)
admin.site.register(Label)
admin.site.register(ImageView)
admin.site.register(Button)