from django import forms
from accounts.models import Station, User
from .models import Criminal,ImageSearch

class StationUserForm(forms.ModelForm):
    """Form definition for User."""

    class Meta:
        """Meta definition for Userform."""

        model = User
        fields = ('email','username','password')

class StationForm(forms.ModelForm):
    """Form definition for Station."""

    class Meta:
        """Meta definition for Stationform."""

        model = Station
        fields = ['phone']


class CriminalForm(forms.ModelForm):
    """Form definition for Criminal."""

    class Meta:
        """Meta definition for Criminalform."""

        model = Criminal
        exclude = ['city', 'user']

class ImageSearchForm(forms.ModelForm):
    """Form definition for ImageSearch."""

    class Meta:
        """Meta definition for ImageSearchform."""

        model = ImageSearch
        fields = ('image',)



