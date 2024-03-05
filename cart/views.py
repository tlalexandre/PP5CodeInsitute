from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from orderonline.models import MenuItem, MenuItemIngredient

def cart(request):
    # Get the cart from the session
    cart = request.session.get('cart', [])

    # Render the cart template
    return render(request, 'cart/cart.html', {'cart': cart})

def add_to_cart(request):
    if request.method == 'POST':
        # Get the selected item
        item_id = request.POST.get('item_id')
        item = get_object_or_404(MenuItem, id=item_id)

        # Get the selected options and extras
        selected_options = request.POST.getlist('option')
        selected_extras = request.POST.getlist('extra')

        # Create a cart item
        cart_item = {
            'name': item.name,
            'price': float(item.price),
            'options': [get_object_or_404(MenuItemIngredient, id=option_id).name for option_id in selected_options],
            'extras': [get_object_or_404(MenuItemIngredient, id=extra_id).name for extra_id in selected_extras],
            'image_url': item.image.url if item.image else None,
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