from django.shortcuts import render, get_object_or_404
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

def item_detail(request, item_id):
    item = get_object_or_404(MenuItem, pk=item_id)
    return render(request, 'orderonline/item_detail.html', {'item': item})

