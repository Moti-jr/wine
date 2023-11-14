from django.forms import forms


class LoginForm(forms.form):
    username=forms.charfield(max_lenght=50)
    password=forms.forms.charField(max_length=50, widget=forms.PasswordInput)