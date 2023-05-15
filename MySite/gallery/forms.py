from django import forms
import re
from django.core.exceptions import ValidationError


class ContactForm(forms.Form):
    
    name = forms.CharField(max_length=150, label='Name', widget=forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Name'}))
    email = forms.CharField(max_length=50, label='Email', widget=forms.EmailInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Email'}))
    subject = forms.CharField(max_length=50, label='Subject', required=False, widget=forms.TextInput(attrs={"class": "form-control mb-3", 'placeholder': 'Subject'}))
    message = forms.CharField(max_length=500, label='Message', widget=forms.Textarea(attrs={"class": "form-control mb-3", "rows": 5, 'placeholder': 'Write your message'}))
    
    


def clean_name(self):
    name = self.cleaned_data['name']

    if re.match(r'\d', name):
        raise ValidationError("Your name shouldn't contain any number")
    
    return name
