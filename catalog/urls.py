# coding=utf-8

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^categorias/([\w_-]+)/$', views.category, name='category'),
    url(r'^produtos/([\w_-]+)/$', views.product, name='product'),
]
