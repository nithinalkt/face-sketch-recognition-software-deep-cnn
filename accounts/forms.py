from django import forms
from .models import Officer, User


class UserForm(forms.ModelForm):
    """Form definition for User."""

    class Meta:
        """Meta definition for Userform."""

        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password')



class OfficerForm(forms.ModelForm):
    """Form definition for Officer."""

    class Meta:
        """Meta definition for Officerform."""

        model = Officer
        exclude = ['user']
