from django.db import models

class TickerData(models.Model):
    """
    Stores OHLCV data, indicators, and signals for a stock ticker.
    """
    ticker = models.CharField(max_length=10)  # Stock ticker symbol
    date = models.DateField()  # Date of the data
    open_price = models.FloatField()  # Opening price
    high_price = models.FloatField()  # High price
    low_price = models.FloatField()  # Low price
    close_price = models.FloatField()  # Closing price
    volume = models.BigIntegerField()  # Volume of the stock

    atr = models.FloatField(null=True, blank=True)  # Average True Range
    buy_signal = models.BooleanField(default=False)  # Buy signal flag
    sell_signal = models.BooleanField(default=False)  # Sell signal flag

    def __str__(self):
        return f"{self.ticker} - {self.date}"
