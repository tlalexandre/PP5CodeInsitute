from django.shortcuts import render, get_object_or_404,redirect
from django.urls import reverse
from .models import MenuCategory, MenuItem, MenuItemIngredient, IngredientOption, MenuItemIncludedItem , Ingredient
from .forms import AddToCartForm, ItemForm
from django.forms import formset_factory
from django.contrib import messages
from django.db.models import F

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
    item = get_object_or_404(MenuItem, id=item_id)
    included_items = MenuItemIncludedItem.objects.filter(menu_item=item)
    form = AddToCartForm(item=item, initial={'item_id': item})
    categories = MenuCategory.objects.all()

    options_extras = {}
    for included_item in included_items:
        menu_item_ingredients = MenuItemIngredient.objects.filter(menu_item=included_item.included_item).annotate(option_name=F('option__name')).values('id', 'ingredient__name', 'option_name', 'price')
        options_extras[included_item.id] = {'Extras': [], 'Options': {}}
        for menu_item_ingredient in menu_item_ingredients:
            if menu_item_ingredient['option_name']:
                if menu_item_ingredient['option_name'] not in options_extras[included_item.id]['Options']:
                    options_extras[included_item.id]['Options'][menu_item_ingredient['option_name']] = []
                options_extras[included_item.id]['Options'][menu_item_ingredient['option_name']].append(menu_item_ingredient)
            else:
                options_extras[included_item.id]['Extras'].append(menu_item_ingredient)

    return render(request, 'orderonline/item_detail.html', {
        'item': item,
        'categories': categories,
        'form': form,
        'included_items': included_items,
        'options_extras': options_extras,
    })


def product_management(request):
    """ A view to return the product management page """
    return render(request, 'orderonline/product_management.html')


def add_item(request):
    """ Add a new item to the menu """
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save()
            messages.success(request, 'Successfully added item!')
            return redirect(reverse('add_item'))
        else:
            messages.error(request, 'Failed to add item. Please ensure the form is valid.')
    else:
        form = ItemForm()
    template = 'orderonline/add_item.html'
    context = {
        'form': form,
    }
    return render(request, template, context)