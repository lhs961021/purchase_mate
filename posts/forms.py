from django import forms
from django.forms import fields
from .models import Spot
from .models import Search


class SpotForm(forms.ModelForm):
    spot = forms.CharField(label='')
    class Meta:
        model = Spot
        fields = ['spot', ]

class SearchForm(forms.ModelForm):
    address = forms.CharField(label='')
    class Meta:
        model = Search
        fields = ['address', ]