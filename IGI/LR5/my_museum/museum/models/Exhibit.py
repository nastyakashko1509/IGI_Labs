from django.db import models
from museum.models.BaseModel import BaseModel
from museum.models.Hall import Hall
from museum.models.ArtType import ArtType


class Exhibit(BaseModel):  # Экспонат.
    title = models.CharField(max_length=200)
    description = models.TextField()
    art_type = models.ForeignKey(ArtType, on_delete=models.SET_NULL, null=True)
    hall = models.ForeignKey(Hall, on_delete=models.SET_NULL, null=True)
    creation_date = models.DateField()
    author = models.CharField(max_length=100, blank=True)
    photo = models.ImageField(upload_to='photos/exhibits/')

    def __str__(self):
        return self.title
