from django.urls import path

import orderapp.views as orderapp
app_name = 'orderapp'

urlpatterns = [
    path('', orderapp.OrderListView.as_view(), name='order_list'),
    path('read/<pk>', orderapp.OrderRead.as_view(), name='order_read'),
    path('create/', orderapp.OrderItemCreate.as_view(), name='order_create'),
    path('update/<pk>', orderapp.OrderItemUpdate.as_view(), name='order_update'),
    path('delete/<pk>', orderapp.OrderItemDelete.as_view(), name='order_delete'),
    path('complete/<pk>', orderapp.order_forming_complete, name='order_complete')
]