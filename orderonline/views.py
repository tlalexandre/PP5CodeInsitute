from django.shortcuts import render

# Create your views here.

def order_online(request):
    """ A view to return the order online page """
    
    return render(request, 'orderonline/orderonline.html')