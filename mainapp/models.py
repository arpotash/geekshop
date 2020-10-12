from django.db import models


# Create your models here.


class CategoryProduct(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=64, unique=True, verbose_name='Название')
    description = models.TextField(max_length=64, blank=True, verbose_name='Описание')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Product(models.Model):
    small_size = '15'
    normal_size = '16'
    big_size = '17'
    biggest_size = '18'
    sizes = [
        (small_size, '15'),
        (normal_size, '16'),
        (big_size, '17'),
        (biggest_size, '18'),
    ]
    objects = models.Manager()
    name = models.CharField(max_length=64, verbose_name='Название')
    category = models.ForeignKey(CategoryProduct, on_delete=models.CASCADE, verbose_name='Категория')
    price = models.DecimalField(verbose_name='Цена', max_digits=8, decimal_places=2, default=0)
    description = models.TextField(max_length=512, blank=True, verbose_name='Описание')
    image = models.ImageField(upload_to='products_image', blank=True, verbose_name='Картинка')
    size = models.CharField(max_length=4, choices=sizes)
    quantity = models.PositiveSmallIntegerField(verbose_name='Количество')

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return f'{self.name} ({self.category.name})'
