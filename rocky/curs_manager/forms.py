from django import forms
from django.core.exceptions import ValidationError

from .models import Curs, Student

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
        #fields = "__all__"
        fields = ["nume", "an"] # exclude = ["profesor"]

    #profesor = forms.CharField(label="Numele profesorului", widget=forms.TextInput(attrs={"placeholder": "numele profesorului"}))

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"

    def clean_nume(self):
        value = self.cleaned_data["nume"]
        if value[0].islower():
            raise forms.ValidationError("Numele trebuie sa inceapa cu litera mare")

