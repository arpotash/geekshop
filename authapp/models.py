from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class ShopUser(AbstractUser):
    username = models.CharField(verbose_name='Логин', max_length=64, unique=True)
    first_name = models.CharField(verbose_name='Имя', max_length=64)
    email = models.CharField(verbose_name='Email', max_length=64)
    avatar = models.ImageField(upload_to='users_avatar', blank=True, verbose_name='Аватарка')
    age = models.PositiveSmallIntegerField(verbose_name='Возраст')