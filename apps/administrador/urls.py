from django.conf.urls import patterns, url
from .views import CreateUsuario,Visitante_views, UsuariosA_views, OficinaA_views, CreateVisitante, VisitanteEdit, VisitanteDelete, CreateOficina, CreateVisitante, OficinaEdit, BusquedaOficinasAjax, Oficina_ajax, Index_view, OficinaDelete
#from apps.administrador import views

urlpatterns = patterns('',
				url(r'^$', Index_view, name='p_inicio'),
				url(r'^visitante/$', Visitante_views, name='p_visitante'),
				url(r'^oficina/$', OficinaA_views, name='p_oficina'),
				url(r'^usuarios/$', UsuariosA_views, name='p_usuarios'),
				url(r'^usuarios/nuevo/$', CreateUsuario.as_view(), name='pu_nuevo'),
				url(r'^oficina/nuevo/$', CreateOficina.as_view(), name='po_nuevo'),
				url(r'^oficina/editar/(?P<pk>\d+)$', OficinaEdit.as_view(), name='o_editar'),
				url(r'^oficina/eliminar/(?P<pk>\d+)$', OficinaDelete.as_view(), name='o_eliminar'),
				url(r'^visitante/nuevo/$', CreateVisitante.as_view(), name='pv_nuevo'),
				url(r'^visitante/listarOficinas-ajax/$', BusquedaOficinasAjax.as_view()),
				url(r'^busqueda_ajax/$', Oficina_ajax),
				)
						