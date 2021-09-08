from django import forms
from .models import Image


class ImageForm(forms.ModelForm):
    color = forms.CharField(max_length=16)

    class Meta:
        model = Image
        fields = ('image',)

