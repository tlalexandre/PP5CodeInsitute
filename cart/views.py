from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from orderonline.models import MenuItem, MenuItemIngredient, MenuItemIncludedItem
from orderonline.forms import AddToCartForm

def cart(request):
    # Get the cart from the session
    cart = request.session.get('cart', [])

    # Render the cart template
    return render(request, 'cart/cart.html', {'cart': cart})


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
            'price': float(item.price),
            'options': [get_object_or_404(MenuItemIngredient, id=int(option_id[0])).ingredient.name for option_id in selected_options if is_int(option_id[0]) and MenuItemIngredient.objects.filter(id=int(option_id[0])).exists()],
            'extras': [get_object_or_404(MenuItemIngredient, id=int(extra_id[0])).ingredient.name for extra_id in selected_extras if is_int(extra_id[0]) and MenuItemIngredient.objects.filter(id=int(extra_id[0])).exists()],
            'image_url': item.image.url if item.image else None,
        }
        if included_item is not None:
            cart_item['included_item'] = {
                'name': included_item.included_item.name,
                'options': [get_object_or_404(MenuItemIngredient, id=int(option_id[0])).ingredient.name for option_id in selected_included_options if MenuItemIngredient.objects.filter(id=int(option_id[0])).exists()],
                'extras': [get_object_or_404(MenuItemIngredient, id=int(extra_id[0])).ingredient.name for extra_id in selected_included_extras if MenuItemIngredient.objects.filter(id=int(extra_id[0])).exists()],
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