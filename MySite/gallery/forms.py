from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=150, label='Name: ')
    email = forms.EmailInput
    subject = forms.CharField(max_length=50, label='Subject: ', required=False)
    message = forms.CharField(label='Message: ')

