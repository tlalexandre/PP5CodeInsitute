from django.contrib import admin
from .models import MenuCategory, MenuItem, MenuItemIngredient, Ingredient

admin.site.register(MenuCategory)
admin.site.register(MenuItem)
admin.site.register(MenuItemIngredient)
admin.site.register(Ingredient)