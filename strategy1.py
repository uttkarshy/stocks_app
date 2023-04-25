import alpaca_trade_api as tradeapi
import yfinance as yf
import time
from alpaca_trade_api.stream import CryptoDataStream
from ta.momentum import RSIIndicator
import pandas as pd

api_key = 'PKPVZD0TTQ18DO38OPJ7'
api_secret = 'W8EZQGNk6Zd0bx30ViBbbay83GRRjbtKjWFnUZNi'
base_url = 'https://paper-api.alpaca.markets'

api = tradeapi.REST(api_key, api_secret, base_url, api_version='v2')
# Define the symbol and date range
symbol = 'AAPL'
time_frame = '1d'
#start_date = '2023-04-24'
#end_date = '2023-04-26'

# Fetch the historical data from Yahoo Finance
# start=start_date, end=end_date
data = yf.download(symbol,interval=time_frame)

# Calculate the RSI over a 14-day period
rsi = RSIIndicator(data['Close'], window=14)

# Add the RSI values to the data frame
data['RSI'] = rsi.rsi()

# Define the RSI window and the buy/sell thresholds
rsi_window = 14
buy_threshold = 30
sell_threshold = 70

while True:
    # Fetch the historical data from Yahoo Finance
    data = yf.download(symbol)

    # Calculate the RSI over the specified period
    rsi = RSIIndicator(data['Close'], window=rsi_window)

    # Add the RSI values to the data frame
    data['RSI'] = rsi.rsi()

    # Check if the RSI has crossed the buy threshold
    if data['RSI'].iloc[-1] <= buy_threshold:
        print("Strong buy signal detected!")
        api.submit_order(
     symbol='ETHUSD',
     qty=1,
     side='buy',
     type='market',
     time_in_force='gtc'
     )
        break

    # If not, wait for 5 minutes before checking again
    print("No strong buy signal yet. Waiting for 5 minutes...")
    time.sleep(300)  # 300 seconds = 5 minutes