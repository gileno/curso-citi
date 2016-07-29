# coding=utf-8

from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage
from django.views.generic import ListView, DetailView
from django.http import Http404

from .models import Product, Category


class IndexView(ListView):

    paginate_by = 3
    context_object_name = 'products'
    template_name = 'catalog/index.html'

    def get_queryset(self):
        products = Product.objects.approved()
        q = self.request.GET.get('q', None)
        if q:
            products = products.filter(name__icontains=q)
        return products


def category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    context = {
        'category': category,
        'products': Product.objects.approved().filter(category=category)
    }
    return render(request, 'catalog/category.html', context)


class ProductDetailView(DetailView):

    template_name = 'catalog/product.html'
    context_object_name = 'product'
    queryset = Product.objects.approved()
