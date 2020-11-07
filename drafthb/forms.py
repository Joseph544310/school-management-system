from django import forms


class LoginForm(forms.Form):

    Username = forms.CharField(label='Username')
    Password = forms.CharField(label='Password', widget=forms.PasswordInput)
