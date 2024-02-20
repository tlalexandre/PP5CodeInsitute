from django.shortcuts import render
from .models import MenuCategory

# Create your views here.

def order_online(request):
    """ A view to return the order online page """
    
    categories = MenuCategory.objects.all()

    return render(request, 'orderonline/orderonline.html', {'categories': categories})

