from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from orderonline.models import MenuItem, Ingredient, MenuItemIncludedItem

# Create your views here.
def cart(request):
    # Get the cart from the session
    cart = request.session.get('cart', [])

    # Create a new list for the cart items
    cart_items = []

    # Loop over the cart items
    for item in cart:
        # Copy the item dictionary
        item = item.copy()

        # Replace the option and extra IDs with the corresponding Ingredient objects
        item['options'] = [get_object_or_404(Ingredient, id=option_id) for option_id in item['options']]
        item['extras'] = [get_object_or_404(Ingredient, id=extra_id) for extra_id in item['extras']]

        # Add the item to the new list
        cart_items.append(item)

    # Pass the new list to the template
        print(cart_items)
    return render(request, 'cart/cart.html', {'cart': cart_items})


def add_to_cart(request):
    if request.method == 'POST':
        # Get the selected options and extras from the form data
        selected_options = []
        selected_extras = []
        selected_included_item = request.POST.get('included_item')

         # Loop over the POST data
        for key, value in request.POST.items():
            if key.startswith('option_'):
                selected_options.append(value)
            elif key.startswith('extra_'):
                selected_extras.append(value)

        # Get the MenuItem object for the selected item
        menu_item = get_object_or_404(MenuItem, id=request.POST.get('item_id'))

        # Create a dictionary for the cart item
        cart_item = {
            'item_id': menu_item.id,
            'name': menu_item.name,
            'price': float(menu_item.price),
            'options': [int(option) for option in selected_options],
            'extras': [int(extra) for extra in selected_extras],
        }

        # Add the selected included item to the cart item
        if selected_included_item:
            included_item = get_object_or_404(MenuItemIncludedItem, id=selected_included_item)
            cart_item['included_item'] = included_item.included_item.id
            cart_item['price'] += float(included_item.price)

        # Get the cart from the session
        cart = request.session.get('cart', [])

        # Add the cart item to the cart
        cart.append(cart_item)

        # Save the cart in the session
        request.session['cart'] = cart

        # Display a success message
        messages.success(request, f'{menu_item.name} has been added to cart')

        print(request.session['cart'])

        return redirect('cart')