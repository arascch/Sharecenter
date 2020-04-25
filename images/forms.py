from django import forms
from .models import Image

class ImageCreateForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('title' , 'url' , 'description')
        widget = {
            'url' : forms.HiddenInput,
        }
    
    def clean_url(self):
        url = self.cleaned_data['url']
        valid_extensions = ['jpg' , 'jpeg']
        extension = url.rsplit('.' , 1)[1].lower()
        if extension not in valid_extensions:
            raise forms.ValidationError('the given url does not match valid image extensions.')
        return url