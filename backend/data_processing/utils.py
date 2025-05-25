from multiprocessing import Pool, cpu_count
from data_processing.turtle_trading import TurtleTrading
from data_processing.models import TickerData
from datetime import datetime
from functools import partial

def process_ticker(ticker: str, days: int, period: str = "1mo"):
    """
    Fetch, process, and save data for a single ticker if it meets criteria.
    """
    try:
        # Initialize TurtleTrading
        trader = TurtleTrading(ticker, period=period)
        data = trader.fetch_data()

        if data is not None:
            # Calculate indicators and generate signals
            data = trader.calculate_indicators()
            data = trader.generate_signals()

            # Check for buy signals
            if 'Buy_Signal' in data.columns and data['Buy_Signal'].tail(days).any():
                print(f"Ticker {ticker} has a Buy Signal within the last {days} days.")

                # Save to TickerData model
                for _, row in data.iterrows():
                    TickerData.objects.update_or_create(
                        ticker=ticker,
                        date=row['Date'],
                        defaults={
                            'open_price': row['Open'],
                            'high_price': row['High'],
                            'low_price': row['Low'],
                            'close_price': row['Close'],
                            'volume': row['Volume'],
                            'atr': row.get('Avg_True_Range(N)', None),
                            'buy_signal': row.get('Buy_Signal', False),
                            'sell_signal': row.get('Sell_Signal', False),
                        }
                    )
                print(f"Processed and saved data for {ticker}")
            else:
                print(f"No Buy Signal for {ticker} in the last {days} days.")

        else:
            print(f"No data fetched for {ticker}")

    except Exception as e:
        print(f"Error processing {ticker}: {e}")

def safe_process_ticker(ticker, days, period):
    try:
        process_ticker(ticker, days, period)
    except Exception as e:
        print(f"Error processing {ticker}: {e}")

def process_all_tickers(tickers, days=1, period="1y"):
    """
    Process multiple tickers in parallel using multiprocessing.
    Includes error handling, dynamic process count, and chunking.
    """
    num_processes = min(cpu_count(), len(tickers))
    chunk_size = max(1, len(tickers) // num_processes)

    with Pool(processes=num_processes) as pool:
        pool.map(partial(safe_process_ticker, days=days, period=period), tickers, chunksize=chunk_size)
