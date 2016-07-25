# coding=utf-8

from django.test import TestCase, Client
from django.core.urlresolvers import reverse


class ViewsTestCase(TestCase):

    def setUp(self):
        self.url_index = reverse('index')
        self.url_contact = reverse('contact')
        self.client = Client()

    def test_index_view(self):
        response = self.client.get(self.url_index)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_index_contact(self):
        response = self.client.get(self.url_contact)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact.html')
