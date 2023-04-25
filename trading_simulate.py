import time

# Define trading parameters
symbol = 'ETH/USD'
amount = 0.1
stop_loss_pct = 0.05
take_profit_pct = 0.1

# Define momentum threshold
threshold = 0.5

# Define the period of the momentum calculation
timeframe = '1m'

# Define the number of previous periods to use in the momentum calculation
history_size = 10

# Define the delay between each iteration of the trading loop in seconds
delay = 30

# Define a function to calculate the momentum
def momentum(data):
    close = data['close']
    momentum = close[-1] / close[0] - 1
    return momentum

# Define a function to simulate trading
def simulate_trading():
    # Load historical data
    with open('C:\Users\uttka\Desktop\stocks\app\data.csv', 'r') as f:
        lines = f.readlines()
    data = []
    for line in lines:
        time, open, high, low, close, volume = line.strip().split(',')
        data.append({
            'time': int(time),
            'open': float(open),
            'high': float(high),
            'low': float(low),
            'close': float(close),
            'volume': float(volume),
        })

    # Enter the trading loop
    for i in range(history_size, len(data)):
        # Get the historical data
        historical_data = data[i - history_size:i]

        # Calculate the momentum
        current_momentum = momentum(historical_data)

        # Check if the momentum is above the threshold
        if current_momentum > threshold:
            # Enter a long position
            entry_price = data[i]['close']
            stop_loss_price = entry_price * (1 - stop_loss_pct)
            take_profit_price = entry_price * (1 + take_profit_pct)
            print('Long position entered. Entry price:', entry_price)

            # Wait for the position to close
            while True:
                # Get the current price
                current_price = data[i]['close']

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
    
    print('Trading simulation completed.')

# Run the trading simulation
simulate_trading()
