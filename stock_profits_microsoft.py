import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

# Define the parameters
ticker = "MSFT"
investment_amount = 100
investment_frequency_days = 14  # Every 2 weeks
start_date = datetime.now() - timedelta(days=5*365)  # 5 years ago

# Fetch historical data for Microsoft
msft = yf.Ticker(ticker)
historical_data = msft.history(start=start_date.strftime('%Y-%m-%d'), end=datetime.now().strftime('%Y-%m-%d'))

# Generate investment dates
investment_dates = pd.date_range(start=start_date, end=datetime.now(), freq=f'{investment_frequency_days}D')

# Initialize investment dataframe
investment_df = pd.DataFrame(index=investment_dates)
investment_df['Investment'] = investment_amount

# Ensure the indices are timezone-naive before merging
investment_df.index = investment_df.index.tz_localize(None)
historical_data.index = historical_data.index.tz_localize(None)

# Reindex investment_df to match historical_data's dates and forward fill missing values
investment_df = investment_df.reindex(historical_data.index, method='ffill')

# Fill initial NaN investment value with 0
investment_df['Investment'] = investment_df['Investment'].fillna(0)

# Merge with historical prices to get the stock prices on investment dates
investment_df = investment_df.merge(historical_data['Close'], left_index=True, right_index=True, how='left')

# Forward fill missing prices (weekends/holidays)
investment_df['Close'] = investment_df['Close'].ffill()

# Check for any NaN values in 'Close' after forward fill
if investment_df['Close'].isna().any():
    print("Warning: There are still NaN values in the 'Close' column after forward fill.")
    print(investment_df[investment_df['Close'].isna()])

# Calculate shares purchased and cumulative shares
investment_df['Shares'] = investment_df['Investment'] / investment_df['Close']
investment_df['Cumulative_Shares'] = investment_df['Shares'].cumsum()

# Fetch dividends data
dividends = msft.dividends[start_date.strftime('%Y-%m-%d'):datetime.now().strftime('%Y-%m-%d')]

# Normalize the dividends index to match historical_data
dividends.index = dividends.index.tz_localize(None)

# Initialize a dataframe to keep track of total value over time
value_df = investment_df[['Cumulative_Shares']].copy()

# Calculate value of the portfolio over time
value_df = value_df.merge(historical_data['Close'], left_index=True, right_index=True, how='left')
value_df['Portfolio_Value'] = value_df['Cumulative_Shares'] * value_df['Close']

# Reinvest dividends
for date, dividend in dividends.items():
    if date in value_df.index:
        reinvested_shares = dividend * value_df.loc[date, 'Cumulative_Shares'] / value_df.loc[date, 'Close']
        value_df.loc[date:, 'Cumulative_Shares'] += reinvested_shares
        value_df['Portfolio_Value'] = value_df['Cumulative_Shares'] * value_df['Close']

# Check for NaN values in 'Portfolio_Value'
if value_df['Portfolio_Value'].isna().any():
    print("Warning: There are NaN values in the 'Portfolio_Value' column.")
    print(value_df[value_df['Portfolio_Value'].isna()])

# Ensure the final value is not NaN
final_value = value_df['Portfolio_Value'].iloc[-1] if not pd.isna(value_df['Portfolio_Value'].iloc[-1]) else 0

# Calculate total savings
total_savings = investment_amount * len(investment_dates)

# Create a DataFrame for total savings over time
savings_df = pd.DataFrame(index=historical_data.index)
savings_df['Total_Savings'] = savings_df.index.to_series().apply(lambda x: investment_amount * ((x - start_date).days // investment_frequency_days))
savings_df['Total_Savings'] = savings_df['Total_Savings'].clip(upper=len(investment_dates) * investment_amount)

# Calculate the percentage profit
percentage_profit = ((final_value - total_savings) / total_savings) * 100 if total_savings != 0 else 0

# Print comparison schema with colors
print("\n--- Comparison Schema ---")
print(f"Total money saved if only saved: {Fore.RED}${total_savings:.2f}{Style.RESET_ALL}")
print(f"Final portfolio value with investment: {Fore.YELLOW}${final_value:.2f}{Style.RESET_ALL}")
print(f"Percentage profit from investment: {percentage_profit:.2f}%")
print("--------------------------")

# Plotting the portfolio value and total savings over time
plt.figure(figsize=(12, 6))
plt.plot(value_df.index, value_df['Portfolio_Value'], label='Portfolio Value', color='blue')
plt.plot(savings_df.index, savings_df['Total_Savings'], label='Total Savings', color='red')
plt.xlabel('Date')
plt.ylabel('Value ($)')
plt.title('Portfolio Value vs. Total Savings Over Time')
plt.legend()
plt.grid(True)
plt.show()

# Debugging information
print(f"First few rows of investment_df:\n{investment_df.head()}")
print(f"First few rows of value_df:\n{value_df.head()}")
print(f"First few rows of historical_data:\n{historical_data.head()}")
print(f"First few rows of dividends:\n{dividends.head()}")
