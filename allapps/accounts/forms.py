from django import forms
from django.db.models import Q
from django.utils.safestring import mark_safe
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, ReadOnlyPasswordHashField


class AddUserForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'password1', 'password2')


class UpdateUserForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField(
        label=("Password"),
        help_text=mark_safe(
            "Raw passwords are not stored, so there is no way that you can see \
            your current password, but you can reset your password \
            using <a href=\"/accounts/password_reset/\">this form</a>."
        ),
    )

    class Meta:
        model = get_user_model()
        fields = (
            'username', 'password', 'email', 'first_name', 'last_name'
        )

    field_order = ['username', 'password', 'email', 'first_name', 'last_name']

    def clean_password(self):
        return self.initial["password"]


class LoginUserForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': '', 'name': 'username'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': '',
            'name': 'password'
        }
    ))

    def __init__(self, *args, **kwargs):
        super(LoginUserForm, self).__init__(*args, **kwargs)
