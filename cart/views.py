from django.contrib import messages
from django.shortcuts import render, redirect
from orderonline.models import MenuItem, Ingredient, MenuItemIncludedItem

# Create your views here.
def cart(request):
    return render(request, 'cart/cart.html')



def add_to_cart(request):
    if request.method == 'POST':
        # Get the selected options and extras from the form data
        selected_options = request.POST.getlist('option')
        selected_extras = request.POST.getlist('extra')
        selected_included_item = request.POST.get('included_item')

        # Get the MenuItem object for the selected item
        menu_item = MenuItem.objects.get(id=request.POST.get('item_id'))

        # Create a dictionary for the cart item
        cart_item = {
            'name': menu_item.name,
            'price': menu_item.price,
            'options': [Ingredient.objects.get(id=option_id).name for option_id in selected_options],
            'extras': [Ingredient.objects.get(id=extra_id).name for extra_id in selected_extras],
        }

        # Add the selected included item to the cart item
        if selected_included_item:
            included_item = MenuItemIncludedItem.objects.get(id=selected_included_item)
            cart_item['included_item'] = included_item.name
            cart_item['price'] += included_item.price

        # Get the cart from the session
        cart = request.session.get('cart', [])

        # Add the cart item to the cart
        cart.append(cart_item)

        # Save the cart in the session
        request.session['cart'] = cart

        # Display a success message
        messages.success(request, f'{menu_item.name} has been added to cart')

        return redirect('cart/cart.html')