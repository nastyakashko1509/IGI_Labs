from django.core.exceptions import ValidationError
from django.utils import timezone
from django.db import models
from museum.models.BaseModel import BaseModel
from django.contrib.auth.models import User
import re


class Client(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, related_name='museum_client')
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    date_of_birth = models.DateField()
    phone = models.CharField(max_length=20)

    def clean(self):
        super().clean()  

        if self.phone:
            pattern = r'^\+375 \((25|29|33|44)\) \d{3}-\d{2}-\d{2}$'
            if not re.match(pattern, self.phone):
                raise ValidationError({
                    'phone': 'Номер телефона должен быть в формате +375 (29) XXX-XX-XX'
                })
            
        today = timezone.now().date()
        age = today.year - self.date_of_birth.year - ((today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day))
        if age < 18:
            raise ValidationError("Возраст клиента должен быть не менее 18 лет.")
