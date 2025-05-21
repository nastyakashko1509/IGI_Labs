from django.db import models
from museum.models.BaseModel import BaseModel


class FAQ(BaseModel):  # Словарь терминов и понятий.
    question = models.CharField(max_length=255)
    answer = models.TextField(blank=True, null=True)
    added_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.question
