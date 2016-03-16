from django.conf.urls import patterns, url
from .views import Visitante_views, UsuariosA_views, OficinaA_views, CreateVisitante, VisitanteEdit, VisitanteDelete, CreateOficina, CreateVisitante, OficinaEdit
#from apps.administrador import views

urlpatterns = patterns('apps.administrador.views',
				url(r'^$', 'Index_view', name='p_inicio'),
				url(r'^visitante/$', Visitante_views, name='p_visitante'),
				url(r'^oficina/$', OficinaA_views, name='p_oficina'),
				url(r'^usuarios/$', UsuariosA_views, name='p_usuarios'),
				url(r'^oficina/nuevo/$', CreateOficina.as_view(), name='po_nuevo'),
				url(r'^oficina/editar/(?P<pk>\d+)$', OficinaEdit.as_view, name='Oeditar'),
				#url(r'^panel/evento/editar/(?P<pk>\d+)$', EventEdit.as_view(), name='editar'),
				url(r'^visitante/editar/(?P<pk>\d+)$', VisitanteEdit.as_view(), name='po_editar'),
				url(r'^visitante/nuevo/$', CreateVisitante.as_view(), name='pv_nuevo'),
				
						)
						