import os

from django.contrib.auth import get_user_model
from django.db import models
from django.template.defaultfilters import slugify

class Disease(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f"{self.name}"

class Modality(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f"{self.name}"

class Dataset(models.Model):
    def file_upload_to(self, instance=None):
        if instance:
            return os.path.join("datasets", slugify(self.author), instance)
        return None

    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        get_user_model(), default=1, on_delete=models.SET_DEFAULT)
    disease = models.ForeignKey(Disease, on_delete=models.PROTECT)
    modality = models.ForeignKey(Modality, on_delete=models.PROTECT)
    description = models.TextField()
    reference = models.URLField()
    measurable_index = models.CharField(max_length=100)
    zipfile = models.FileField(upload_to=file_upload_to, max_length=255)

    def __str__(self):
        return f'{self.author}-{self.title}-{self.description} ({self.zipfile})'
