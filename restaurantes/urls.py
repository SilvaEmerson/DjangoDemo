from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.rests_list, name='rests_list'),
    url(r'^new/$', views.restaurant_new, name='restaurant_new'),
    url(r'^edit/(?P<pk>[0-9]+)/$', views.restaurant_edit,
        name='restaurant_edit'),
    url(r'^del/(?P<pk>[0-9]+)/$', views.restaurant_delete,
        name='restaurant_delete'),
    url(r'^addfeed/(?P<pk>[0-9]+)/$', views.do_feedback,
        name='add_feedback'),
    url(r'^vote0/(?P<pk>[0-9]+)/$', views.vote0, name='vote0'),
    url(r'^vote1/(?P<pk>[0-9]+)/$', views.vote1, name='vote1'),
    url(r'^vote2/(?P<pk>[0-9]+)/$', views.vote2, name='vote2'),
    url(r'^vote3/(?P<pk>[0-9]+)/$', views.vote3, name='vote3'),
    url(r'^vote4/(?P<pk>[0-9]+)/$', views.vote4, name='vote4')
]
