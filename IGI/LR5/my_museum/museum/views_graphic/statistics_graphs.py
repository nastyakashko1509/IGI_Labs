from django.http import HttpResponse
from django.shortcuts import render
from museum.models import Purchase
from django.db.models import Count
import matplotlib.pyplot as plt
from io import BytesIO
import logging


logger = logging.getLogger(__name__)

def sales_by_visitor_age_chart(request):
    data = Purchase.objects.values('ticket__visitor_age').annotate(count=Count('id'))
    categories = [item['ticket__visitor_age'] for item in data]
    counts = [item['count'] for item in data]

    labels = {'baby': '0-5 лет', 'child': '5-18 лет', 'adult': 'от 18 лет'}
    labels_display = [labels.get(cat, cat) for cat in categories]

    plt.figure(figsize=(8, 5))
    plt.bar(labels_display, counts, color='sandybrown')
    plt.title('Продажи билетов по возрастным категориям')
    plt.xlabel('Возрастная категория')
    plt.ylabel('Количество продаж')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()

    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    plt.close()
    buffer.seek(0)
    return HttpResponse(buffer.getvalue(), content_type='image/png')

def sales_by_day_type_chart(request):
    data = Purchase.objects.values('ticket__day_type').annotate(count=Count('id'))
    categories = [item['ticket__day_type'] for item in data]
    counts = [item['count'] for item in data]

    labels = {'weekday': 'Будний день', 'weekend': 'Выходной', 'holiday': 'Праздник'}
    labels_display = [labels.get(cat, cat) for cat in categories]

    plt.figure(figsize=(8, 5))
    plt.pie(counts, labels=labels_display, autopct='%1.1f%%', startangle=140, colors=['#f4a261', '#e76f51', '#2a9d8f'])
    plt.title('Распределение продаж по типам дней')
    plt.tight_layout()

    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    plt.close()
    buffer.seek(0)
    return HttpResponse(buffer.getvalue(), content_type='image/png')

def sales_over_time_chart(request):
    data = Purchase.objects.extra({'purchase_day': "date(purchase_date)"}).values('purchase_day').annotate(count=Count('id')).order_by('purchase_day')

    dates = [item['purchase_day'] for item in data]
    counts = [item['count'] for item in data]

    plt.figure(figsize=(10, 5))
    plt.plot(dates, counts, marker='o', linestyle='-', color='steelblue')
    plt.title('Продажи билетов по дням')
    plt.xlabel('Дата')
    plt.ylabel('Количество продаж')
    plt.grid(True)
    plt.tight_layout()
    plt.xticks(rotation=45)

    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    plt.close()
    buffer.seek(0)
    return HttpResponse(buffer.getvalue(), content_type='image/png')

def sales_charts_page(request):
    logger.info("Запрос к странице с графиками")
    return render(request, 'sales_charts.html')
