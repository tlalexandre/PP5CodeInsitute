from django.shortcuts import render

# Create your views here.

def index(request):
    """ A view to return the index page """
    
    return render(request, 'home/index.html')


def about(request):
    """ A view to return the about page """
    
    return render(request, 'about/about.html')

def menu(request):
    """ A view to return the menu page """
    
    return render(request, 'menu/menu.html')