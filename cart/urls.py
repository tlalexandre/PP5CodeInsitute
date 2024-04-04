from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.cart, name='cart'),
    path('add_to_cart/', views.add_to_cart, name='add_to_cart'),
    path('cart/delete/<int:item_index>/',
         views.delete_from_cart, name='delete_from_cart'),
    path('cart/update/<int:item_index>/',
         views.update_cart_item, name='update_cart_item'),
]
