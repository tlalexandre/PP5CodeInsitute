from django.contrib import admin
from .models import MenuCategory, MenuItem, MenuItemIngredient, Ingredient, MenuItemIncludedItem, IngredientOption

class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price')
    list_filter = ('category',)
    filter_horizontal = ('ingredients',)

class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name', 'option')
    list_filter = ('option',)


class MenuItemIngredientAdmin(admin.ModelAdmin):
    list_display = ('menu_item', 'ingredient', 'price', 'is_optional')
    

admin.site.register(MenuCategory)
admin.site.register(MenuItem, MenuItemAdmin)
admin.site.register(MenuItemIngredient, MenuItemIngredientAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(MenuItemIncludedItem)
admin.site.register(IngredientOption)
