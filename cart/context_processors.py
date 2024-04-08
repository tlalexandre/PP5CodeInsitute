from .views import get_cart_total_price


def cart_total_price(request):
    '''A context processor to add the cart total price to the context.'''
    cart = request.session.get('cart', {})
    return {'cart_total_price': get_cart_total_price(cart)}
