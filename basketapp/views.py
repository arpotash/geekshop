from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404


# Create your views here.
from django.template.loader import render_to_string
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView

from basketapp.models import Basket
from mainapp.models import Product
from mainapp.views import get_basket


@login_required
def basket(request):
    title = 'корзина'
    basket_items = Basket.objects.filter(user=request.user).order_by('product__category')
    content = {'title': title, 'basket_items': basket_items, 'basket': get_basket(request.user)}
    return render(request, 'basketapp/basket.html', content)


@login_required
def BasketAdd(request, pk):
    if 'login' in request.META.get('HTTP_REFERER'):
        return HttpResponseRedirect(reverse('product', args=[pk]))
    product = get_object_or_404(Product, pk=pk)
    _basket = Basket.objects.filter(user=request.user, product=product).first()
    if not _basket:
        _basket = Basket(user=request.user, product=product)

    _basket.quantity += 1
    _basket.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def remove_basket(request, pk):
    _basket = get_object_or_404(Basket, pk=pk)
    _basket.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def basket_edit_plus(request, pk):
    if request.is_ajax():
        new_basket_item = Basket.objects.get(pk=int(pk))
        new_basket_item.quantity += 1
        new_basket_item.save()

        basket_items = Basket.objects.filter(user=request.user)

        content = {'basket_items': basket_items}
        result = render_to_string('basketapp/includes/inc_basket_list.html', content)
        print(content)
        return JsonResponse({'result': result})


@login_required
def basket_edit_minus(request, pk):
    if request.is_ajax():
        new_basket_item = Basket.objects.get(pk=int(pk))
        if new_basket_item.quantity > 0:
            new_basket_item.quantity -= 1
            new_basket_item.save()
        else:
            new_basket_item.delete()

        basket_items = Basket.objects.filter(user=request.user)

        content = {'basket_items': basket_items}
        result = render_to_string('basketapp/includes/inc_basket_list.html', content)
        return JsonResponse({'result': result})