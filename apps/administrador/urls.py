from django.conf.urls import patterns, url
from .views import CreateVisitante, VisitanteEdit, VisitanteDelete, CreateOficina
from apps.administrador import views

urlpatterns = patterns('apps.administrador.views',
				url(r'^$', 'Index_view', name='p_inicio'),
				url(r'^visitante/$', views.Visitante_views, name='p_visitante'),
				url(r'^oficina/$', views.Oficina_views, name='p_oficina'),
				url(r'^oficina/nuevo/$', CreateOficina.as_view(), name='po_nuevo'),
				url(r'^visitante/editar/(?P<pk>\d+)$', VisitanteEdit.as_view(), name='po_editar'),
						)
						