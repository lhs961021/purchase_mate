from django.contrib.auth.models import User
from django import forms
from .models import Profile


class SignupForm(forms.Form):
    model = User

    name = forms.CharField(label="이름")
    phnum = forms.CharField(label="휴대폰 번호")
    address = forms.CharField(label="자취방 주소")

    def signup(self, request, user):
        profile = Profile()
        profile.user = user
        profile.name = self.cleaned_data["name"]
        profile.phnum = self.cleaned_data["phnum"]
        profile.address = self.cleaned_data["address"]
        profile.save()
        user.save()
        return user