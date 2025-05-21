from django.db import models
from museum.models.Exhibition import Exhibition
from museum.models.Employee import Employee
from museum.models.BaseModel import BaseModel
from museum.models.Ticket import Ticket


class Tour(BaseModel):  # Экскурсия.
    title = models.CharField(max_length=100)
    topic = models.CharField(max_length=100)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    ticket_prices = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    responsible_employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, related_name='tours')
    exhibitions = models.ManyToManyField(Exhibition, related_name='tours')
    ticket = models.ManyToManyField(Ticket, related_name='tours')
    group_size = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title
    