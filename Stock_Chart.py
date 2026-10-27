import requests
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
from datetime import datetime, timedelta

stock_symbol = input("Enter the stock symbol (e.g., AAPL, MSFT): ")
historical_data = int(input("How many days of historical data do you want? "))
# Fetch historical stock data for the past days
end_date = datetime.now()
start_date = end_date - timedelta(days=historical_data)
ticker = yf.Ticker(stock_symbol)
data = ticker.history(start=start_date, end=end_date)
print(data)

#-----------------------------------

# Extract the daily data
daily_data = data[['Open', 'High', 'Low', 'Close', 'Volume']]

# Create a DataFrame
df = pd.DataFrame({
    'date': data.index,
    'max_rate': data['High'],
    'min_rate': data['Low'],
    'close_rate': data['Close']
})

print(df.head())

#-----------------------------------

# Create the plot
plt.figure(figsize=(10, 5))
plt.plot(df['date'], df['max_rate'], label='High', color='green')
plt.plot(df['date'], df['min_rate'], label='Low', color='red')
plt.title(f"{stock_symbol} High vs Low")
plt.xlabel("Date")
plt.ylabel("Price ($)")
plt.legend()
plt.grid(True)

# 1. Save first
plt.savefig(f'{stock_symbol}_{historical_data}_chart.png', bbox_inches='tight')

# 2. Display second
plt.show()