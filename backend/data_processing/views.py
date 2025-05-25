from django.shortcuts import render
from .models import Stock
from .turtle_trading import process_single_ticker

# Create your views here.
def process_ticker(request):
    stock = Stock.objects.get(pk = 1)
    print(stock)
    result = process_single_ticker(ticker= stock.ticker)
    return render(request, result)
    