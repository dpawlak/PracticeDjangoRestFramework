from django import forms 
from .models import Prescriptions

class PrescriptionsForm(forms.ModelForm):
    class Meta:
        model = Prescriptions
        fields = "__all__"

        