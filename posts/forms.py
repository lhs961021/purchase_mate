from django import forms
from django.forms import fields
from .models import Spot

class SpotForm(forms.ModelForm):
    spot = forms.CharField(label='')
    class Meta:
        model = Spot
        fields = ['spot', ]