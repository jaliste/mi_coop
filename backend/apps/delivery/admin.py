from django.contrib import admin

# Register your models here.
from .models import *

class BasketSubscriptionItemInline(admin.StackedInline):
    model = BasketSubscriptionItem

@admin.register(BasketSubscription)
class BasketSubscriptionAdmin(admin.ModelAdmin):
    inlines = [BasketSubscriptionItemInline]

admin.site.register(PickupPlace)
#admin.site.register(BasketSubscription)
admin.site.register(PickupDay)
admin.site.register(Basket)
admin.site.register(SubscriptionPeriodicity)
admin.site.register(ProduceUnit)
