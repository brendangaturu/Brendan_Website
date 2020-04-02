from django import forms
from crispy_forms.helper import FormHelper

#TODO: makeover the contact form
class ContactForm(forms.Form):
    """Email contact form"""
    helper = FormHelper()
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'placeholder': 'Enter Your Email'}))
    name = forms.CharField(required=True,  widget=forms.TextInput(attrs={'placeholder': 'Your name'}))
    message = forms.CharField(required=True, widget=forms.Textarea())
