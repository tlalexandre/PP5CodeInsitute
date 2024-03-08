from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from orderonline.models import MenuItem, MenuItemIngredient, MenuItemIncludedItem, IngredientOption
from orderonline.forms import AddToCartForm
from decimal import Decimal
import json
from django.core.serializers.json import DjangoJSONEncoder


def cart(request):
    # Get the cart from the session
    cart = request.session.get('cart', [])

    # Render the cart template
    return render(request, 'cart/cart.html', {'cart': cart})


class DecimalEncoder(DjangoJSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return str(obj)
        return super().default(obj)

def is_int(value):
    try:
        int(value)
        return True
    except ValueError:
        return False
    
def calculate_total_price(request, item, selected_options, selected_extras, selected_included_options, selected_included_extras):
    total_price = Decimal(item.price)
    for option_id in selected_options:
        print(f"Option ID: {option_id}")
        option = get_object_or_404(MenuItemIngredient, id=int(option_id))
        total_price += Decimal(option.price)
    for extra_id in selected_extras:
        print(f"Extra ID: {extra_id}")
        extra = get_object_or_404(MenuItemIngredient, id=int(extra_id))
        total_price += Decimal(extra.price)
    included_item_id = request.POST.get('included_item')
    if included_item_id:
        print(f"Included Item ID: {included_item_id}")
        included_item = get_object_or_404(MenuItemIncludedItem, id=int(included_item_id))
        total_price += Decimal(included_item.price)
        for option_id in selected_included_options:
            print(f"Included Option ID: {option_id}")
            option = get_object_or_404(MenuItemIngredient, id=int(option_id))
            total_price += Decimal(option.price)
        for extra_id in selected_included_extras:
            print(f"Included Extra ID: {extra_id}")
            extra = get_object_or_404(MenuItemIngredient, id=int(extra_id))
            total_price += Decimal(extra.price)
    return total_price

def add_to_cart(request):
    if request.method == 'POST':
        print(request.POST)
        # Get the selected item
        item_id = request.POST.get('item_id')
        print("Item ID: ", item_id)
        item = get_object_or_404(MenuItem, id=item_id)

        # Get the selected included item
        included_item_id = request.POST.get('included_item')
        included_item = None
        print("Included item ID: ", included_item_id)
        if included_item_id:
            included_item = get_object_or_404(MenuItemIncludedItem, id=included_item_id)
            print("Included item: ", included_item.included_item.name)

        # Get the selected options and extras
        selected_options = []
        selected_extras = []
        selected_included_options = []
        selected_included_extras = []


        for key, values in request.POST.lists():
            print(f"Key: {key}, Values: {values}")
            if 'included_item_option_' in key:
                selected_included_options.extend(values)
            elif 'included_item_extra_' in key:
                selected_included_extras.extend(values)  # No need to check if it's an int or if the MenuItemIngredient exists here
            elif 'Extras' in key:
                selected_extras.extend(values)  # No need to check if it's an int or if the MenuItemIngredient exists here
            else:
                for value in values:
                    if is_int(value) and MenuItemIngredient.objects.filter(id=int(value), option__isnull=False, menu_item=item).exists():
                        selected_options.extend([value])

        print(f"Selected options: {selected_options}")
        print(f"Selected extras: {selected_extras}")
        print(f"Selected included options: {selected_included_options}")
        print(f"Selected included extras: {selected_included_extras}")

        try:
            cart_item = {
                'name': item.name,
                'original_price': "{:.2f}".format(float(item.price)),
                'price': "{:.2f}".format(float(calculate_total_price(request, item, selected_options, selected_extras, selected_included_options, selected_included_extras))),
                'options': [{'id': int(option_id), 'name': MenuItemIngredient.objects.get(id=int(option_id)).ingredient.name, 'price': "{:.2f}".format(float(MenuItemIngredient.objects.get(id=int(option_id)).price))} for option_id in selected_options if is_int(option_id) and MenuItemIngredient.objects.filter(id=int(option_id)).exists()],
                'extras': [{'id': int(extra_id), 'name': MenuItemIngredient.objects.get(id=int(extra_id)).ingredient.name, 'price': "{:.2f}".format(float(MenuItemIngredient.objects.get(id=int(extra_id)).price))} for extra_id in selected_extras if is_int(extra_id) and MenuItemIngredient.objects.filter(id=int(extra_id)).exists()],
                'image_url': item.image.url if item.image else None,
            }
            if included_item is not None:
                print("Included item: ", included_item.menu_item.name)
                cart_item['included_item'] = {
                    'name': included_item.included_item.name,
                    'price': "{:.2f}".format(float(included_item.price)),
                    'options': [{'name': MenuItemIngredient.objects.get(id=int(option_id[0])).ingredient.name, 'price': "{:.2f}".format(float(MenuItemIngredient.objects.get(id=int(option_id[0])).price))} for option_id in selected_included_options if is_int(option_id[0]) and MenuItemIngredient.objects.filter(id=int(option_id[0])).exists()],
                    'extras': [{'name': MenuItemIngredient.objects.get(id=int(extra_id)).ingredient.name, 'price': "{:.2f}".format(float(MenuItemIngredient.objects.get(id=int(extra_id)).price))} for extra_id in selected_included_extras if is_int(extra_id) and MenuItemIngredient.objects.filter(id=int(extra_id)).exists()],
                }
        except MenuItemIngredient.DoesNotExist as e:
            print(f"MenuItemIngredient with id does not exist: {e}")
            messages.error(request, 'An error occurred while adding the item to the cart. Please try again.')
            return redirect('cart')

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
            # Get the selected options and extras
            selected_options = []
            selected_extras = []
            selected_included_options = []
            selected_included_extras = []

            for key, values in request.POST.lists():
                if 'included_item_option_' in key:
                    selected_included_options.extend(values)
                elif 'included_item_extra_' in key:
                    selected_included_extras.extend(values)
                elif 'Extras' in key:  # Add this condition to handle multiple extras
                    for value in values:
                        if is_int(value) and MenuItemIngredient.objects.filter(id=int(value), option__isnull=True, menu_item=item).exists():
                            selected_extras.append(value)  # Use append instead of extend
                else:
                    for value in values:
                        if is_int(value) and MenuItemIngredient.objects.filter(id=int(value), option__isnull=False, menu_item=item).exists():
                            selected_options.append(value)  # Use append instead of extend

            try:
                # Update the cart item
                cart_item['price'] = "{:.2f}".format(float(calculate_total_price(request, item, selected_options, selected_extras, selected_included_options, selected_included_extras)))
                cart_item['options'] = [{'id': int(option_id), 'name': get_object_or_404(MenuItemIngredient, id=int(option_id)).ingredient.name, 'price': "{:.2f}".format(float(get_object_or_404(MenuItemIngredient, id=int(option_id)).price))} for option_id in selected_options if is_int(option_id) and MenuItemIngredient.objects.filter(id=int(option_id)).exists()]
                cart_item['extras'] = [{'id': int(extra_id), 'name': get_object_or_404(MenuItemIngredient, id=int(extra_id)).ingredient.name, 'price': "{:.2f}".format(float(get_object_or_404(MenuItemIngredient, id=int(extra_id)).price))} for extra_id in selected_extras if is_int(extra_id) and MenuItemIngredient.objects.filter(id=int(extra_id)).exists()]
            except Exception as e:
                print("An error occurred: ", str(e))

            # Save the cart back to the session
            request.session['cart'] = cart

            # Display a success message
            messages.success(request, 'Item has been updated')

            return redirect('cart')


        # If the form has not been submitted, display the form with the current item data
        initial_data = {
            'item_id': item.id,
        }
        
        included_items = MenuItemIncludedItem.objects.none()  # Initialize an empty queryset

        if 'included_item' in cart_item:
            included_items = MenuItemIncludedItem.objects.filter(included_item__name=cart_item['included_item']['name'])
            for included_item in included_items:
                initial_data['included_item'] = str(included_item.id)

        for option in cart_item['options']:
            menu_item_ingredients = MenuItemIngredient.objects.filter(ingredient__name=option['name'])
            initial_data[menu_item_ingredients.first().option.name] = [str(mii.id) for mii in menu_item_ingredients]

        # Initialize the list of IDs for the extras
        initial_data['Extras'] = []

        for extra in cart_item['extras']:
            menu_item_ingredients = MenuItemIngredient.objects.filter(ingredient__name=extra['name'])
            # Extend the list of IDs for the extras with the IDs of the MenuItemIngredient objects for this extra
            initial_data['Extras'].extend([str(mii.id) for mii in menu_item_ingredients])

        form = AddToCartForm(initial=initial_data, item=item, adding=False)

        item_price = item.price
        for option in cart_item['options']:
            item_price += Decimal(option['price'])
        for extra in cart_item['extras']:
            item_price += Decimal(extra['price'])

        # Get the optionsExtras data
        optionsExtras = {}
        for included_item in MenuItemIncludedItem.objects.filter(menu_item=item):
            optionsExtras[included_item.id] = {
                'Extras': [
                    {
                        'id': extra.id,
                        'ingredient__name': extra.ingredient.name,
                        'price': "{:.2f}".format(float(extra.price)),
                    }
                    for extra in MenuItemIngredient.objects.filter(menu_item=included_item.included_item, option__isnull=True)
                ],
                'Options': {},
            }
            for option in MenuItemIngredient.objects.filter(menu_item=included_item.included_item, option__isnull=False):
                option_name = option.option.name
                if option_name not in optionsExtras[included_item.id]['Options']:
                    optionsExtras[included_item.id]['Options'][option_name] = []
                optionsExtras[included_item.id]['Options'][option_name].append({
                    'id': option.id,
                    'ingredient__name': option.ingredient.name,
                    'price': "{:.2f}".format(float(option.price)),
                })

        optionsExtras_json = json.dumps(optionsExtras)

        # Pass the optionsExtras data to the template
        return render(request, 'orderonline/update_item.html', {
            'form': form,
            'item_index': item_index,
            'item': item,
            'item_price': item_price,
            'optionsExtras': optionsExtras_json,  # Pass optionsExtras as a Python object
        })