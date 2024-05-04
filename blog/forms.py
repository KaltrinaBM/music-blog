"""
Forms for the blog application.

Defines a contact form for users to submit inquiries and a comment form for submitting comments on blog posts.
"""

from django.core.validators import EmailValidator
from django import forms
from .models import Comment, ContactFormEntry


class ContactForm(forms.ModelForm):
    """
    A form for users to contact the Music blog team.

    - Uses the ContactFormEntry model.
    - Includes fields for name, email, subject, message, and phone number.
    """
    class Meta:
        model = ContactFormEntry
        fields = ('name', 'email', 'subject', 'message', 'phone_number',)


class CommentForm(forms.ModelForm):
    """
    A form for submitting comments on blog posts.

    - Uses the Comment model.
    - Only contains the body field for the comment content.
    """
    class Meta:
        model = Comment
        fields = ('body',)
