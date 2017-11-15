from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^index$', views.index, name='index'),
    url(r'^folder/(?P<folder_name>.+)/$', views.folder, name='folder'),
    url(r'^images/(?P<folder_name>.+)/(?P<image_name>.+).png$', views.image, name='image'),
]