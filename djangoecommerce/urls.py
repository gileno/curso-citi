# coding=utf-8

from django.conf.urls import url, include
from django.contrib import admin

from core.views import index, contact


urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^contato/$', contact, name='contact'),
    url(r'^catalogo/', include('catalog.urls', namespace='catalog')),
    url(r'^admin/', admin.site.urls),
]
