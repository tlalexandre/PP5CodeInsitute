from django.shortcuts import render, get_object_or_404
from .models import MenuCategory, MenuItem, MenuItemIngredient, IngredientOption, MenuItemIncludedItem
# Create your views here.

def order_online(request):
    """ A view to return the order online page """
    
    categories = MenuCategory.objects.all()

    items= MenuItem.objects.all()
    
    context= {
        'categories': categories,
        'items': items,
    }

    return render(request, 'orderonline/orderonline.html', context)

def item_detail(request, item_id):
    item = get_object_or_404(MenuItem, pk=item_id)
    menu_item_ingredients = MenuItemIngredient.objects.filter(menu_item=item).order_by('option')
    ingredient_options = IngredientOption.objects.filter(menu_items=item)
    included_items = MenuItemIncludedItem.objects.filter(menu_item=item)

    # Retrieve the MenuItemIngredient instances for each IncludedItem and order them by option
    for included_item in included_items:
        included_item.ingredients = MenuItemIngredient.objects.filter(menu_item=included_item.included_item).order_by('option')

    categories = MenuCategory.objects.all()

    return render(request, 'orderonline/item_detail.html', {
        'item': item,
        'menu_item_ingredients': menu_item_ingredients,
        'ingredient_options': ingredient_options,
        'included_items': included_items,
        'categories': categories,
    })