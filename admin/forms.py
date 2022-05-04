from django import forms
from accounts.models import CaseType

class CaseTypeForm(forms.ModelForm):
    """Form definition for CaseType."""

    class Meta:
        """Meta definition for CaseTypeform."""

        model = CaseType
        fields = '__all__'
