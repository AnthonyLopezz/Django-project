from django import forms


class FormContact(forms.Form):
    name = forms.CharField(label="Name", required=True, max_length=25,
                           widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}))
    email = forms.CharField(label="Email", required=True,
                            widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Email'}))
    message = forms.CharField(label="Message", required=True,
                              widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Your Message'}))
