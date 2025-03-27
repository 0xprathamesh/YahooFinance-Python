import yfinance as yf
import pandas as pd

def get_option_chain(ticker) :
     # Fetch the Stock Data from Yahoo Finance
    stock  = yf.Ticker(ticker)
    
    #Fetch the Expiration Dates
    expiration_dates = stock.options
    
    # Dictionary to hold all the options data
    options_data = {'Calls': [], 'Puts': []}
    
    # Loop through each expiration date and fetch the options data
    for exp_date in expiration_dates:
        options = stock.option_chain(exp_date)
        
        # Add the expiration date to the data
        calls = options.calls.copy()
        calls['expirationDate'] = exp_date
        puts = options.puts.copy()
        puts['expirationDate'] = exp_date
        
        options_data['Calls'].append(calls)
        options_data['Puts'].append(puts)
    
    # Concatenate all the dataframes for calls and puts
    calls_df = pd.concat(options_data['Calls'])
    puts_df = pd.concat(options_data['Puts'])
    
    return calls_df, puts_df

ticker = "BTC" #Bitcoin

calls,puts = get_option_chain(ticker)

print("Calls:")
print(calls.head())
print("\nPuts:")
print(puts.head())
