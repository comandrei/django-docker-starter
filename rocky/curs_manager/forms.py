from django import forms
from django.core.exceptions import ValidationError

from .models import Curs

class ContactForm(forms.Form):
    nume = forms.CharField(label="Numele tau")
    email = forms.EmailField()
    mesaj = forms.CharField(widget=forms.Textarea(attrs={"rows": "5", "class": "black"}))
    multumit = forms.BooleanField(required=False)

    def clean_email(self):
        value = self.cleaned_data["email"]
        if not value.endswith("@gmail.com"):
            raise ValidationError("Trebuie sa fie o adresa gmail")


class CursForm(forms.ModelForm):
    class Meta:
        model = Curs
        fields = "__all__"
