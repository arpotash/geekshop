import json
from django.conf import settings
from django.core.management import BaseCommand
import os
from authapp.models import ShopUser
from mainapp.models import Product, CategoryProduct

FILE_PATH = 'mainapp/json'


def load_from_json(filename):
    with open(os.path.join(FILE_PATH, filename + '.json'), encoding='utf-8') as json_file:
        return json.load(json_file)


class Command(BaseCommand):

    def handle(self, *args, **options):
        categories = load_from_json("categories")
        CategoryProduct.objects.all().delete()
        for category in categories:
            CategoryProduct.objects.create(**category)

        products = load_from_json("products")
        Product.objects.all().delete()
        for product in products:
            category_name = product['category']
            _category = CategoryProduct.objects.get(name=category_name)
            product['category'] = _category
            Product.objects.create(**product)

        ShopUser.objects.create_superuser(username='django', password='geekbrains', age='30')