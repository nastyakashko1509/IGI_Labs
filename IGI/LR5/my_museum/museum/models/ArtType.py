from django.db import models
from museum.models.BaseModel import BaseModel


class ArtType(BaseModel):  # Вид искусства.
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.name
