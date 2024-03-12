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
    cart_total_price = get_cart_total_price(request)

    # Calculate subtotal for each item in the cart
    for item in cart:
        item['subtotal'] = float(item['price']) * item['quantity']

    # Render the cart template
    return render(request, 'cart/cart.html', {'cart': cart, 'cart_total_price': cart_total_price})

def price_header(request):
    # Get the cart total price
    cart_total_price = get_cart_total_price(request)

    # Render some other template and pass the cart total price
    return render(request, 'base.html', {'cart_total_price': cart_total_price})


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
    
def get_cart_total_price(request):
    cart = request.session.get('cart', [])
    cart_total_price = Decimal(0)
    for item_data in cart:
        item_price = Decimal(item_data.get('price', 0))
        item_quantity = item_data.get('quantity', 1)  # Get the quantity, default to 1 if not provided
        item_total_price = item_price * item_quantity  # Calculate the total price for this item
        cart_total_price += item_total_price
    return cart_total_price

def calculate_total_price(request, item, selected_options, selected_extras, selected_included_options, selected_included_extras, quantity):
    total_price = Decimal(item.price)
    for option_id in selected_options:
        option = get_object_or_404(MenuItemIngredient, id=int(option_id))
        total_price += Decimal(option.price)
    for extra_id in selected_extras:
        extra = get_object_or_404(MenuItemIngredient, id=int(extra_id))
        total_price += Decimal(extra.price)
    included_item_id = request.POST.get('included_item')
    if included_item_id:
        included_item = get_object_or_404(MenuItemIncludedItem, id=int(included_item_id))
        total_price += Decimal(included_item.price)
        for option_id in selected_included_options:
            option = get_object_or_404(MenuItemIngredient, id=int(option_id))
            total_price += Decimal(option.price)
        for extra_id in selected_included_extras:
            extra = get_object_or_404(MenuItemIngredient, id=int(extra_id))
            total_price += Decimal(extra.price)
    subtotal = total_price * quantity
    return total_price, subtotal

def get_cart_items(request):
    from orderonline.models import MenuItem, MenuItemIngredient, MenuItemIncludedItem, IngredientOption

    # Get the cart from the session
    cart = request.session.get('cart', [])

    # Create a list to hold all cart items with their details
    cart_items = []

    # Loop through each item in the cart
    for item_data in cart:
        # Check if 'name' is in the dictionary
        if 'name' in item_data:
            # Get the item from the database
            item = MenuItem.objects.get(name=item_data['name'])

            # Get the included item, options, and extras for the item
            included_item_data = item_data.get('included_item')
            if included_item_data:

                included_item = MenuItem.objects.get(name=included_item_data['name'])
                included_item_option_names = [option['name'] for option in included_item_data.get('options', [])]
                included_item_extra_names = [extra['name'] for extra in included_item_data.get('extras', [])]
                included_item_options = MenuItemIngredient.objects.filter(menu_item=included_item, ingredient__name__in=included_item_option_names)
                included_item_extras = MenuItemIngredient.objects.filter(menu_item=included_item, ingredient__name__in=included_item_extra_names)
            else:
                included_item = None
                included_item_options = MenuItemIngredient.objects.none()
                included_item_extras = MenuItemIngredient.objects.none()

            options = MenuItemIngredient.objects.filter(id__in=[option['id'] for option in item_data.get('options', [])])
            extras = MenuItemIngredient.objects.filter(id__in=[extra['id'] for extra in item_data.get('extras', [])])

            # Create a dictionary to hold the item details
            item_details = {
                'item': item,
                'included_item': included_item,
                'included_item_options': included_item_options,
                'included_item_extras': included_item_extras,
                'options': options,
                'extras': extras,
                'quantity': item_data.get('quantity', 1),
                'total_price': Decimal(item_data.get('price', 0)),
            }

            # Add the item details to the cart_items list
            cart_items.append(item_details)

    # Return the cart_items list
    return cart_items

def add_to_cart(request):
    if request.method == 'POST':
        # Get the selected item
        item_id = request.POST.get('item_id')
        item = get_object_or_404(MenuItem, id=item_id)
        quantity = int(request.POST.get('quantity', 1))

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


        for key, values in request.POST.lists():
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

        try:
            total_price , subtotal = calculate_total_price(request, item, selected_options, selected_extras, selected_included_options, selected_included_extras, quantity)
            cart_item = {
                'name': item.name,
                'quantity': quantity,
                'original_price': "{:.2f}".format(float(item.price)),
                'price': "{:.2f}".format(float(total_price)),
                'subtotal': "{:.2f}".format(float(subtotal)),
                'options': [{'id': int(option_id), 'name': MenuItemIngredient.objects.get(id=int(option_id)).ingredient.name, 'price': "{:.2f}".format(float(MenuItemIngredient.objects.get(id=int(option_id)).price))} for option_id in selected_options if is_int(option_id) and MenuItemIngredient.objects.filter(id=int(option_id)).exists()],
                'extras': [{'id': int(extra_id), 'name': MenuItemIngredient.objects.get(id=int(extra_id)).ingredient.name, 'price': "{:.2f}".format(float(MenuItemIngredient.objects.get(id=int(extra_id)).price))} for extra_id in selected_extras if is_int(extra_id) and MenuItemIngredient.objects.filter(id=int(extra_id)).exists()],
                'image_url': item.image.url if item.image else None,
            }
            if included_item is not None:
                cart_item['included_item'] = {
                    'name': included_item.included_item.name,
                    'price': "{:.2f}".format(float(included_item.price)),
                    'options': [{'name': MenuItemIngredient.objects.get(id=int(option_id)).ingredient.name, 'price': "{:.2f}".format(float(MenuItemIngredient.objects.get(id=int(option_id)).price))} for option_id in selected_included_options if is_int(option_id) and MenuItemIngredient.objects.filter(id=int(option_id)).exists()],
                    'extras': [{'name': MenuItemIngredient.objects.get(id=int(extra_id)).ingredient.name, 'price': "{:.2f}".format(float(MenuItemIngredient.objects.get(id=int(extra_id)).price))} for extra_id in selected_included_extras if is_int(extra_id) and MenuItemIngredient.objects.filter(id=int(extra_id)).exists()],
                }
        except MenuItemIngredient.DoesNotExist as e:
            print(f"MenuItemIngredient with id does not exist: {e}")
            messages.error(request, 'An error occurred while adding the item to the cart. Please try again.')
            return redirect('cart')

        # Get the cart from the session
        cart = request.session.get('cart', [])

        # Check if the item is already in the cart
        for existing_item in cart:
            if existing_item['name'] == item.name:
                # If the item is already in the cart, update the quantity
                existing_item['quantity'] += quantity
                break
        else:
            if 'quantity' not in cart_item:
                cart_item['quantity'] = 1
            cart.append(cart_item)

        # Save the cart in the session
        request.session['cart'] = cart

        # Display a success message
        messages.success(request, f'{item.name} has been added to cart')

        return redirect('order_online')
    


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

            # Get the quantity from the POST data
            quantity = int(request.POST.get('quantity', 1))  # Get the quantity from the POST data, default to 1 if not provided

            # Get the selected included item
            included_item_id = request.POST.get('included_item')
            included_item = None
            if included_item_id:
                included_item = get_object_or_404(MenuItemIncludedItem, id=included_item_id)

            # Get the selected options and extras
            selected_options = request.POST.getlist('options', [])
            selected_extras = request.POST.getlist('extras', [])
            selected_included_options = request.POST.getlist('included_options', [])
            selected_included_extras = request.POST.getlist('included_extras', [])

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
                total_price, _ = calculate_total_price(request, item, selected_options, selected_extras, selected_included_options, selected_included_extras, quantity)
                cart_item['price'] = "{:.2f}".format(float(total_price))
                cart_item['options'] = [{'id': int(option_id), 'name': get_object_or_404(MenuItemIngredient, id=int(option_id)).ingredient.name, 'price': "{:.2f}".format(float(get_object_or_404(MenuItemIngredient, id=int(option_id)).price))} for option_id in selected_options if is_int(option_id) and MenuItemIngredient.objects.filter(id=int(option_id)).exists()]
                cart_item['extras'] = [{'id': int(extra_id), 'name': get_object_or_404(MenuItemIngredient, id=int(extra_id)).ingredient.name, 'price': "{:.2f}".format(float(get_object_or_404(MenuItemIngredient, id=int(extra_id)).price))} for extra_id in selected_extras if is_int(extra_id) and MenuItemIngredient.objects.filter(id=int(extra_id)).exists()]
                cart_item['quantity'] = quantity

                if included_item is not None:
                    cart_item['included_item'] = {
                        'name': included_item.included_item.name,
                        'price': "{:.2f}".format(float(included_item.price)),
                        'options': [{'name': MenuItemIngredient.objects.get(id=int(option_id)).ingredient.name, 'price': "{:.2f}".format(float(MenuItemIngredient.objects.get(id=int(option_id)).price))} for option_id in selected_included_options if is_int(option_id) and MenuItemIngredient.objects.filter(id=int(option_id)).exists()],
                        'extras': [{'name': MenuItemIngredient.objects.get(id=int(extra_id)).ingredient.name, 'price': "{:.2f}".format(float(MenuItemIngredient.objects.get(id=int(extra_id)).price))} for extra_id in selected_included_extras if is_int(extra_id) and MenuItemIngredient.objects.filter(id=int(extra_id)).exists()],
                    }
            except Exception as e:
                print("An error occurred: ", str(e))

            # Save the cart back to the session
            request.session['cart'] = cart


            # Display a success message
            messages.success(request, f'{item.name} has been updated')

            return redirect('cart')


        # If the form has not been submitted, display the form with the current item data
        initial_data = {
            'item_id': item.id,
            'quantity': cart_item['quantity'],
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