from datetime import timedelta

from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.timezone import now


class ShopUser(AbstractUser):
    username = models.CharField(verbose_name='Логин', max_length=64, unique=True)
    first_name = models.CharField(verbose_name='Имя', max_length=64)
    email = models.CharField(verbose_name='Email', max_length=64)
    avatar = models.ImageField(upload_to='users_avatar', blank=True, verbose_name='Аватарка')
    age = models.PositiveSmallIntegerField(verbose_name='Возраст', default=18)
    is_active = models.BooleanField(default=True)
    activation_key = models.CharField(max_length=128, blank=True)
    activation_key_expires = models.DateTimeField(default=(now() + timedelta(hours=48)))

    def is_activation_key_expired(self):
        if self.activation_key_expires <= now():
            return True
        else:
            return False


class ShopUserProfile(models.Model):
    MALE = 'M'
    FEMALE = 'W'
    GENDER = (
        (MALE, 'М'),
        (FEMALE, 'Ж'),
    )
    objects = models.Manager()
    user = models.OneToOneField(ShopUser, primary_key=True, null=False, db_index=True, on_delete=models.CASCADE)
    tagline = models.CharField(verbose_name='теги', max_length=128, blank=True)
    aboutMe = models.TextField(verbose_name='о себе', max_length=512, blank=True)
    gender = models.CharField(verbose_name='пол', max_length=1, choices=GENDER, blank=True)

    @receiver(post_save, sender=ShopUser)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            ShopUserProfile.objects.create(user=instance)

    @receiver(post_save, sender=ShopUser)
    def save_user_profile(sender, instance, **kwargs):
        instance.shopuserprofile.save()