from django.contrib import admin
from .models import TickerData,Index,Stock

@admin.register(TickerData)
class TickerDataAdmin(admin.ModelAdmin):
    list_display = ('ticker', 'date', 'close_price', 'atr', 'buy_signal', 'sell_signal')
    list_filter = ('ticker', 'buy_signal', 'sell_signal', 'date')
    search_fields = ('ticker',)

@admin.register(Index)
class IndexAdmin(admin.ModelAdmin):
    list_display = ('name', 'last_updated')

@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ('ticker', 'index')