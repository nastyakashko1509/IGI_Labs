from django.db import models
from museum.models.BaseModel import BaseModel


class News(BaseModel):  # Новости и главная страница (= последняя новость).
    title = models.CharField(max_length=255)
    short_description = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to='photos/news_images/')
    published_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
