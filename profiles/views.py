from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserProfileForm
from .models import Profile



@login_required
def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            profile, created = Profile.objects.get_or_create(user=request.user)
            profile.first_name = form.cleaned_data['first_name']
            profile.last_name = form.cleaned_data['last_name']
            profile.address = form.cleaned_data['address']
            profile.city = form.cleaned_data['city']
            profile.postal_code = form.cleaned_data['postal_code']
            profile.country = form.cleaned_data['country']
            profile.save()
            return redirect('profile')
    else:
        profile, created = Profile.objects.get_or_create(user=request.user)
        form = UserProfileForm(initial={
            'first_name': profile.first_name,
            'last_name': profile.last_name,
            'address': profile.address,
            'city': profile.city,
            'postal_code': profile.postal_code,
            'country': profile.country,
        })
    return render(request, 'profiles/profile.html', {'form': form})

