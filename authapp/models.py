from datetime import timedelta

from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
from django.utils.timezone import now


class ShopUser(AbstractUser):
    username = models.CharField(verbose_name='Логин', max_length=64, unique=True)
    first_name = models.CharField(verbose_name='Имя', max_length=64)
    email = models.CharField(verbose_name='Email', max_length=64)
    avatar = models.ImageField(upload_to='users_avatar', blank=True, verbose_name='Аватарка')
    age = models.PositiveSmallIntegerField(verbose_name='Возраст')
    is_active = models.BooleanField(default=True)
    activation_key = models.CharField(max_length=128, blank=True)
    activation_key_expires = models.DateTimeField(default=(now() + timedelta(hours=48)))

    def is_activation_key_expired(self):
        if self.activation_key_expires <= now():
            return True
        else:
            return False
