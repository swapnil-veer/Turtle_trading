from django.db import models

# Create your models here.
class Company(models.Model):
    date = models.DateField()
    open = models.DecimalField()
    high = models.DecimalField()
    low = models.DecimalField()
    close = models.DecimalField(null=True)
    adj_close = models.DecimalField(null=True)
    volume = models.BigIntegerField(null=True)

    class Meta():
        db_table = "company"

    # def __str__(self):
    #     return self

