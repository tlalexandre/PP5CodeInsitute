from django.shortcuts import render
from .models import MenuCategory, MenuItem

# Create your views here.

def order_online(request):
    """ A view to return the order online page """
    
    categories = MenuCategory.objects.all()

    items= MenuItem.objects.all()
    
    context= {
        'categories': categories,
        'items': items,
    }

    return render(request, 'orderonline/orderonline.html', context)

