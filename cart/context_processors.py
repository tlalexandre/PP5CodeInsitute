
from .views import get_cart_total_price, get_cart_items

def cart_total_price(request):
    cart= request.session.get('cart', {})
    return {'cart_total_price': get_cart_total_price(cart)}

def cart_items(request):
    # Your code to get cart items goes here
    cart_items = get_cart_items(request)
    return {'cart_items': cart_items}