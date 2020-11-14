from django.urls import include, path

import basketapp.views as basketapp

app_name = 'basketapp'

urlpatterns = [
    path('', basketapp.basket, name='basket_list'),
    path('add:<pk>', basketapp.add, name='add'),
    path('remove:<pk>', basketapp.remove_basket, name='remove'),
    path('editminus/<int:pk>/', basketapp.basket_edit_minus, name='editminus'),
    path('editplus/<int:pk>/', basketapp.basket_edit_plus, name='editplus')
]