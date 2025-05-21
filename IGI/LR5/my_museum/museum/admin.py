from django.contrib import admin
from .models import *


models = (
    ArtType, Employee, Exhibit,
    Exhibition, Exposition, Hall,
    Position, Tour, Ticket, Client, Purchase)

admin.site.register(Employee)
admin.site.register(ArtType)
admin.site.register(Exhibit)
admin.site.register(Exhibition)
admin.site.register(Exposition)
admin.site.register(Hall)
admin.site.register(Position)
admin.site.register(Tour)
admin.site.register(Ticket)
admin.site.register(Client)
admin.site.register(Purchase)
