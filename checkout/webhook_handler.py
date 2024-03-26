from django.http import HttpResponse
from .models import Order, OrderLineItem, Cart
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from orderonline.models import MenuItem, MenuItemIncludedItem
from profiles.models import UserProfile
from smtplib import SMTPException
import uuid

import json
import stripe
import time


class StripeWH_Handler:
    '''Handle Stripe webhooks'''

    def __init__(self, request):
        self.request = request


    def _send_confirmation_email(self, order):
            """Send the user a confirmation email"""
            cust_email = order.email
            subject = render_to_string(
                'checkout/confirmation_emails/confirmation_email_subject.txt',
                {'order': order})
            body = render_to_string(
                'checkout/confirmation_emails/confirmation_email_body.txt',
                {'order': order, 'contact_email': settings.DEFAULT_FROM_EMAIL})
            
            send_mail(
                subject,
                body,
                settings.DEFAULT_FROM_EMAIL,
                [cust_email]
            )        

    def handle_event(self, event):
        '''Handle a generic/unknown/unexpected webhook event'''
        return HttpResponse(
            content=f'Unhandled Webhook received: {event["type"]}',
            status=200)
    
    def handle_payment_intent_succeeded(self, event):
        '''Handle the payment_intent.succeeded webhook from Stripe'''
        intent = event.data.object
        pid = intent.id
        cart_obj = Cart.objects.get(id=uuid.UUID(intent.metadata['cart_id']))
        print(type(cart_obj.items))
        print(cart_obj.items)
        cart = cart_obj.items
        save_info = intent.metadata.save_info
        stripe_charge = stripe.Charge.retrieve(intent.latest_charge)
        billing_details = stripe_charge.billing_details
        total_price = round(stripe_charge.amount / 100, 2)

        # Clean data in the billing details
        for field, value in billing_details.address.items():
            if value == "":
                billing_details.address[field] = None

        # Update profile information if save_info was checked
        profile = None
        username = intent.metadata.username
        if username != 'AnonymousUser':
            profile = UserProfile.objects.get(user__username=username)
            if save_info:
                profile.default_phone_number = billing_details.phone
                profile.default_country = billing_details.address.country
                profile.default_town_or_city = billing_details.address.city
                profile.default_street_address1 = billing_details.address.line1
                profile.default_street_address2 = billing_details.address.line2
                profile.default_county = billing_details.address.state
                profile.save()
        
        
        order_exists = False
        attempt = 1
        while attempt <= 5:
            try:
                order = Order.objects.get(
                    full_name__iexact=billing_details.name,
                    email__iexact=billing_details.email,
                    phone_number__iexact=billing_details.phone,
                    country__iexact=billing_details.address.country,
                    town_or_city__iexact=billing_details.address.city,
                    street_address1__iexact=billing_details.address.line1,
                    street_address2__iexact=billing_details.address.line2,
                    county__iexact=billing_details.address.state,
                    total_price__exact=total_price,
                    original_cart=cart,
                    stripe_pid=pid,
                )
                order_exists = True
                break
            except Order.DoesNotExist:
                    print('Orders with same payment intent ID:', Order.objects.filter(stripe_pid=pid))
                    attempt += 1
                    time.sleep(1)

        if order_exists:
            self._send_confirmation_email(order)
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | SUCCESS: Verified order already in database',
                status=200)
        else:
            order= None
            try:
                order = Order.objects.create(
                    full_name=billing_details.name,
                    user_profile=profile,
                    email=billing_details.email,
                    phone_number=billing_details.phone,
                    country=billing_details.address.country,
                    town_or_city=billing_details.address.city,
                    street_address1=billing_details.address.line1,
                    street_address2=billing_details.address.line2,
                    county=billing_details.address.state,
                    total_price=total_price,
                    original_cart=cart,
                    stripe_pid=pid,
                )
                print('Order retrieved by webhook handler: ',order, order.stripe_pid, order.total_price, order.original_cart)
                for item_data in json.loads(cart):
                    menu_item_id = item_data.get('id')
                    menu_item = MenuItem.objects.get(id=menu_item_id)
                    
                    included_item = item_data.get('included_item')
                    quantity = item_data['quantity']

                    # Convert included_item to a MenuItemIncludedItem instance
                    if included_item is not None:
                        included_items = MenuItemIncludedItem.objects.filter(included_item__id=included_item['id'])
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

                    included_item_options = item_data.get('included_item_options')
                    if included_item_options is not None:
                        included_item_option_ids = [option['id'] for option in included_item_options]
                        order_line_item.included_item_options.set(included_item_option_ids)

                    included_item_extras = item_data.get('included_item_extras')
                    if included_item_extras is not None:
                        included_item_extra_ids = [extra['id'] for extra in included_item_extras]
                        order_line_item.included_item_extras.set(included_item_extra_ids)

                    options = item_data.get('options')
                    if options is not None:
                        option_ids = [option['id'] for option in options]
                        order_line_item.options.set(option_ids)

                    extras = item_data.get('extras')
                    if extras is not None:
                        extra_ids = [extra['id'] for extra in extras]
                        order_line_item.extras.set(extra_ids)

                    order_line_item.save()
            except Exception as e:
                if order:
                    order.delete()
                return HttpResponse(
                    content=f'Webhook received: {event["type"]} | ERROR: {e}',
                    status=500)
        self._send_confirmation_email(order)
        return HttpResponse(
            content=f'Webhook received: {event["type"]} | SUCCESS: Created order in webhook',
            status=200)
    
    def handle_payment_intent_payment_failed(self, event):
        '''Handle the payment_intent.payment_failed webhook from Stripe'''
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)
    

    