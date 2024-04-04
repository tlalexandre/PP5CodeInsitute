from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages


def index(request):
    """ A view to return the index page """
    return render(request, 'home/index.html')


def about(request):
    """ A view to return the about page """
    return render(request, 'about/about.html')


def menu(request):
    """ A view to return the menu page """
    return render(request, 'menu/menu.html')


def contact(request):
    """ A view to return the contact page """
    if request.method == 'POST':
        form = ContactForm(request.POST, user=request.user)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            message = form.cleaned_data.get('message')
            full_message = f"Message from {name} ({email}):\n\n{message}"
            try:
                send_mail(
                    'Contact Form Submission from ' + name,
                    full_message,
                    settings.EMAIL_HOST_USER,
                    [settings.EMAIL_HOST_USER],
                    fail_silently=False,
                )
            except Exception as e:
                print(e)
                messages.error(
                    request, 'There was an error sending the email.')
                return render(request, 'contact/contact.html', {'form': form})
            messages.success(
                request, 'Your message has been sent successfully!')
            return render(request, 'contact/contact_success.html')
        else:
            print(form.errors)
    else:
        form = ContactForm(user=request.user)

    return render(request, 'contact/contact.html', {'form': form})


def contact_success(request):
    """ A view to return the contact success page """

    return render(request, 'contact/contact_success.html')
