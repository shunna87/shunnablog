from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.
class Imprint(models.Model):
    content = RichTextField()

    class Meta:
        """Meta definition for Imprint."""

        verbose_name = 'Imprint'
        verbose_name_plural = 'Imprints'

