"""sirecovi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from apps.administrador import views

urlpatterns = [
    url(r'^$', views.Index_principal),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^administrador/', include('apps.administrador.urls', namespace="administrador_app")),
    url(r'^recepcion/', include('apps.recepcion.urls', namespace="recepcion_app")),
    url(r'^oficina/', include('apps.oficina.urls', namespace="oficina_app")),
    url(r'^', include('apps.users.urls', namespace="users_app")),

]
