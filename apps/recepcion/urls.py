from django.conf.urls import patterns, url
from .views import CreateVisitante, VisitanteEdit, VisitanteDelete
from apps.recepcion import views

urlpatterns = patterns('apps.recepcion.views',
						url(r'^$', 'Index_view', name='index'),
						url(r'^recepcion/$', views.Visitante_views, name='p_visitante'),
						url(r'^recepcion/editar/(?P<pk>\d+)$', VisitanteEdit.as_view(), name='po_editar'),
						)
						