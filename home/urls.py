
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name='home'),
  path('about/', views.about, name='about'),
  path('menu/', views.menu, name='menu'),
  path('contact/', views.contact, name='contact'),
  path('contact_success/', views.contact_success, name='contact_success'),
]
