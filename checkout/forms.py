from django import forms

class CheckoutForm(forms.Form):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    address = forms.CharField(max_length=100)
    city = forms.CharField(max_length=50)
    postal_code = forms.CharField(max_length=10)
    country = forms.CharField(max_length=50)
    save_info = forms.BooleanField(required=False)