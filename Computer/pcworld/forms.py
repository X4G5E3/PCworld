from django import forms
from .models import Contact
from django.contrib.auth.models import User
from django.urls import reverse_lazy

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']
    
    def get_succes_url(self):
        return reverse_lazy('login')
    
class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ['first_name', 'subject', 'email', 'message']
