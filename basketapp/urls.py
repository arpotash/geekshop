from django.urls import include, path

import basketapp.views as basketapp

app_name = 'basketapp'

urlpatterns = [
    path('', basketapp.basket, name='basket'),
    path('add:<pk>', basketapp.add, name='add'),
]