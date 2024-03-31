import uuid
from django.db import models
from django.db.models import Sum
from django.conf import settings
from django_countries.fields import CountryField

from orderonline.models import MenuItem, MenuItemIngredient, MenuItemIncludedItem
from profiles.models import UserProfile

import uuid
# Create your models here.


class Order(models.Model):
    order_number = models.CharField(max_length=32, null=False, editable=False)
    user_profile=models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True, blank=True, related_name='orders')
    full_name = models.CharField(max_length=50, blank=False)
    email = models.EmailField(max_length=254, blank=False)
    phone_number = models.CharField(max_length=20, blank=False)
    country = CountryField(blank_label='Country *',null=False, blank=False)
    town_or_city = models.CharField(max_length=40, blank=False)
    street_address1 = models.CharField(max_length=40, blank=False)
    street_address2 = models.CharField(max_length=40, blank=False)
    county = models.CharField(max_length=40, blank=True)
    date = models.DateField(auto_now_add=True)
    pickup_time = models.TimeField(auto_now_add=False, blank=True, null=True)
    order_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    original_cart = models.TextField(null=False, blank=False, default='')
    stripe_pid = models.CharField(max_length=254, null=False, blank=False, default='')

    def _generate_order_number(self):
        ''' Generate a random, unique order number using UUID '''
        return uuid.uuid4().hex.upper()
    
    def update_total(self):
        ''' Update grand total each time a line item is added, accounting for delivery costs '''
        self.order_total = self.lineitems.aggregate(Sum('lineitem_total'))['lineitem_total__sum'] or 0
        self.grand_total = self.order_total
        self.save()
    
    def save(self, *args, **kwargs):
        ''' Override the original save method to set the order number if it hasn't been set already '''
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number
    
class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, null=False, on_delete=models.CASCADE, related_name='lineitems')
    menu_item = models.ForeignKey(MenuItem, null=False, on_delete=models.CASCADE)
    included_item = models.ForeignKey(MenuItemIncludedItem, null=True, blank=True, on_delete=models.SET_NULL, related_name='+')
    included_item_options = models.ManyToManyField(MenuItemIngredient, related_name='+', blank=True)
    included_item_extras = models.ManyToManyField(MenuItemIngredient, related_name='+', blank=True)
    options = models.ManyToManyField(MenuItemIngredient, related_name='+', blank=True)
    extras = models.ManyToManyField(MenuItemIngredient, related_name='+', blank=True)
    item_price = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    quantity = models.IntegerField(blank=False)
    lineitem_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False, editable=False)

    def __str__(self):
        return f'SKU {self.menu_item.sku} on order {self.order.order_number}'
    
    def print_prices(self):
            print(f"Menu item price: {self.menu_item.price}")
            if self.included_item is not None:
                print(f"Included item price: {self.included_item.price}")
            for option in self.options.all():
                print(f"Option price: {option.price}")
            for extra in self.extras.all():
                print(f"Extra price: {extra.price}")
            if self.included_item is not None:
                for option in self.included_item_options.all():
                    print(f"Included item option price: {option.price}")
                for extra in self.included_item_extras.all():
                    print(f"Included item extra price: {extra.price}")
            print(f"Line item total: {self.lineitem_total}")

    
    def save(self, *args, **kwargs):
        """
        Override the original save method to set the line item total
        """
        self.lineitem_total = self.menu_item.price * self.quantity

        # Add the price of the included item, if it exists
        if self.included_item is not None:
            self.lineitem_total += self.included_item.price * self.quantity

        super().save(*args, **kwargs)  # Save the instance to generate an ID

        # Add the prices of the options and extras
        for option in self.options.all():
            self.lineitem_total += option.price * self.quantity
        for extra in self.extras.all():
            self.lineitem_total += extra.price * self.quantity

        # Add the prices of the included item options and extras, if the included item exists
        if self.included_item is not None:
            for option in self.included_item_options.all():
                self.lineitem_total += option.price * self.quantity
            for extra in self.included_item_extras.all():
                self.lineitem_total += extra.price * self.quantity

        super().save(*args, **kwargs)  # Save the instance again to update the lineitem_total




class Cart(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    items = models.TextField()  # Store the cart items as a JSON string
    
    def __str__(self):
        return str(self.id)