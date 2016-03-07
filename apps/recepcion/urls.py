from django.conf.urls import patterns, url

urlpatterns = patterns('apps.recepcion.views',
						url(r'^$', 'Index_view', name='index'),
						)
						