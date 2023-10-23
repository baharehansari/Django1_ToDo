from django import forms

# Create your models here.
class UserRegisterForm(forms.Form):
    username= forms.CharField()
    email=forms.EmailField()
    password= forms.CharField()
    name=forms.CharField()
    family=forms.CharField()


class UserLoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField()
