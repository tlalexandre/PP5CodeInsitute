from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from orderonline.models import MenuItem, MenuItemIngredient, MenuItemIncludedItem, IngredientOption
from orderonline.forms import AddToCartForm
from decimal import Decimal
from django.db import models
from django.db.models import QuerySet


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
            'options': [{'id': int(option_id[0]), 'name': get_object_or_404(MenuItemIngredient, id=int(option_id[0])).ingredient.name, 'price': "{:.2f}".format(float(get_object_or_404(MenuItemIngredient, id=int(option_id[0])).price))} for option_id in selected_options if is_int(option_id[0]) and MenuItemIngredient.objects.filter(id=int(option_id[0])).exists()],
            'extras': [{'id': int(extra_id[0]), 'name': get_object_or_404(MenuItemIngredient, id=int(extra_id[0])).ingredient.name, 'price': "{:.2f}".format(float(get_object_or_404(MenuItemIngredient, id=int(extra_id[0])).price))} for extra_id in selected_extras if is_int(extra_id[0]) and MenuItemIngredient.objects.filter(id=int(extra_id[0])).exists()],
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




def update_cart_item(request, item_index):
    # Get the cart from the session
    cart = request.session.get('cart', [])

    # Check if the item index is valid
    if 0 <= item_index < len(cart):
        # Get the item at the given index from the cart
        cart_item = cart[item_index]

        # Convert the cart item back to a MenuItem instance
        item = MenuItem.objects.get(name=cart_item['name'])

        if request.method == 'POST':
            # If the form has been submitted, update the item with the form data
            form = AddToCartForm(request.POST, item=item)
            if form.is_valid():
                # Update the item in the cart
                cleaned_data = form.cleaned_data.copy()
                for key, value in cleaned_data.items():
                    if isinstance(value, models.Model):
                        cleaned_data[key] = value.id
                    elif isinstance(value, QuerySet):
                        cleaned_data[key] = [{'id': obj.id, 'name': obj.ingredient.name, 'price': "{:.2f}".format(float(obj.price))} for obj in value]
                cart_item.update(cleaned_data)
                cart[item_index] = dict(cart_item)  # Replace the dictionary in the cart list

                # Save the cart back to the session
                request.session['cart'] = cart

                # Display a success message
                messages.success(request, 'Item has been updated')

                return redirect('cart')
            else:
                print(form.errors)  # Print the form errors

        # If the form has not been submitted, display the form with the current item data
        initial_data = {
            'item_id': item.id,
        }

        if 'included_item' in cart_item:
                included_item = MenuItemIncludedItem.objects.get(included_item__name=cart_item['included_item']['name'])
                initial_data['included_item'] = str(included_item.id)

        for option in cart_item['options']:
            menu_item_ingredients = MenuItemIngredient.objects.filter(ingredient__name=option['name'])
            initial_data[menu_item_ingredients.first().option.name] = [str(mii.id) for mii in menu_item_ingredients]

        for extra in cart_item['extras']:
            menu_item_ingredients = MenuItemIngredient.objects.filter(ingredient__name=extra['name'])
            initial_data['Extras'] = [str(mii.id) for mii in menu_item_ingredients]

        form = AddToCartForm(initial=initial_data, item=item, adding=False)

        item_price = item.price
        for option in cart_item['options']:
            item_price += Decimal(option['price'])
        for extra in cart_item['extras']:
            item_price += Decimal(extra['price'])

        return render(request, 'orderonline/update_item.html', {'form': form, 'item_index': item_index, 'item': item, 'item_price': item_price})
