# coding=utf-8

from django.shortcuts import render

from .models import Product, Category


def index(request):
    context = {
        'products': Product.objects.all(),
    }
    return render(request, 'catalog/index.html', context)
