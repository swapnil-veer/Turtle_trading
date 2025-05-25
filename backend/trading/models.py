from django.db import models

class Trade(models.Model):
    """
    Tracks trades executed for a stock.
    """
    ticker = models.CharField(max_length=10)  # Stock ticker symbol
    entry_price = models.FloatField()  # Entry price of the trade
    stop_loss = models.FloatField()  # Stop-loss level
    position_size = models.IntegerField()  # Number of shares
    status = models.CharField(
        max_length=20,
        choices=[('OPEN', 'Open'), ('CLOSED', 'Closed')],
        default='OPEN'
    )  # Trade status

    def __str__(self):
        return f"Trade {self.ticker} - {self.status}"
