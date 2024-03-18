from .views import get_cart_total_price

def cart_total_price(request):
    cart= request.session.get('cart', {})
    return {'cart_total_price': get_cart_total_price(cart)}

