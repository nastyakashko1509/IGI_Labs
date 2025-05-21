from django.db import models
from django.contrib.auth.models import User as AdmUser
from museum.models.BaseModel import BaseModel
from museum.models.Hall import Hall
from museum.models.Position import Position
import re
from django.core.exceptions import ValidationError
from django.utils import timezone


class Employee(BaseModel):  # Сотрудник.
    user = models.OneToOneField(AdmUser, on_delete=models.CASCADE, default=None, null=True, blank=True, related_name='museum_employee')
    full_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    bio = models.TextField()
    photo = models.ImageField(upload_to='photos/employees/', default=None, null=True)
    position = models.ForeignKey(Position, on_delete=models.SET_NULL, null=True, related_name="employees")
    halls = models.ManyToManyField(Hall, related_name="employees")
    work_description = models.TextField(blank=True)
    date_of_birth = models.DateField()

    def __str__(self):
        return f"{self.full_name}"
    
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
            raise ValidationError("Возраст сотрудника должен быть не менее 18 лет.")
