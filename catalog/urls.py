# coding=utf-8

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^categorias/([\w_-]+)/$', views.category, name='category'),
    url(r'^produtos/(?P<slug>[\w_-]+)/$', views.ProductDetailView.as_view(), name='product'),
]
