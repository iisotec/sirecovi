from django.conf.urls import patterns, url
from .views import CreateVisitante, VisitanteRegister, VisitanteDelete, search
from apps.recepcion import views

urlpatterns = patterns('apps.recepcion.views',
					#	url(r'^$', 'Index_view', name='index'),
						url(r'^$', views.Visitante_views.as_view(), name='p_visitante'),
						url(r'^registrar/', VisitanteRegister.as_view(), name='r_registrar'),
						url(r'^nuevo/$', CreateVisitante.as_view(), name='r_nuevo'),
						#url(r'^con_ajax_post/$',views.lista_visitantes),
						url(r'^reportes/$',views.pdf, name='r_reportes'),
						url(r'^busqueda/$', search, name='r_busqueda'),
						#url(r'^registrar/(?P<pk>\d+)$', OficinaEdit.as_view(), name='o_editar'),
				
						)
						