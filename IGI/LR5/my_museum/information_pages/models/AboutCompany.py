from django.db import models
from museum.models.BaseModel import BaseModel


class AboutCompany(BaseModel):  # О компании.
    content = models.TextField()

    def __str__(self):
        return self.content