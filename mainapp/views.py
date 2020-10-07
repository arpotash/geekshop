from django.shortcuts import render, get_object_or_404
from geekshop import settings
from mainapp.models import Product, CategoryProduct
import json
import os

links = CategoryProduct.objects.all()


def main(request, pk=None):
    if pk == None:
        products = Product.objects.all()[:9]
    else:
        category = get_object_or_404(CategoryProduct, pk=pk)
        products = Product.objects.filter(category=category)
    content = {
        'products': products,
        'links': links,
    }
    return render(request, 'mainapp/index.html', content)


def description(request, pk=None):
    print(pk)
    content = {
        'links': links,
    }
    return render(request, 'mainapp/description.html', content)


def about(request):
    content = {
    }
    return render(request, 'mainapp/aboutUs.html', content)
