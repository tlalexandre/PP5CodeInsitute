from django import forms


class ContactForm(forms.Form):
    '''A form to allow users to contact the site owner.'''
    name = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=100, required=True)
    message = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'non-resizable'})
    )

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(ContactForm, self).__init__(*args, **kwargs)
        if user and user.is_authenticated:
            self.fields['name'].initial = user.username
            self.fields['email'].initial = user.email


