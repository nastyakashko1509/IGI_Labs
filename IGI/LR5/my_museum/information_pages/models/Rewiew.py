from django.db import models
from django.contrib.auth.models import User
from museum.models.BaseModel import BaseModel


class Review(BaseModel):  # Отзывы.
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author.username} — {self.rating}/5"
