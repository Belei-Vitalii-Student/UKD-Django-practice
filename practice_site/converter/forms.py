from django import forms

class ImageUploadForm(forms.Form):
    image = forms.ImageField()
    color = forms.CharField(widget=forms.TextInput(attrs={'type': 'color'}))