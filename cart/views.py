from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from orderonline.models import MenuItem, MenuItemIngredient, MenuItemIncludedItem
from orderonline.forms import AddToCartForm
from decimal import Decimal


def cart(request):
    # Get the cart from the session
    cart = request.session.get('cart', [])

    # Render the cart template
    return render(request, 'cart/cart.html', {'cart': cart})


def is_int(value):
    try:
        int(value)
        return True
    except ValueError:
        return False
    
def calculate_total_price(request, item, selected_options, selected_extras, selected_included_options, selected_included_extras):
    total_price = Decimal(item.price)
    for option_id in selected_options:
        option = get_object_or_404(MenuItemIngredient, id=int(option_id[0]))
        total_price += Decimal(option.price)
    for extra_id in selected_extras:
        extra = get_object_or_404(MenuItemIngredient, id=int(extra_id[0]))
        total_price += Decimal(extra.price)
    included_item_id = request.POST.get('included_item')
    if included_item_id:
        included_item = get_object_or_404(MenuItemIncludedItem, id=int(included_item_id))
        total_price += Decimal(included_item.price)
        for option_id in selected_included_options:
            option = get_object_or_404(MenuItemIngredient, id=int(option_id[0]))
            total_price += Decimal(option.price)
        for extra_id in selected_included_extras:
            extra = get_object_or_404(MenuItemIngredient, id=int(extra_id[0]))
            total_price += Decimal(extra.price)
    return total_price

def add_to_cart(request):
    if request.method == 'POST':
        print(request.POST)
        # Get the selected item
        item_id = request.POST.get('item_id')
        item = get_object_or_404(MenuItem, id=item_id)

        # Get the selected included item
        included_item_id = request.POST.get('included_item')
        included_item = None
        if included_item_id:
            included_item = get_object_or_404(MenuItemIncludedItem, id=included_item_id)

        # Get the selected options and extras
        selected_options = []
        selected_extras = []
        selected_included_options = []
        selected_included_extras = []

        def is_int(s):
            try: 
                int(s)
                return True
            except ValueError:
                return False

        for key, value in request.POST.lists():
            if 'included_item_option_' in key:
                selected_included_options.append(value)
            elif 'included_item_extra_' in key:
                selected_included_extras.append(value)
            elif is_int(value[0]) and MenuItemIngredient.objects.filter(id=int(value[0]), option__isnull=False, menu_item=item).exists():
                selected_options.append(value)
            elif is_int(value[0]) and MenuItemIngredient.objects.filter(id=int(value[0]), option__isnull=True, menu_item=item).exists():
                selected_extras.append(value)

        cart_item = {
            'name': item.name,
            'original_price': "{:.2f}".format(float(item.price)),
            'price': "{:.2f}".format(float(calculate_total_price(request, item, selected_options, selected_extras, selected_included_options, selected_included_extras))),
            'options': [{'name': get_object_or_404(MenuItemIngredient, id=int(option_id[0])).ingredient.name, 'price': "{:.2f}".format(float(get_object_or_404(MenuItemIngredient, id=int(option_id[0])).price))} for option_id in selected_options if is_int(option_id[0]) and MenuItemIngredient.objects.filter(id=int(option_id[0])).exists()],
            'extras': [{'name': get_object_or_404(MenuItemIngredient, id=int(extra_id[0])).ingredient.name, 'price': "{:.2f}".format(float(get_object_or_404(MenuItemIngredient, id=int(extra_id[0])).price))} for extra_id in selected_extras if is_int(extra_id[0]) and MenuItemIngredient.objects.filter(id=int(extra_id[0])).exists()],
            'image_url': item.image.url if item.image else None,
        }
        if included_item is not None:
            cart_item['included_item'] = {
                'name': included_item.included_item.name,
                'price': "{:.2f}".format(float(included_item.price)),
                'options': [{'name': get_object_or_404(MenuItemIngredient, id=int(option_id[0])).ingredient.name, 'price': "{:.2f}".format(float(get_object_or_404(MenuItemIngredient, id=int(option_id[0])).price))} for option_id in selected_included_options if is_int(option_id[0]) and MenuItemIngredient.objects.filter(id=int(option_id[0])).exists()],
                'extras': [{'name': get_object_or_404(MenuItemIngredient, id=int(extra_id[0])).ingredient.name, 'price': "{:.2f}".format(float(get_object_or_404(MenuItemIngredient, id=int(extra_id[0])).price))} for extra_id in selected_included_extras if is_int(extra_id[0]) and extra_id[0] != 'undefined' and MenuItemIngredient.objects.filter(id=int(extra_id[0])).exists()],
            }

        # Get the cart from the session
        cart = request.session.get('cart', [])

        # Add the cart item to the cart
        cart.append(cart_item)

        # Save the cart in the session
        request.session['cart'] = cart

        # Display a success message
        messages.success(request, f'{item.name} has been added to cart')

        return redirect('cart')
    


def delete_from_cart(request, item_index):
    # Get the cart from the session
    cart = request.session.get('cart', [])

    # Check if the item index is valid
    if 0 <= item_index < len(cart):
        # Remove the item at the given index from the cart
        del cart[item_index]

        # Save the cart back to the session
        request.session['cart'] = cart

        # Display a success message
        messages.success(request, 'Item has been removed from cart')

    return redirect('cart')