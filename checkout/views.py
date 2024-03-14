from django.shortcuts import render, redirect, reverse
from .forms import OrderForm
from django.contrib import messages
from django.conf import settings
from cart.views import get_cart_items  # Import the get_cart_items function
from cart.context_processors import cart_total_price  # Import the cart_total_price function
import stripe

# def checkout(request):
#     cart_items = get_cart_items(request)  # Get the cart items

#     if request.method == 'POST':
#         form = CheckoutForm(request.POST)
#         if form.is_valid():
#             # If the user is authenticated and wants to save their info,
#             # save it to their profile
#             if request.user.is_authenticated and form.cleaned_data['save_info']:
#                 profile, created = Profile.objects.get_or_create(user=request.user)
#                 profile.first_name = form.cleaned_data['first_name']
#                 profile.last_name = form.cleaned_data['last_name']
#                 profile.address = form.cleaned_data['address']
#                 profile.city = form.cleaned_data['city']
#                 profile.postal_code = form.cleaned_data['postal_code']
#                 profile.country = form.cleaned_data['country']
#                 profile.save()
#             # Process the payment and handle the order...
#             return redirect('success')  # Redirect to a success page after payment
#     else:
#         # If the user is authenticated, pre-fill the form with their profile info
#         if request.user.is_authenticated:
#             profile, created = Profile.objects.get_or_create(user=request.user)
#             form = CheckoutForm(initial={
#                 'first_name': profile.first_name,
#                 'last_name': profile.last_name,
#                 'address': profile.address,
#                 'city': profile.city,
#                 'postal_code': profile.postal_code,
#                 'country': profile.country,
#             })
#         else:
#             form = CheckoutForm()

#     # Pass the form and the cart items to the template
#     return render(request, 'checkout/checkout.html', {'form': form, 'cart_items': cart_items})


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

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