from django.db import models
from museum.models.BaseModel import BaseModel


class Ticket(BaseModel):
    name = models.CharField(null=True, blank=True, max_length=50)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    AGE_CHOICES = [
        ('baby', '0-5 лет'),
        ('child', '5-18 лет'),
        ('adult', 'от 18 лет'),
    ]
    visitor_age = models.CharField(choices=AGE_CHOICES)
    DAY_CHOICES = [
        ('weekday', 'Будний день'),
        ('weekend', 'Выходной'),
        ('holiday', 'Праздник'),
    ]
    day_type = models.CharField(max_length=10, choices=DAY_CHOICES)
    photo_permission_fee = models.BooleanField(default=False)

    def __str__(self):
        return f'Билет ({self.get_day_type_display()}) - {self.price}₽ + Фото: {self.photo_permission_fee}₽'
