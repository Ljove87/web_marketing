from django import forms

class ContactForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)
    your_email = forms.EmailField(label="Your email")
    your_url_adress = forms.URLField(max_length=200,)
