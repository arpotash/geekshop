from django.db import transaction
from django.forms import formset_factory, inlineformset_factory
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView

from basketapp.models import Basket
from orderapp.forms import OrderItemForm
from orderapp.models import Order, OrderItem


class OrderListView(ListView):
    model = Order

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)


class OrderItemCreate(CreateView):
    model = Order
    fields = []
    success_url = reverse_lazy('orderapp:order_list')

    def get_context_data(self, **kwargs):
        context = super(OrderItemCreate, self).get_context_data(**kwargs)
        order_item_formset = inlineformset_factory(Order, OrderItem, form=OrderItemForm, extra=1)
        if self.request.POST:
            formset = order_item_formset(self.request.POST)
        else:
            basket_item = Basket.get_items(self.request.user)
            if len(basket_item):
                order_item_formset = inlineformset_factory(Order, OrderItem, form=OrderItemForm, extra=len(basket_item))
                formset = order_item_formset()
                for num, form in enumerate(formset.forms):
                    form.initial['product'] = basket_item[num].product
                    form.initial['quantity'] = basket_item[num].quantity
                basket_item.delete()
            else:
                formset = order_item_formset()
        context['orderitems'] = formset
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        orderitems = context['orderitems']
        form.instance.user = self.request.user
        self.object = form.save()
        if orderitems.is_valid():
            orderitems.instance = self.object
            orderitems.save()

        if self.object.get_total_cost() == 0:
            self.object.delete()
        return super(OrderItemCreate, self).form_valid(form)


class OrderItemUpdate(UpdateView):
    model = Order
    fields = []
    success_url = reverse_lazy('orderapp:order_list')

    def get_context_data(self, **kwargs):
        context = super(OrderItemUpdate, self).get_context_data(**kwargs)
        order_item_formset = inlineformset_factory(Order, OrderItem, form=OrderItemForm, extra=1)
        if self.request.POST:
            formset = order_item_formset(self.request.POST, instance=self.object)
        else:
            formset = order_item_formset(instance=self.object)
        context['orderitems'] = formset
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        orderitems = context['orderitems']
        self.object = form.save()
        if orderitems.is_valid():
            orderitems.instance = self.object
            orderitems.save()

        if self.object.get_total_cost() == 0:
            self.object.delete()
        return super(OrderItemUpdate, self).form_valid(form)


class OrderItemDelete(DeleteView):
    model = Order
    success_url = reverse_lazy('orderapp:order_list')


class OrderRead(DetailView):
    model = Order


def order_forming_complete(request, pk):
    order = get_object_or_404(Order, pk=pk)
    order.status = Order.SENT_TO_PROCEED
    order.save()
    return HttpResponseRedirect(reverse('orderapp:order_list'))