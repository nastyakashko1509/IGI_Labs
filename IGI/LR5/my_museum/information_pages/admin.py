from django.contrib import admin
from .models import *


models = (AboutCompany, FAQ, News,
    PrivacyPolicy, PromoCode, Rewiew)

admin.site.register(News)
admin.site.register(AboutCompany)
admin.site.register(PrivacyPolicy)
admin.site.register(Review)
admin.site.register(PromoCode)
admin.site.register(FAQ)
