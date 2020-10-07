from django.shortcuts import render
from geekshop import settings
from mainapp.models import Product, CategoryProduct
import json
import os

links = CategoryProduct.objects.all()


def main(request, pk=None):
    print(pk)
    if pk == None:
        products = Product.objects.all()[:9]
    else:
        products = Product.objects.filter(category__pk=pk)[:9]
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
