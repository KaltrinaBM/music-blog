from django.core.validators import EmailValidator
from django import forms
from .models import Comment, ContactFormEntry


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactFormEntry
        fields = ('name', 'email', 'subject', 'message', 'phone_number',)  


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)