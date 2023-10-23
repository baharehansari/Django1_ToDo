from django import forms
from .models import ToDo
from django.forms import ModelForm

# Create your models here.
class Form(forms.Form):
    title= forms.CharField(required=False)
    body= forms.CharField(required=False)
    dateCreate= forms.DateTimeField(required=False)
    

class updateForm(forms.ModelForm):
    class Meta:
        model=ToDo
        fields=('title','body','dateCreate')
