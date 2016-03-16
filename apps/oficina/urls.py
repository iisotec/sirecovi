from django.conf.urls import patterns, url
from .views import CreateOficina, OficinaEdit, OficinaDelete, CreateOficina
from apps.oficina import views

urlpatterns = patterns('apps.oficina.views',
						#url(r'^$', 'Index_view', name='index'),
						url(r'^$', views.Oficina_views, name='ap_oficina'),
						url(r'^oficina/nuevo/$', CreateOficina.as_view(), name='apo_nuevo'),

						)
						