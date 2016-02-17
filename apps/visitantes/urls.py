from django.conf.urls import patterns, url

urlpatterns = patterns('apps.visitantes.views',
						url(r'^$', 'index_view', name='index'),
						)