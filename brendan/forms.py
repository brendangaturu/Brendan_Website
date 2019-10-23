from django import forms

class ContactForm(forms.Form):
    """Email contact form"""
    name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    message = forms.CharField(required=True, widget=forms.Textarea)