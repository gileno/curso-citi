# coding=utf-8

from django.shortcuts import render, get_object_or_404

from .models import Product, Category


def index(request):
    context = {
        'products': Product.objects.all(),
    }
    return render(request, 'catalog/index.html', context)


def category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    context = {
        'category': category,
        'products': Product.objects.filter(category=category)
    }
    return render(request, 'catalog/category.html', context)


def product(request, slug):
    product = get_object_or_404(Product, slug=slug)
    context = {
        'product': product
    }
    return render(request, 'catalog/product.html', context)
