from django.contrib import admin
from .models import Trade

@admin.register(Trade)
class TradeAdmin(admin.ModelAdmin):
    list_display = ('ticker', 'entry_price', 'stop_loss', 'position_size', 'status')
    list_filter = ('status', 'ticker')
    search_fields = ('ticker',)
