from django.shortcuts import render, redirect, reverse, get_object_or_404 , HttpResponse
from django.views.decorators.http import require_POST
from .forms import OrderForm
from django.contrib import messages
from django.conf import settings
from orderonline.models import MenuItem, MenuItemIncludedItem
from cart.views import get_cart_items  # Import the get_cart_items function
from cart.context_processors import cart_total_price  # Import the cart_total_price function
from .models import OrderLineItem, Order

import stripe
import json

@require_POST
def cache_checkout_data(request):
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'cart': json.dumps(request.session.get('cart', {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Sorry, your payment cannot be \
            processed right now. Please try again later.')
        return HttpResponse(content=e, status=400)

def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    current_cart= get_cart_items(request)
    print(current_cart)

    if request.method == 'POST':
        cart = request.session.get('cart', {})
        
        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'town_or_city': request.POST['town_or_city'],
            'postcode': request.POST['postcode'],
            'country': request.POST['country'],
        }
        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save()
            for item_data in current_cart:
                print(item_data)
                try:
                    menu_item = item_data.get('item')
                    included_item = item_data.get('included_item')
                    quantity = item_data['quantity']

                    # Convert included_item to a MenuItemIncludedItem instance
                    if included_item is not None:
                        included_items = MenuItemIncludedItem.objects.filter(included_item__id=included_item.id)
                        # Handle the case where multiple objects are returned
                        if included_items.exists():
                            included_item = included_items.first()
                        else:
                            included_item = None
                    else:
                        included_item = None

                    order_line_item = OrderLineItem(
                        order=order,
                        menu_item=menu_item,
                        included_item=included_item,
                        quantity=quantity,
                    )
                    order_line_item.save()  # Save the instance to generate an ID
                    order_line_item.print_prices()

                    # Now you can set the many-to-many fields
                    included_item_options = item_data.get('included_item_options')
                    if included_item_options is not None:
                        order_line_item.included_item_options.set(included_item_options)

                    included_item_extras = item_data.get('included_item_extras')
                    if included_item_extras is not None:
                        order_line_item.included_item_extras.set(included_item_extras)

                    options = item_data.get('options')
                    if options is not None:
                        order_line_item.options.set(options)

                    extras = item_data.get('extras')
                    if extras is not None:
                        order_line_item.extras.set(extras)

                    # Call save again to update the lineitem_total with the prices of the options and extras
                    order_line_item.save()
                except MenuItem.DoesNotExist:
                    messages.error(request, (
                        "One of the products in your cart wasn't found in our database. "
                        "Please call us for assistance!")
                    )
                    order.delete()
                    return redirect(reverse('cart'))

            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('checkout_success', args=[order.order_number]))
        else:
            messages.error(request, 'There was an error with your form. \
                Please double check your information.')
    else:

        cart = request.session.get('cart', {})
        if not cart:
            messages.error(request, "There's nothing in your cart at the moment")
            return redirect(reverse('orderonline'))
        cart_total_price_context = cart_total_price(request)
        total = cart_total_price_context['cart_total_price']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        print(stripe.api_key)
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )
        print(intent)

        order_form = OrderForm()

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. Did you forget to set it in your environment?')

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'cart': cart,
        'stripe_public_key': stripe_public_key, 
        'client_secret': intent.client_secret,
    }
    return render(request, template, context)



def checkout_success(request, order_number):
    """
    Handle successful checkouts
    """
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)
    messages.success(request, f'Order successfully processed! \
        Your order number is {order_number}. A confirmation \
        email will be sent to {order.email}.')

    if 'cart' in request.session:
        del request.session['cart']

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)