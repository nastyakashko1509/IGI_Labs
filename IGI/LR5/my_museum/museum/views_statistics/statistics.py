from django.db.models import Sum, F, Case, When, Value, DecimalField
from statistics import mean, median, mode, StatisticsError
from museum.models import Purchase, Client
from django.shortcuts import render
from django.utils import timezone
from collections import Counter
import logging


logger = logging.getLogger(__name__)

def statistics_view(request):
    logger.info("Запрос к странице со статистикой")
    clients = Client.objects.all().order_by('full_name')
    purchases = Purchase.objects.select_related('ticket').all()

    total_sales = Purchase.objects.annotate(
        full_price=F('ticket__price') + Case(
            When(ticket__photo_permission_fee=True, then=Value(5.00)),  # Например, 5₽ за фото
            default=Value(0.00),
            output_field=DecimalField()
        )
    ).aggregate(total=Sum('full_price'))['total'] or 0

    sales_amounts = [p.ticket.price for p in purchases]

    avg_sale = mean(sales_amounts) if sales_amounts else 0
    med_sale = median(sales_amounts) if sales_amounts else 0
    try:
        mode_sale = mode(sales_amounts) if sales_amounts else 0
    except StatisticsError:
        mode_sale = "Мода не определена (все значения уникальны)"

    today = timezone.now().date()
    client_ages = [
        today.year - client.date_of_birth.year - ((today.month, today.day) < (client.date_of_birth.month, client.date_of_birth.day))
        for client in clients
    ]

    avg_age = round(mean(client_ages), 2) if client_ages else 0
    med_age = round(median(client_ages), 2) if client_ages else 0

    ticket_type_counter = Counter(p.ticket.name for p in purchases)
    if ticket_type_counter:
        most_popular_ticket_type = ticket_type_counter.most_common(1)[0][0]
    else:
        most_popular_ticket_type = "Нет данных"

    profit_by_type = {}
    for p in purchases:
        key = p.ticket.name
        profit_by_type[key] = profit_by_type.get(key, 0) + p.ticket.price
    if profit_by_type:
        most_profitable_type = max(profit_by_type.items(), key=lambda x: x[1])[0]
    else:
        most_profitable_type = "Нет данных"

    return render(request, 'statistics.html', {
        'clients': clients,
        'total_sales': total_sales,
        'avg_sale': avg_sale,
        'med_sale': med_sale,
        'mode_sale': mode_sale,
        'avg_age': avg_age,
        'med_age': med_age,
        'most_popular_ticket_type': most_popular_ticket_type,
        'most_profitable_type': most_profitable_type,
    })
