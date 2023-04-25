import pandas as pd
import yfinance as yf

# Ticker symbol of the stock we want to retrieve data for
symbol = "AAPL"

# Retrieve data using yfinance library
data = yf.download(symbol, start="2023-04-01", end="2023-04-25")

# Convert data to a pandas DataFrame
df = pd.DataFrame(data)

# Add a new column to the DataFrame for daily percentage change
df['daily_change'] = df['Close'].pct_change()

# Filter the DataFrame to show only days where the daily change was greater than 1%
df_filtered = df[df['daily_change'] > 0.01]

# Sort the filtered DataFrame by date in descending order
df_sorted = df_filtered.sort_values(by=['Date'], ascending=False)

# Write the filtered and sorted data to an Excel file
df_sorted.to_excel("C:\Users\uttka\Desktop\stocks\app\output.xlsx", index=False)
