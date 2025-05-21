from django.db import models
from museum.models.BaseModel import BaseModel
from museum.models.Exposition import Exposition
from museum.models.Employee import Employee
from museum.models.Hall import Hall
from museum.models.Ticket import Ticket


class Exhibition(BaseModel):  # Выставка.
    title = models.CharField(max_length=200)
    exposition = models.ManyToManyField(Exposition)
    hall = models.ForeignKey(Hall, on_delete=models.SET_NULL, null=True, related_name='exhibitions')
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    responsible_employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, related_name='exhibitions')
    ticket = models.ManyToManyField(Ticket, related_name='exhibitions')

    def __str__(self):
        return self.title
