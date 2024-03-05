from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from orderonline.models import MenuItem, MenuItemIngredient
from orderonline.forms import AddToCartForm

def cart(request):
    # Get the cart from the session
    cart = request.session.get('cart', [])

    # Render the cart template
    return render(request, 'cart/cart.html', {'cart': cart})


def add_to_cart(request):
    if request.method == 'POST':
        form = AddToCartForm(request.POST)
        if form.is_valid():
            # Access form data
            item_id = form.cleaned_data['item_id']
            included_item = form.cleaned_data.get('included_item')  # This may be None if the field was not included in the form

            # Access dynamic form data
            options = {key: value for key, value in request.POST.items() if key.startswith('option')}

            # TODO: Add the item to the cart

            return redirect('cart')
    else:
        form = AddToCartForm()

    return render(request, 'add_to_cart.html', {'form': form})