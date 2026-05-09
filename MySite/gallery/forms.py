from django import forms
import re

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from captcha.fields import CaptchaField


class ContactForm(forms.Form):

    name = forms.CharField(
        max_length=150,
        label=_('Name'),
        widget=forms.TextInput(
            attrs={
                'class': 'form-control mb-3',
                'placeholder': _('Name')
            }
        )
    )

    email = forms.CharField(
        max_length=50,
        label=_('Email'),
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control mb-3',
                'placeholder': _('Email')
            }
        )
    )

    subject = forms.CharField(
        max_length=50,
        required=False,
        label=_('Subject'),
        widget=forms.TextInput(
            attrs={
                "class": "form-control mb-3",
                'placeholder': _('Subject')
            }
        )
    )

    message = forms.CharField(
        max_length=500,
        label=_('Message'),
        widget=forms.Textarea(
            attrs={
                "class": "form-control mb-3",
                "rows": 5,
                'placeholder': _('Write your message')
            }
        )
    )

    captcha = CaptchaField(
        label=_('Captcha')
    )

    def clean_name(self):

        name = self.cleaned_data['name']

        if re.match(r'\d', name):

            raise ValidationError(
                _("Your name shouldn't contain any number")
            )

        return name
