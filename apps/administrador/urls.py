from django.conf.urls import patterns, url

urlpatterns = patterns('apps.administrador.views',
						url(r'^$', 'Index_view', name='index'),
						url(r'^control/$', 'Visitante', name='visitante'),
						url(r'^control/$', 'Oficina', name='oficina'),
						)
						