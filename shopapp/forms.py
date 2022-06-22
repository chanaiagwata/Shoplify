from .models import *
from django import forms

class DetailsForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user','product']