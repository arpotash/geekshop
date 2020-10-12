from django.urls import include, path

import basketapp.views as basketapp

app_name = 'basketapp'

urlpatterns = [
    path('', basketapp.basket, name='basket_list'),
    path('add:<pk>', basketapp.add, name='add'),
    path('remove:<pk>', basketapp.remove_basket, name='remove'),
    path('edit/<int:pk>/<int:quantity>/', basketapp.basket_edit, name='edit')
]