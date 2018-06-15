from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^index$', views.index, name='index'),
    url(r'^folder/(?P<folder_name>.+)/$', views.folder, name='folder'),
    url(r'^detail/(?P<identifier>.+)/$', views.detail, name='detail'),
    url(r'^tag/(?P<tag_id>.+)/$', views.tag, name='tag'),
    
    # image urls
    url(r'^images/(?P<identifier>.+).png$', views.image_png, name='image_png'),
    url(r'^images/(?P<identifier>.+).jpg$', views.image_jpg, name='image_jpg'),
    url(r'^images/(?P<identifier>.+).svg$', views.image_svg, name='image_svg'),
    url(r'^images/(?P<identifier>.+).pdf$', views.image_pdf, name='image_pdf'),
    url(r'^images/(?P<identifier>.+).eps$', views.image_eps, name='image_eps'),
    
]