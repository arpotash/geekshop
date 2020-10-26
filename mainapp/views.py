import random
from random import randint

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404

from basketapp.models import Basket
from geekshop import settings
from mainapp.models import Product, CategoryProduct
import json
import os

links = CategoryProduct.objects.all()


def get_basket(user):
    basket = []
    if user.is_authenticated:
        basket = Basket.objects.filter(user=user)
    return basket


def hot_products():
    _product = Product.objects.all()
    hot_list = list(random.sample(list(_product), 2))
    return hot_list


def main(request, pk=None, page=1):
    title = 'главная'
    if pk is None:
        products = Product.objects.all()[:9]
        category = ''
    else:
        category = get_object_or_404(CategoryProduct, pk=pk)
        products = Product.objects.filter(category=category)
    paginator = Paginator(products, 2)
    try:
        products_paginator = paginator.page(page)
    except PageNotAnInteger:
        products_paginator = paginator.page(1)
    except EmptyPage:
        products_paginator = paginator.page(paginator.num_pages)
    hot_product = hot_products()

    content = {
        'title': title,
        'products': products_paginator,
        'category': category,
        'links': links,
        'basket': get_basket(request.user),
        'hot_product': hot_product,
    }
    return render(request, 'mainapp/index.html', content)


def catalog(request):
    title = 'каталог'
    _catalog = Product.objects.all()
    content = {'title': title, 'catalog': _catalog, 'links': links, 'basket': get_basket(request.user)}
    return render(request, 'mainapp/catalog.html', content)


def product(request, pk=None):
    _product = get_object_or_404(Product, pk=pk)
    content = {
        'links': links,
        'product': _product,
        'basket': get_basket(request.user)
    }
    return render(request, 'mainapp/product.html', content)


def about(request):
    content = {
        'basket': get_basket(request.user),
    }
    return render(request, 'mainapp/aboutUs.html', content)
