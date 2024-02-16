
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.order_online, name='order_online'),

]
