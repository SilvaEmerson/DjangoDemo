from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.rests_list, name='rests_list'),
    url(r'^new/$', views.restaurant_new, name='restaurant_new'),
    url(r'^edit/(?P<pk>[0-9]+)/$', views.restaurant_edit,
        name='restaurant_edit'),
    url(r'^del/(?P<pk>[0-9]+)/$', views.restaurant_delete,
        name='restaurant_delete')
]
