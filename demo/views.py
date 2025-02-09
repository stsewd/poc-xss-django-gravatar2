from django import forms
from django.contrib.auth.models import User
from django.shortcuts import render


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["first_name", "email"]
        widgets = {"email": forms.TextInput()}


def index(request):
    form = UserForm(request.GET)
    return render(request, "index.html", {"form": form})
