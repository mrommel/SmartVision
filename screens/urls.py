from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^index$', views.index, name='index'),
    url(r'^project/(?P<project_id>.+)/$', views.project, name='project'),
    url(r'^layout/(?P<layout_id>.+)/$', views.layout, name='layout'),
    
    url(r'^screen/(?P<screen_id>.+)/$', views.screen_svg, name='screen_svg'),
]