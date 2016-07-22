# coding=utf-8

from django.db import models


class Category(models.Model):

    name = models.CharField('Nome', max_length=100)
    slug = models.SlugField('Slug')

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.name


class Product(models.Model):

    name = models.CharField('Nome', max_length=100)
    slug = models.SlugField('Slug')
    category = models.ForeignKey(Category, verbose_name='Categoria')
    description = models.TextField('Descrição', blank=True)

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'

    def __str__(self):
        return self.name
