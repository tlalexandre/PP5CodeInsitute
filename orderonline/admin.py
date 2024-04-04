from django.contrib import admin
from .models import (
    MenuCategory, MenuItem, MenuItemIngredient,
    Ingredient, MenuItemIncludedItem, IngredientOption
)


class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price')
    list_filter = ('category',)


class MenuItemIngredientAdmin(admin.ModelAdmin):
    list_display = (
        'menu_item',
        'ingredient',
        'price',
        'option',
        'is_optional')


class MenuItemIngredientInline(admin.TabularInline):
    model = MenuItemIngredient
    extra = 1


class IngredientOptionAdmin(admin.ModelAdmin):
    inlines = [MenuItemIngredientInline]


admin.site.register(IngredientOption, IngredientOptionAdmin)
admin.site.register(MenuCategory)
admin.site.register(MenuItem, MenuItemAdmin)
admin.site.register(MenuItemIngredient, MenuItemIngredientAdmin)
admin.site.register(Ingredient)
admin.site.register(MenuItemIncludedItem)
