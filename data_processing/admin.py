from django.contrib import admin
from .models import TickerData

@admin.register(TickerData)
class TickerDataAdmin(admin.ModelAdmin):
    list_display = ('ticker', 'date', 'close_price', 'atr', 'buy_signal', 'sell_signal')
    list_filter = ('ticker', 'buy_signal', 'sell_signal', 'date')
    search_fields = ('ticker',)
