from django.db import models
from museum.models.BaseModel import BaseModel


class Hall(BaseModel):  # Холл.
    name = models.CharField(max_length=50)
    floor = models.IntegerField()
    square = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return f"{self.name} (этаж {self.floor})"
