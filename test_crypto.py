import alpaca_trade_api as tradeapi
import yfinance as yf

# Set up Alpaca API
api_key = 'PKPVZD0TTQ18DO38OPJ7'
api_secret = 'W8EZQGNk6Zd0bx30ViBbbay83GRRjbtKjWFnUZNi'
base_url = 'https://paper-api.alpaca.markets'

api = tradeapi.REST(api_key, api_secret, base_url, api_version='v2')

api.list_assets()
