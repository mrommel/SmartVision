from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^index$', views.index, name='index'),
    url(r'^folder/(?P<folder_name>.+)/$', views.folder, name='folder'),
    url(r'^detail/(?P<folder_name>.+)/(?P<image_name>.+)/$', views.detail, name='detail'),
    url(r'^images/(?P<folder_name>.+)/(?P<image_name>.+).png$', views.image, name='image'),
    url(r'^images/(?P<folder_name>.+)/(?P<image_name>.+).svg$', views.image_svg, name='image_svg'),
    url(r'^images/(?P<folder_name>.+)/(?P<image_name>.+).pdf$', views.image_pdf, name='image_pdf'),
    url(r'^images/(?P<folder_name>.+)/(?P<image_name>.+).eps$', views.image_eps, name='image_eps'),
]