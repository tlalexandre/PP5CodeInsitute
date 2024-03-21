
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.order_online, name='order_online'),\
    path('item/<int:item_id>/', views.item_detail, name='item_detail'),
    path('product_management/', views.product_management, name='product_management'),
    path('add/', views.add_item, name='add_item'),
    path('edit/<int:item_id>/', views.edit_item, name='edit_item'),
]
