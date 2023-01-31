from django import forms

class ContactForm(forms.Form):
    nume = forms.CharField()
    email = forms.EmailField()
    mesaj = forms.CharField()
    multumit = forms.BooleanField()