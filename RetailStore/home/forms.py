from django import forms

class RegisterForm(forms.Form):
    Name = forms.CharField(label='Name', max_length=100)
    Address = forms.CharField(label='Address', max_length=500)
    Contact = forms.CharField(label='Contact', max_length=10)
    Email = forms.EmailField(label='Email', max_length=100)

class BillingStartForm(forms.Form):
    Contact = forms.CharField(label='Contact', max_length=10)
