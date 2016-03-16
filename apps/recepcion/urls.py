from django.conf.urls import patterns, url
from .views import CreateVisitante, VisitanteEdit, VisitanteDelete
from apps.recepcion import views

urlpatterns = patterns('apps.recepcion.views',
					#	url(r'^$', 'Index_view', name='index'),
						url(r'^$', views.Visitante_views, name='p_visitante'),
						url(r'^editar/(?P<pk>\d+)$', VisitanteEdit.as_view(), name='po_editar'),
						url(r'^nuevo/$', CreateVisitante.as_view(), name='r_nuevo'),
						#url(r'^con_ajax_post/$',views.lista_visitantes),
						url(r'^reportes/$',views.pdf, name='r_reportes'),
						)
						