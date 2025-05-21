from django.db import models
from museum.models.BaseModel import BaseModel


class PromoCode(BaseModel):  # Купоны и промокоды.
    code = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    is_active = models.BooleanField(default=True)
    valid_until = models.DateField()

    def __str__(self):
        return self.code
