from django.db import models
from django.utils import timezone  # Текущее время.


class BaseModel(models.Model):
    created_at = models.DateTimeField(default=timezone.now)  # При создании объекта -> текущее время.
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True  # Абстрактная модель -> не будет создана в бд.
