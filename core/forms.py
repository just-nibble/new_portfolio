from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    full_name = forms.CharField(
        label="Full name",
        widget=forms.TextInput(
            attrs={
                    "id": "form_name",
                    "type": "text",
                    "class": "form-control",
                    "data-error": "Name is required"
                }
        ))
    email = forms.EmailField(
        label="Email",
        widget=forms.TextInput(
            attrs={
                    "id": "form_email",
                    "type": "email",
                    "class": "form-control",
                    "data-error": "Valid email is required"
                }
        ))
    subject = forms.CharField(
        label="Subject",
        widget=forms.TextInput(
            attrs={
                    "id": "form_subject",
                    "type": "text",
                    "class": "form-control",
                    "data-error": "Subject is required"
                }
        ))
    message = forms.CharField(
        label="Message",
        widget=forms.Textarea(
            attrs={
                    "id": "form_message",
                    "class": "form-control",
                    "rows": 7,
                    "data-error": "Please leave me a message"
                }
        ))
    class Meta:
        model = Contact
        fields = ["full_name", "email", "subject", "message"]

