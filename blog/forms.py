from .models import Comment
from django import forms
from django.core.validators import EmailValidator


class ContactForm(forms.Form):
    name = forms.CharField(max_length=30)
    email = forms.EmailField(validators=[EmailValidator()])
    subject = forms.CharField(max_length=100, required=False)  # Optional subject field
    message = forms.CharField(widget=forms.Textarea(attrs={'rows': 3, 'cols': 30}))
    phone_number = forms.CharField(max_length=15, required=False)  # Optional phone number field


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)