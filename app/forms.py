from django import forms
from django.utils.translation import gettext as _
from .models import ContactMessage


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message']

        widgets = {
            'name': forms.TextInput(
                attrs={'class': 'px-2 py-2 border w-full outline-none rounded-md font-bold', 'required': 'required'}),
            'email': forms.EmailInput(
                attrs={'class': 'px-2 py-2 border w-full outline-none rounded-md font-bold', 'required': 'required'}),
            'message': forms.Textarea(
                attrs={'class': 'px-2 py-2 border rounded-[5px] w-full outline-none font-bold',
                       'required': 'required'}),
        }

        labels = {
            'name': _('Name'),
            'email': _('Email'),
            'message': _('Message'),
        }
