from django.conf.urls import patterns, url

urlpatterns = patterns('apps.oficina.views',
						url(r'^$', 'Index_view', name='index'),
						)
						