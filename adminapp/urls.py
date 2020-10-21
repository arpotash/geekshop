from django.urls import path

import adminapp
import adminapp.views as adminapp

app_name = 'adminapp'

urlpatterns = [
    path('', adminapp.render_admin_page, name='admin_page'),
    path('users/create', adminapp.user_create, name='user_create'),
    path('users/delete/<pk>', adminapp.user_delete, name='user_delete'),
    path('users/read/', adminapp.user_read, name='user_read'),
    path('users/update/<pk>', adminapp.user_update, name='user_update'),

    path('products/create/', adminapp.product_create, name='product_create'),
    path('product/delete/<pk>', adminapp.product_delete, name='product_delete'),
    path('product/read', adminapp.products_read, name='products_read'),
    path('product/category/read/<pk>', adminapp.product_in_category_read, name='products_in_category_read'),
    path('product/update/<pk>', adminapp.product_update, name='product_update'),

    path('category/create', adminapp.category_create, name='category_create'),
    path('category/delete<pk>', adminapp.category_delete, name='category_delete'),
    path('category/read/', adminapp.category_read, name='category_read'),
    path('category/update/<pk>', adminapp.category_update, name='category_update'),
]