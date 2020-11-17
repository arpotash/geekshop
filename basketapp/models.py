from django.db import models

# Create your models here.
from geekshop.settings import AUTH_USER_MODEL
from mainapp.models import Product, CategoryProduct


class Basket(models.Model):
    objects = models.Manager()
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='пользователь', related_name='basket')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='продукт')
    quantity = models.PositiveIntegerField(verbose_name='количество', default=0)
    data_create = models.DateTimeField(verbose_name='время', auto_now_add=True)

    @staticmethod
    def get_items(user):
        return Basket.objects.filter(user=user).order_by('product__category')

    @property
    def product_cost(self):
        return self.product.price * self.quantity

    @property
    def total_quantity(self):
        _items = Basket.objects.filter(user=self.user)
        _total_quantity = sum(list(map(lambda x: x.quantity, _items)))
        return _total_quantity

    @property
    def total_cost(self):
        _items = Basket.objects.filter(user=self.user)
        _total_cost = sum(list(map(lambda x: x.product_cost, _items)))
        return _total_cost