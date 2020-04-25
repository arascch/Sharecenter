from django import forms
from .models import Image

class ImageCreateForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('title' , 'url' , 'description')
        widget = {
            'url' : forms.HiddenInput,
        }