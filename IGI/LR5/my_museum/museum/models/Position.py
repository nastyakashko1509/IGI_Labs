from django.db import models
from museum.models.BaseModel import BaseModel


class Position(BaseModel):  # Должность.
    title = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.title
    