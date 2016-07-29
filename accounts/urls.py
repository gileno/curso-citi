# coding=utf-8

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^alterar-dados/$', views.edit, name='edit'),
    url(r'^alterar-senha/$', views.PasswordChangeView.as_view(), name='password_change'),
    url(r'^cadastro/$', views.register, name='register'),
]
