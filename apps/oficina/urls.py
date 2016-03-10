from django.conf.urls import patterns, url
from .views import CreateOficina, OficinaEdit, OficinaDelete, CreateOficina
from apps.administrador import views

urlpatterns = patterns('apps.oficina.views',
						url(r'^$', 'Index_view', name='index'),
						url(r'^oficina/$', views.Oficina_views, name='p_oficina'),
						url(r'^oficina/nuevo/$', CreateOficina.as_view(), name='po_nuevo'),

						)
						