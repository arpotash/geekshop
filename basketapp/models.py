from django.db import models

# Create your models here.
from geekshop.settings import AUTH_USER_MODEL
from mainapp.models import Product


class Basket(models.Model):
    objects = models.Manager()
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='пользователь')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='продукт')
    quantity = models.PositiveIntegerField(verbose_name='количество', default=0)
    data_create = models.DateTimeField(verbose_name='время', auto_now_add=True)