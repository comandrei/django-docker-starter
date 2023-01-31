from django import forms
from django.core.exceptions import ValidationError

class ContactForm(forms.Form):
    nume = forms.CharField()
    email = forms.EmailField()
    mesaj = forms.CharField()
    multumit = forms.BooleanField(required=False)

    def clean_email(self):
        value = self.cleaned_data["email"]
        if not value.endswith("@gmail.com"):
            raise ValidationError("Trebuie sa fie o adresa gmail")
