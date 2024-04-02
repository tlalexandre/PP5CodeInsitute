from django.shortcuts import render, redirect
from django.conf import settings
from mailchimp3 import MailChimp
from django.contrib import messages


def handler404(request, exception):
    ''' Error Handler 404- Page Not Found'''
    return render(request, 'errors/404.html',{}, status=404)

def subscribe_email(request):
    if request.method == 'POST':
        email = request.POST['email']
        client = MailChimp(mc_api=settings.MAILCHIMP_API_KEY, mc_user='tanguy.lalexandre@gmail.com')
        try:
            client.lists.members.create(settings.MAILCHIMP_LIST_ID, {
                'email_address': email,
                'status': 'subscribed',
            })
            messages.success(request, 'You have been successfully subscribed to the newsletter.')
        except Exception as e:
            messages.error(request, 'There was an error subscribing to the newsletter.')
            
    return render(request, 'home/index.html')