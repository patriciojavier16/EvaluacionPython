from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Page(models.Model):
    title=models.CharField(max_length=100, verbose_name="Titulo")
    content=RichTextField(verbose_name="Contenido")
    created=models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated=models.DateTimeField(auto_now_add=True, verbose_name="Fecha de modificación")

    class Meta:
        verbose_name="Página"
        verbose_name_plural="Páginas"
        ordering=["created"]

    def __str__(self):
        return self.title