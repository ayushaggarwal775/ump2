from django import forms
from .models import User

class AddForm(forms.ModelForm):
    class Meta:
        model =  User
        fields = ['name','email','role']

class userAuth(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())
