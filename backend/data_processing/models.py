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

class Index(models.Model):
    """
    Represents a stock index, e.g., Nifty 50, Nifty 500.
    """
    name = models.CharField(max_length=50, unique=True)  # Name of the index
    last_updated = models.DateTimeField(auto_now=True)  # Tracks when the index was last updated

    def __str__(self):
        return self.name


class Stock(models.Model):
    """
    Represents a stock in an index.
    """
    ticker = models.CharField(max_length=10, unique=True)  # Stock ticker symbol
    name = models.CharField(max_length=100, blank=True, null=True)  # Optional: Full stock name
    index = models.ForeignKey(Index, related_name="stocks", on_delete=models.CASCADE)  # Link to an index

    def __str__(self):
        return f"{self.ticker} ({self.index.name})"
