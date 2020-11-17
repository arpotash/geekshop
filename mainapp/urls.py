from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
import mainapp.views as mainapp

app_name = 'mainapp'

urlpatterns = [
    path('', mainapp.ProductsList.as_view(), name='index'),
    path('category/<int:pk>/', mainapp.ProductsInCategory.as_view(), name='category'),
    path('catalog/', mainapp.Catalog.as_view(), name='catalog'),
]