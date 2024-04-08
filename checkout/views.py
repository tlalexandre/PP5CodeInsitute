from django.shortcuts import (
    render, redirect, reverse, get_object_or_404, HttpResponse
)
from django.views.decorators.http import require_POST
from .forms import OrderForm
from django.contrib import messages
from django.conf import settings
from orderonline.models import (
    MenuItem, MenuItemIncludedItem, MenuItemIngredient
    )
from cart.context_processors import cart_total_price
from .models import OrderLineItem, Order, Cart
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
        cart = request.session.get('cart', {})
        total_quantity = sum(item['quantity'] for item in cart)
        total_price = sum(
            float(item['price']) * item['quantity'] for item in cart)
        stripe.PaymentIntent.modify(pid, metadata={
            'total_quantity': total_quantity,
            'total_price': total_price,
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        error_message = (
            'Sorry, your payment cannot be'
            ' processed right now. Please try again later.')
        messages.error(
            request,
            error_message
        )
        return HttpResponse(content=e, status=400)


def checkout(request):
    """
    Handles the checkout process.

    This function creates a Stripe PaymentIntent and an Order instance
    based on the items in the user's cart. 
    It also handles the creation of OrderLineItem instances for each item
    in the cart, including any included items and their options and extras.

    If the user is authenticated, the function pre-fills the order form with
    the user's default information from their profile.

    The function also handles form validation and error handling,
    including checking if the cart is empty and if the Stripe public key is 
    missing.

    Parameters:
    request (HttpRequest): The request instance.

    Returns:
    HttpResponse: The response instance, 
    rendering the 'checkout/checkout.html' template.
    """
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        cart = request.session.get('cart', {})
        cart_obj = Cart.objects.create(items=json.dumps(cart))

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
            for item_data in cart:
                try:
                    menu_item_id = item_data.get('id')
                    menu_item = MenuItem.objects.get(id=menu_item_id)
                    quantity = item_data['quantity']
                    included_item_data = item_data.get('included_item')
                    if included_item_data is not None:
                        included_item_id = included_item_data['id']
                        included_item_menu_item = MenuItem.objects.get(
                            id=included_item_id)
                        included_item = MenuItemIncludedItem.objects.get(
                            menu_item=menu_item,
                            included_item=included_item_menu_item
                        )
                    else:
                        included_item = None

                    item_price = item_data['price']
                    order_line_item = OrderLineItem(
                        order=order,
                        menu_item=menu_item,
                        included_item=included_item,
                        quantity=quantity,
                        item_price=item_price,
                    )
                    order_line_item.save()
                    

                    if included_item is not None:
                        included_item_options_data = [
                            option['name']
                            for option in included_item_data.get('options', [])
                        ]
                        included_item_extras_data = [
                            extra['name']
                            for extra in included_item_data.get('extras', [])
                        ]
                        included_item_options = (
                            included_item
                            .included_item
                            .menuitemingredient_set
                            .filter(
                                ingredient__name__in=included_item_options_data
                            )
                        )
                        included_item_extras = (
                            included_item
                            .included_item
                            .menuitemingredient_set
                            .filter(
                                ingredient__name__in=included_item_extras_data
                                )
                        )
                    else:
                        included_item_options = []
                        included_item_extras = []
                    order_line_item.included_item_options.set(
                        included_item_options
                        )
                    order_line_item.included_item_extras.set(
                        included_item_extras
                        )

                    options_data = item_data.get('options', [])
                    options = [
                        MenuItemIngredient.objects.get(
                            id=option_data['id']
                            ) for option_data in options_data
                    ]
                    order_line_item.options.set(options)

                    extras_data = item_data.get('extras', [])
                    extras = [
                        MenuItemIngredient.objects.get(
                            id=extra_data['id']
                            ) for extra_data in extras_data
                    ]
                    order_line_item.extras.set(extras)
                    order_line_item.save()
                except MenuItem.DoesNotExist:
                    error_message = (
                        'One of the products in your cart'
                        ' wasn\'t found in our database. '
                        'Please call us for assistance!'
                    )
                    messages.error(
                        request,
                        error_message
                    )
                    order.delete()
                    return redirect(reverse('cart'))

            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse(
                'checkout_success', args=[order.order_number]))
        else:
            error_message = (
                'There was an error with your form.'
                'Please double check your information.'
            )
            messages.error(
                request,
                error_message
            )
    else:
        cart = request.session.get('cart', {})
        if not cart:
            messages.error(
                request,
                "There's nothing in your cart at the moment")
            return redirect(reverse('cart'))

        cart_obj = Cart.objects.create(items=json.dumps(cart))

        cart_total_price_context = cart_total_price(request)
        total = cart_total_price_context['cart_total_price']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key

        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
            metadata={
                'cart_id': str(cart_obj.id),
                'username': request.user,
            }
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
        warning_message = (
            'Stripe public key is missing. '
            'Did you forget to set it in your environment?'
        )
        messages.warning(
            request,
            warning_message
        )

    template = 'checkout/checkout.html'

    context = {
        'order_form': order_form,
        'cart': cart,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }
    return render(request, template, context)


def checkout_success(request, order_number):
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)

    order_line_items = OrderLineItem.objects.filter(order=order)

    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
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

    messages.success(
        request,
        f'Order successfully processed! Your order number is {order_number}. '
        f'A confirmation email will be sent to {order.email}.'
    )

    if 'cart' in request.session:
        del request.session['cart']

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'order_line_items': order_line_items,
    }

    return render(request, template, context)
