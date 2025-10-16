from django import forms
from django.core.mail import send_mail


class ContactForm(forms.Form):
    name = forms.CharField(max_length=120, widget=forms.TextInput(attrs={'placeholder':'Your name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':'Your email'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Your message'}))


# Optionally implement a save() that sends email
def save(self):
    data = self.cleaned_data
    send_mail(
    f"Portfolio message from {data['name']}",
    data['message'],
    data['email'],
    ['kingsleycodes247@gmail.com']
    )
