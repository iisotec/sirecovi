from django.conf.urls import patterns, url
from .views import CreateOficina, OficinaEdit, OficinaDelete, CreateOficina,Estado_atencion_ajax
from apps.oficina import views

urlpatterns = patterns('apps.oficina.views',
						#url(r'^$', 'Index_view', name='index'),
						url(r'^$', views.Oficina_views, name='ap_oficina'),
						url(r'^oficina/nuevo/$', CreateOficina.as_view(), name='apo_nuevo'),
						url(r'^oficina/estado_atencion_ajax/$', Estado_atencion_ajax),

						)
						