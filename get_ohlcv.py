import alpaca_trade_api as tradeapi

# Replace the placeholders with your Alpaca API key and secret
api_key = 'PKPVZD0TTQ18DO38OPJ7'
api_secret = 'W8EZQGNk6Zd0bx30ViBbbay83GRRjbtKjWFnUZNi'
base_url = 'https://paper-api.alpaca.markets'


# Create an instance of the Alpaca API client
api = tradeapi.REST(api_key, api_secret)

# Define the stock symbol and time frame
symbol = 'AAPL'
timeframe = '15Min' # Valid options are 1Min, 5Min, 15Min, and 1H
start_date = '2023-04-24'
end_date = '2023-04-24'
# Get the latest 100 bars of historical data
bars = api.get_bars(symbol,timeframe,start_date,end_date, limit=100).df

# Print the latest bar data
print(bars.tail(1))
