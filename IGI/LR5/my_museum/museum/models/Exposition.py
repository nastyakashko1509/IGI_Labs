from django.db import models
from museum.models.BaseModel import BaseModel
from museum.models.Exhibit import Exhibit


class Exposition(BaseModel):  # Экспозиция.
    name = models.CharField(max_length=200)
    description = models.TextField()
    exhibits = models.ManyToManyField(Exhibit, related_name="expositions")

    def __str__(self):
        return self.name
