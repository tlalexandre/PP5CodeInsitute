from django.shortcuts import render, redirect, reverse, get_object_or_404 , HttpResponse
from django.views.decorators.http import require_POST
from .forms import OrderForm
from django.contrib import messages
from django.conf import settings
from orderonline.models import MenuItem, MenuItemIncludedItem, MenuItemIngredient
from cart.context_processors import cart_total_price  # Import the cart_total_price function
from .models import OrderLineItem, Order
from profiles.models import UserProfile
from profiles.forms import UserProfileForm

import stripe
import json
import time

@require_POST
def cache_checkout_data(request):
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY

        # Get the cart data from the session
        cart = request.session.get('cart', {})

        # Calculate the total quantity and total price of the items in the cart
        total_quantity = sum(item['quantity'] for item in cart)
        total_price = sum(float(item['price']) * item['quantity'] for item in cart)

        # Store only the total quantity and total price in the PaymentIntent metadata
        stripe.PaymentIntent.modify(pid, metadata={
            'total_quantity': total_quantity,
            'total_price': total_price,
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })

        return HttpResponse(status=200)
    except Exception as e:
        print('Error in cache_checkout_data view:', e)
        messages.error(request, 'Sorry, your payment cannot be \
            processed right now. Please try again later.')
        return HttpResponse(content=e, status=400)

def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        cart = request.session.get('cart', {})
        
        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'town_or_city': request.POST['town_or_city'],
            'country': request.POST['country'],
            'county': request.POST['county'],
            'pickup_time': request.POST['pickup_time'],
        }
        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save(commit=False)
            pid = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = pid
            order.original_cart = json.dumps(cart)
            total_price = sum(float(item['subtotal']) for item in cart)
            order.total_price = total_price
            order.save()
            print('Order created by checkout view: ',order, 'Checkout PID',order.stripe_pid, order.total_price, order.original_cart,)
            for item_data in cart:
                print('Item data:', item_data)
                try:
                    menu_item_id = item_data.get('id')
                    menu_item = MenuItem.objects.get(id=menu_item_id)
                    quantity = item_data['quantity']

                    # Convert included_item to a MenuItemIncludedItem instance
                    included_item_data = item_data.get('included_item')
                    print('Included item data:', included_item_data)
                    if included_item_data is not None:
                        included_item_id = included_item_data['id']
                        included_item_menu_item = MenuItem.objects.get(id=included_item_id)
                        included_item = MenuItemIncludedItem.objects.get(menu_item=menu_item, included_item=included_item_menu_item)
                        print('Included item:', included_item, included_item.price)
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

                    if included_item is not None:
                        included_item_options_data = [option['name'] for option in included_item_data.get('options', [])]
                        included_item_extras_data = [extra['name'] for extra in included_item_data.get('extras', [])]

                        included_item_options = included_item.included_item.menuitemingredient_set.filter(ingredient__name__in=included_item_options_data)
                        print('Included item options:', included_item_options, included_item_options_data)

                        included_item_extras = included_item.included_item.menuitemingredient_set.filter(ingredient__name__in=included_item_extras_data)
                        print('Included item extras:', included_item_extras, included_item_extras_data)
                    else:
                        included_item_options = []
                        included_item_extras = []

                    order_line_item.included_item_options.set(included_item_options)
                    order_line_item.included_item_extras.set(included_item_extras)

                    options_data = item_data.get('options', [])
                    options = [MenuItemIngredient.objects.get(id=option_data['id']) for option_data in options_data]
                    order_line_item.options.set(options)

                    extras_data = item_data.get('extras', [])
                    extras = [MenuItemIngredient.objects.get(id=extra_data['id']) for extra_data in extras_data]
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
            return redirect(reverse('cart'))
        cart_total_price_context = cart_total_price(request)
        total = cart_total_price_context['cart_total_price']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        if request.user.is_authenticated:
            try:
                profile = UserProfile.objects.get(user=request.user)
                order_form = OrderForm(initial={
                    'full_name': profile.user.get_full_name(),
                    'email': profile.user.email,
                    'phone_number': profile.default_phone_number,
                    'street_address1': profile.default_street_address1,
                    'street_address2': profile.default_street_address2,
                    'town_or_city': profile.default_town_or_city,
                    'county': profile.default_county,
                    'country': profile.default_country,
                })
            except UserProfile.DoesNotExist:
                order_form = OrderForm()
        else:

            order_form = OrderForm()

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. Did you forget to set it in your environment?')

    template = 'checkout/checkout.html'
    print('Cart in checkout view:', cart)
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

    order_line_items=OrderLineItem.objects.filter(order=order)

    for line_item in order_line_items:
        print('Order line item:', line_item.menu_item, line_item.included_item, line_item.quantity, line_item.lineitem_total, line_item.options.all(), line_item.extras.all(), line_item.included_item_options.all(), line_item.included_item_extras.all())

    profile= UserProfile.objects.get(user=request.user)
    order.user_profile = profile
    order.save()

    if save_info:
        profile_data = {
            'default_phone_number': order.phone_number,
            'default_street_address1': order.street_address1,
            'default_street_address2': order.street_address2,
            'default_town_or_city': order.town_or_city,
            'default_county': order.county,
            'default_country': order.country,
        }
        user_profile_form = UserProfileForm(profile_data, instance=profile)
        if user_profile_form.is_valid():
            user_profile_form.save()
    
    messages.success(request, f'Order successfully processed! \
        Your order number is {order_number}. A confirmation \
        email will be sent to {order.email}.')

    if 'cart' in request.session:
        del request.session['cart']

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'order_line_items':order_line_items,
    }

    return render(request, template, context)