from django import forms
from .models import UserProfile


class ProfileUserForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('age',)
