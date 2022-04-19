from django.db import models
from ckeditor.fields import RichTextField
from django.utils import timezone

# Create your models here.

class Post (models.Model):
    titulo= models.CharField(max_length=40)
    subtitulo = models.CharField(max_length=40)
    cuerpo = RichTextField(null=True)
    fecha_creacion = models.DateTimeField(default=timezone.now)
    imagen = models.ImageField(upload_to= 'blogimagen',null=True)

    def __str__(self):
        return f'{self.titulo} {self.subtitulo}'


