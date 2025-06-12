from django.contrib import admin
from .models import Pharmacy, InventoryItem, Sale, Order, WebhookEvent

admin.site.register(Pharmacy)
admin.site.register(InventoryItem)
admin.site.register(Sale)
admin.site.register(Order)
admin.site.register(WebhookEvent)
