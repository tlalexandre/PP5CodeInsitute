
from .views import get_cart_total_price

def cart_total_price(request):
    return {'cart_total_price': get_cart_total_price(request)}