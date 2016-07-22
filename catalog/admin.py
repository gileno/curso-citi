from django.contrib import admin

from .models import Category, Product


class CategoryAdmin(admin.ModelAdmin):

    list_display = ['name', 'slug']
    search_fields = ['name', 'slug']


class ProductAdmin(admin.ModelAdmin):

    list_display = ['name', 'slug', 'category']
    search_fields = ['name', 'slug', 'category__name']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
