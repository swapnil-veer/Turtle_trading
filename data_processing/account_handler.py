import pandas as pd



class Account_Handler:
    """
    Handles risk management, position sizing, and trade levels for the Turtle Trading strategy.
    """
    NO_OF_STOCK_TYPE = 2  # Number of different stocks in the account
    account_size = 100000  # Total account size in currency units

    def __init__(self, risk_percentage: float):
        """
        Initialize the account handler with risk management parameters.
        """
        self.risk_percentage = risk_percentage / 100
        self.trading_amt_per_share = self.account_size / self.NO_OF_STOCK_TYPE
        self.risk = self.trading_amt_per_share * self.risk_percentage

    def fetch_atr(self, filename: str, ticker: str) -> float:
        """
        Retrieve the ATR (Average True Range) value from the Excel file for the given ticker.
        """
        ticker = ticker.upper()
        xls = pd.ExcelFile(filename)
        if ticker in xls.sheet_names:
            df = pd.read_excel(filename, sheet_name=ticker)
            df['Date'] = pd.to_datetime(df['Date'])  # Ensure proper datetime format
            df.set_index('Date', inplace=True)
            
            try:
                atr = df.iloc[-1]['Avg_True_Range(N)']
                return atr
            except KeyError:
                raise KeyError(f"ATR column not found for {ticker}.")
        else:
            raise ValueError(f"Ticker {ticker} not found in the Excel file.")

    def calculate_position_size(self, atr: float) -> int:
        """
        Calculate the position size (number of shares) based on risk and ATR.
        """
        if atr <= 0:
            raise ValueError("ATR must be greater than 0.")
        position_size = self.risk // atr
        return int(position_size)

    def fetch_entry_price(self, filename: str, ticker: str) -> float:
        """
        Retrieve the entry price (previous day's close) for the given ticker from the Excel file.
        """
        ticker = ticker.upper()
        xls = pd.ExcelFile(filename)
        if ticker in xls.sheet_names:
            df = pd.read_excel(filename, sheet_name=ticker)
            df['Date'] = pd.to_datetime(df['Date'])  # Ensure proper datetime format
            df.set_index('Date', inplace=True)
            
            try:
                entry_price = df.iloc[-1]['Close']
                return entry_price
            except KeyError:
                raise KeyError(f"Close price column not found for {ticker}.")
        else:
            raise ValueError(f"Ticker {ticker} not found in the Excel file.")

    def calculate_stop_loss(self, entry_price: float, atr: float, multiplier: float = 2.0) -> float:
        """
        Calculate the stop-loss price based on the entry price and ATR multiplier.
        """
        return entry_price - (multiplier * atr)

    def calculate_pyramid_price(self, entry_price: float, atr: float, level: int) -> float:
        """
        Calculate the pyramid levels based on entry price and ATR.
        Levels:
        - Level 1: 0.5 * ATR
        - Level 2: 1.0 * ATR
        - Level 3: 1.5 * ATR (extendable)
        """
        return entry_price + (level * 0.5 * atr)

    def calculate_stop_loss_pyramid(self, stop_loss_price: float, atr: float, level: int) -> float:
        """
        Calculate the stop-loss for pyramid levels based on ATR adjustments.
        """
        return stop_loss_price + (level * 0.5 * atr)
    
if __name__ == "__main__":
    filename = "Turtle1_Trading.xlsx"
    ticker = "FORTIS"
    account_handler = Account_Handler(risk_percentage=1)

    # Fetch ATR and calculate position size
    atr = account_handler.fetch_atr(filename, ticker)
    position_size = account_handler.calculate_position_size(atr)

    # Fetch entry price and calculate stop-loss
    entry_price = account_handler.fetch_entry_price(filename, ticker)
    stop_loss_price = account_handler.calculate_stop_loss(entry_price, atr)

    # Calculate pyramid levels
    first_pyr_price = account_handler.calculate_pyramid_price(entry_price, atr, level=1)
    second_pyr_price = account_handler.calculate_pyramid_price(entry_price, atr, level=2)

    print(f"ATR: {atr}, Position Size: {position_size}, Entry Price: {entry_price}")
    print(f"Stop Loss: {stop_loss_price}, First Pyramid: {first_pyr_price}, Second Pyramid: {second_pyr_price}")