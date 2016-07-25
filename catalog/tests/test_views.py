# coding=utf-8

from django.test import TestCase, Client
from django.core.urlresolvers import reverse

from model_mommy import mommy

from catalog.models import Product, Category


class IndexViewTestCase(TestCase):

    def setUp(self):
        mommy.make(Product, _quantity=10)

    def tearDown(self):
        Category.objects.all().delete()
        Product.objects.all().delete()

    def test_view_ok(self):
        client = Client()
        catalog_index_url = reverse('catalog:index')
        response = client.get(catalog_index_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'catalog/index.html')
        products = response.context['products']
        self.assertEquals(products.count(), 10)


class CategoryViewTestCase(TestCase):

    def setUp(self):
        category1 = mommy.make(Category, slug='teste1')
        category2 = mommy.make(Category, slug='teste2')
        mommy.make(Product, category=category1, _quantity=10)

    def tearDown(self):
        Category.objects.all().delete()
        Product.objects.all().delete()

    def test_view_ok(self):
        client = Client()
        category_url = reverse('catalog:category', args=['teste1'])
        response = client.get(category_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'catalog/category.html')
        products = response.context['products']
        self.assertEquals(products.count(), 10)

    def test_view_not_found(self):
        client = Client()
        category_url = reverse('catalog:category', args=['teste3'])
        response = client.get(category_url)
        self.assertEquals(response.status_code, 404)
