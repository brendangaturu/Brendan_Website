from django import forms
from crispy_forms.helper import FormHelper


class ContactForm(forms.Form):
    """Email contact form"""
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Name'}))
    email = forms.EmailField(required=True)
    message = forms.CharField(required=True, widget=forms.Textarea())
