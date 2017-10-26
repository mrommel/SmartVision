from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^index$', views.index, name='index'),
    url(r'^projects$', views.projects, name='projects'),
    url(r'^project/(?P<project_id>\d+)$', views.project, name='project'),
    url(r'^controller/(?P<controller_id>\d+)$', views.controller, name='controller'),
    url(r'^controller_image/(?P<controller_id>\d+)/image.svg$', views.controller_image, name='controller_image'),
]