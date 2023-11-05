from django.db import models
from django.core import validators

# Create your models here.
class Files(models.Model):
    file = models.FileField(upload_to='files',verbose_name='Файл',
        validators=[validators.FileExtensionValidator(allowed_extensions=('pdf','xlsx'))],
        error_messages={'invalid_extension':'Этот формат не поддерживается!'})
    
    def __str__(self):
        return self.file.url