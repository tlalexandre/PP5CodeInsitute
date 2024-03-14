from django.shortcuts import render, redirect
from .forms import CheckoutForm
from profiles.models import Profile
from cart.views import get_cart_items  # Import the get_cart_items function

def checkout(request):
    cart_items = get_cart_items(request)  # Get the cart items

    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            # If the user is authenticated and wants to save their info,
            # save it to their profile
            if request.user.is_authenticated and form.cleaned_data['save_info']:
                profile, created = Profile.objects.get_or_create(user=request.user)
                profile.first_name = form.cleaned_data['first_name']
                profile.last_name = form.cleaned_data['last_name']
                profile.address = form.cleaned_data['address']
                profile.city = form.cleaned_data['city']
                profile.postal_code = form.cleaned_data['postal_code']
                profile.country = form.cleaned_data['country']
                profile.save()
            # Process the payment and handle the order...
            return redirect('success')  # Redirect to a success page after payment
    else:
        # If the user is authenticated, pre-fill the form with their profile info
        if request.user.is_authenticated:
            profile, created = Profile.objects.get_or_create(user=request.user)
            form = CheckoutForm(initial={
                'first_name': profile.first_name,
                'last_name': profile.last_name,
                'address': profile.address,
                'city': profile.city,
                'postal_code': profile.postal_code,
                'country': profile.country,
            })
        else:
            form = CheckoutForm()

    # Pass the form and the cart items to the template
    return render(request, 'checkout/checkout.html', {'form': form, 'cart_items': cart_items})


