import yfinance as yf
import pandas as pd
import ta.momentum as momentum

# Define the stock ticker symbol
ticker = "RELIANCE.NS"

start_date = "2022-01-31"
end_date = "2023-04-25"

# Get the stock data using yfinance
stock_data = yf.download(ticker, start=start_date, end=end_date)

# Compute the RSI indicator with a lookback period of 14 days
rsi = momentum.RSIIndicator(stock_data["Close"], window=14)
stock_data["RSI"] = rsi.rsi()

# Filter the data to only include stocks that are overbought (RSI > 70) and have high trading volume
overbought_data = stock_data[(stock_data["RSI"] > 70) & (stock_data["Volume"] > stock_data["Volume"].mean())]

# Print out the results
print("Stocks that are overbought and have high volume:")
print(overbought_data)
