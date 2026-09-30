from django import forms

from Loginify.models import UserDetails


class LoginForm(forms.ModelForm):
    class Meta:
        model = UserDetails
        fields = ['username', 'email', 'password']

        
