from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required



@login_required
def profile(request):
    """ Display the user's profile. """

    template = 'profiles/profile.html'

    return render(request, template)

# @login_required
# def order_history(request, order_number):
#     order = get_object_or_404(Order, order_number=order_number)

#     messages.info(request, (
#         f'This is a past confirmation for order number {order_number}. '
#         'A confirmation email was sent on the order date.'
#     ))

#     template = 'checkout/checkout_success.html'
#     context = {
#         'order': order,
#         'from_profile': True,
#     }

#     return render(request, template, context)