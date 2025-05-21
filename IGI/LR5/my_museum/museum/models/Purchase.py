from django.db import models
from museum.models.BaseModel import BaseModel
from museum.models.Ticket import Ticket
from museum.models.Client import Client

class Purchase(BaseModel):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='purchases')
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    purchase_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.client.full_name} - {self.ticket} ({self.purchase_date.strftime('%Y-%m-%d %H:%M')})"
