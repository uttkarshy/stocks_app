import json
import time

# Define trading parameters
fromsymbol = 'ETH/USD'
amount = 0.1
stop_loss_pct = 0.05
take_profit_pct = 0.1

# Define the OHL period
timeframe = '1m'

# Define the number of previous periods to use in the OHL calculation
history_size = 10

# Define the delay between each iteration of the trading loop in seconds
delay = 30

# Define a function to calculate the OHL values
def ohl(data):
    open_price = float(data[-1]['open'])
    high_price = max(float(d['high']) for d in data)
    low_price = min(float(d['low']) for d in data)
    return open_price, high_price, low_price

# Read the historical data from the JSON file
with open(r'C:\Users\uttka\Desktop\stocks\app\fetchdata.json') as f:
    data = json.load(f)

# Enter the trading loop
while True:
    # Get the latest `history_size` periods of data
    current_data = data[-10:]

    # Calculate the OHL values
    current_open, current_high, current_low = ohl(current_data)

    # Check if the current price is above the current high
    if float(current_data[-1]['close']) > current_high:
        # Enter a long position
        entry_price = current_high
        stop_loss_price = entry_price * (1 - stop_loss_pct)
        take_profit_price = entry_price * (1 + take_profit_pct)
        print('Long position entered. Entry price:', entry_price)

        # Wait for the position to close
        while True:
            # Get the current price (in this example we just use the close price of the latest data point)
            current_price = float(data[-1]['close'])

            # Check if the stop loss or take profit has been hit
            if current_price <= stop_loss_price:
                exit_price = current_price
                print('Stop loss hit. Exit price:', exit_price)
                break
            elif current_price >= take_profit_price:
                exit_price = current_price
                print('Take profit hit. Exit price:', exit_price)
                break

            # Wait for the next iteration
            time.sleep(delay)

        # Exit the position
        profit_loss = (exit_price - entry_price) * amount
        print('Position closed with profit/loss of', profit_loss)

    # Check if the current price is below the current low
    elif float(current_data[-1]['close']) < current_low:
        # Enter a short position
        entry_price = current_low
        stop_loss_price = entry_price * (1 + stop_loss_pct)
        take_profit_price = entry_price * (1 - take_profit_pct)
        print('Short position entered. Entry price:', entry_price)

        # Wait for the position to close
        while True:
            # Get the current price (in this example we just use the close price of the latest data point)
            current_price = float(data[-1]['close'])

            # Check if the stop loss or take profit has been hit
            if current_price >= stop_loss_price:
                exit_price = current_price
                print('Stop loss hit. Exit price:', exit_price)
                break
            elif current_price <= take_profit_price:
                exit_price = current_price
                print('Take profit hit. Exit price:', exit_price)
                break

            # Wait for the next iteration
            time.sleep(delay)

        # Exit the position
        profit_loss = (exit_price - entry_price) * amount
        print('Position closed with profit/loss of', profit_loss)

    elif trend_direction == 'down':
        # Enter a short position
        entry_price = float(current_data[0]['close'])
        stop_loss_price = entry_price * (1 + stop_loss_pct)
        take_profit_price = entry_price * (1 - take_profit_pct)
        print('Short position entered. Entry price:', entry_price)

        # Wait for the position to close
        while True:
            # Get the current price (in this example we just use the close price of the latest data point)
            current_price = float(data[-1]['close'])

            # Check if the stop loss or take profit has been hit
            if current_price >= stop_loss_price:
                exit_price = current_price
                print('Stop loss hit. Exit price:', exit_price)
                break
            elif current_price <= take_profit_price:
                exit_price = current_price
                print('Take profit hit. Exit price:', exit_price)
                break

            # Wait for the next iteration
            time.sleep(delay)
        
        # Exit the position
        profit_loss = (exit_price - entry_price) * amount
        print('Position closed with profit/loss of', profit_loss)
        
    # Wait for the next iteration
    time.sleep(delay)
