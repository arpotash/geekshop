from django.urls import path

import adminapp.views as adminapp

app_name = 'adminapp'

urlpatterns = [
    path('', adminapp.TemplateAdminPage.as_view(), name='admin_page'),
    path('users/create', adminapp.UserCreateView.as_view(), name='user_create'),
    path('users/delete/<pk>', adminapp.UserDeleteView.as_view(), name='user_delete'),
    path('users/read/', adminapp.UserListView.as_view(), name='user_read'),
    path('users/read/<page>/', adminapp.UserListView.as_view(), name='user_page'),
    path('users/update/<pk>', adminapp.UserUpdateView.as_view(), name='user_update'),

    path('products/create/', adminapp.ProductCreateView.as_view(), name='product_create'),
    path('product/delete/<pk>', adminapp.ProductDeleteView.as_view(), name='product_delete'),
    path('product/read', adminapp.ProductListView.as_view(), name='products_read'),
    path('product/read/<page>/', adminapp.ProductListView.as_view(), name='products_page'),
    path('product/category/<pk>/', adminapp.ProductInCategoryListView.as_view(), name='products_in_category_read'),
    path('product/category/read/<pk>/<page>', adminapp.ProductInCategoryListView.as_view(), name='products_in_category_page'),
    path('product/update/<pk>', adminapp.ProductUpdateView.as_view(), name='product_update'),

    path('category/create', adminapp.ProductCategoryCreateView.as_view(), name='category_create'),
    path('category/delete<pk>', adminapp.ProductCategoryDeleteView.as_view(), name='category_delete'),
    path('category/read/', adminapp.ProductCategoryListView.as_view(), name='category_read'),
    path('category/read/<page>/', adminapp.ProductCategoryListView.as_view(), name='category_page'),
    path('category/update/<pk>', adminapp.ProductCategoryUpdateView.as_view(), name='category_update'),
]