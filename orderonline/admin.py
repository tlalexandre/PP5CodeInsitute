from django.contrib import admin
from .models import (
    MenuCategory, MenuItem, MenuItemIngredient,
    Ingredient, MenuItemIncludedItem, IngredientOption
)


class MenuItemAdmin(admin.ModelAdmin):
    '''Menu Item Admin'''
    list_display = ('name', 'category', 'price')
    list_filter = ('category',)


class MenuItemIngredientAdmin(admin.ModelAdmin):
    '''Menu Item Ingredient Admin'''
    list_display = (
        'menu_item',
        'ingredient',
        'price',
        'option',
        'is_optional')


class MenuItemIngredientInline(admin.TabularInline):
    '''Menu Item Ingredient Inline'''
    model = MenuItemIngredient
    extra = 1


class IngredientOptionAdmin(admin.ModelAdmin):
    '''Ingredient Option Admin'''
    inlines = [MenuItemIngredientInline]


admin.site.register(IngredientOption, IngredientOptionAdmin)
admin.site.register(MenuCategory)
admin.site.register(MenuItem, MenuItemAdmin)
admin.site.register(MenuItemIngredient, MenuItemIngredientAdmin)
admin.site.register(Ingredient)
admin.site.register(MenuItemIncludedItem)
