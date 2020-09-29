from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
import mainapp.views as mainapp

app_name = 'mainapp'

urlpatterns = [
    path('', mainapp.main, name='index'),
    path('<int:pk>/', mainapp.main, name='category'),
]