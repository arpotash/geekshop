import random
from random import randint

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, TemplateView

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
    _product = Product.objects.filter(is_active=True)
    hot_list = list(random.sample(list(_product), 2))
    return hot_list


class ProductsList(ListView):
    model = Product
    template_name = 'mainapp/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'главная'
        context['hot_products'] = hot_products()
        context['links'] = links
        return context


class ProductsInCategory(ListView):
    model = Product
    template_name = 'mainapp/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['hot_products'] = hot_products()
        context['links'] = links
        context['category'] = self.kwargs
        return context

    def get_queryset(self):
        return Product.objects.filter(category_id=self.kwargs['pk'])


class Catalog(ListView):
    model = Product
    template_name = 'mainapp/catalog.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'каталог'
        context['links'] = links
        return context

    def get_queryset(self):
        return Product.objects.filter(is_active=True)


class ProductObject(ListView):
    model = Product
    template_name = 'mainapp/product.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['links'] = links
        context['product'] = get_object_or_404(Product, pk=self.kwargs['pk'])
        return context


class About(TemplateView):
    template_name = 'mainapp/aboutUs.html'
