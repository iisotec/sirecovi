from django.conf.urls import patterns, url
from apps.administrador import views

urlpatterns = patterns('apps.administrador.views',
						url(r'^$', 'Index_view', name='p_inicio'),
						url(r'^visitante/$', views.Visitante, name='p_visitante'),
						url(r'^oficina/$', views.Oficina, name='p_oficina'),
						)
						