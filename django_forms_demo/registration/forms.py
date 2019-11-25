from django import forms

from django.core import validators


# Custom_Validator


def check_size(value):
    if len(value) < 6:
        raise forms.ValidationError("Length is too short")


class SignUp(forms.Form):

    first_name = forms.CharField(
        initial='First Name', max_length=10, required=True)
    last_name = forms.CharField(
        initial='Last Name', max_length=10, required=True)
    email = forms.EmailField(
        help_text='Write your email', required=True)
    Address = forms.CharField(
        max_length=50, required=False, validators=[check_size], widget=forms.Textarea)
    technology = forms.CharField(
        initial='Django', disabled=True)
    password = forms.CharField(
        widget=forms.PasswordInput, required=True, validators=[validators.MinLengthValidator(6)])
    re_password = forms.CharField(
        help_text='Renter your password', widget=forms.PasswordInput, required=True)

    def clean_password(self):
        password = self.cleaned_data['password']
        if len(password) < 4:
            raise forms.ValidationError("password is too short")
        return password
