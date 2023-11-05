from django.forms import ModelForm
from django import forms
from django.core import validators
from app.models import Files

class FileUpload(ModelForm):
    file = forms.FileField(validators=[validators.FileExtensionValidator(allowed_extensions=('pdf','xlsx'))],
        error_messages={'invalid_extension':'Этот формат не поддерживается!'})

    class Meta:
        model = Files
        fields = ('file',)