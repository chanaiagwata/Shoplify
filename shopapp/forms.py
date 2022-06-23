from .models import *
from django import forms

class DetailsForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user','product']
        
class addProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ['description']

class NewsLetterForm(forms.Form):
    your_name = forms.CharField(label='First Name',max_length=30)
    email = forms.EmailField(label='Email')