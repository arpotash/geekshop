from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
import mainapp.views as mainapp

app_name = 'mainapp'

urlpatterns = [
    path('', mainapp.main, name='index'),
    path('category/<int:pk>/', mainapp.main, name='category'),
    path('catalog/', mainapp.catalog, name='catalog'),
    path('<page>', mainapp.main, name='page'),
]