from django import forms


class ImageForm(forms.Form):
    file = forms.ImageField()
    overwrite = forms.BooleanField(required=False)


class FileForm(forms.Form):
    file = forms.FileField()
    overwrite = forms.BooleanField(required=False)
