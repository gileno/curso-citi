# coding=utf-8

from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage
from django.http import Http404

from .models import Product, Category


def index(request):
    products = Product.objects.approved()
    q = request.GET.get('q', None)
    if q:
        products = products.filter(name__icontains=q)
    paginator = Paginator(products, 3)
    try:
        page_number = int(request.GET.get('page', 1))
        page_obj = paginator.page(page_number)
    except (ValueError, EmptyPage):
        raise Http404
    context = {
        'products': page_obj.object_list,
        'page_obj': page_obj,
        'paginator': paginator,
    }
    return render(request, 'catalog/index.html', context)


def category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    context = {
        'category': category,
        'products': Product.objects.approved().filter(category=category)
    }
    return render(request, 'catalog/category.html', context)


def product(request, slug):
    product = get_object_or_404(Product.objects.approved(), slug=slug)
    context = {
        'product': product
    }
    return render(request, 'catalog/product.html', context)
