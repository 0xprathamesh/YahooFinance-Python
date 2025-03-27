import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def fetch_stock_data(ticker_symbol, period="1mo"):
    """
    Fetch historical stock data for a given ticker symbol
    
    Args:
        ticker_symbol (str): Stock ticker symbol (e.g., 'BTC')
        period (str, optional): Time period for data. Defaults to "1mo".
    
    Returns:
        pandas.DataFrame: Historical stock price data
    """
    try:
        stock = yf.Ticker(ticker_symbol)
        hist = stock.history(period=period)
        return hist
    except Exception as e:
        print(f"Error fetching data for {ticker_symbol}: {e}")
        return None

def calculate_metrics(hist):
    """
    Calculate additional metrics for the stock data
    
    Args:
        hist (pandas.DataFrame): Historical stock price data
    
    Returns:
        pandas.DataFrame: Stock data with additional metrics
    """
    if hist is not None:
        hist['50_MA'] = hist['Close'].rolling(window=50).mean()
        hist['Volatility'] = hist['Close'].pct_change().rolling(window=30).std()
    return hist

def plot_stock_analysis(hist, ticker_symbol):
    """
    Create a plot of stock closing price and 50-day moving average
    
    Args:
        hist (pandas.DataFrame): Historical stock price data
        ticker_symbol (str): Stock ticker symbol
    """
    if hist is not None:
        plt.figure(figsize=(12,6))
        plt.plot(hist['Close'], label='Closing Price')
        plt.plot(hist['50_MA'], label='50-Day Moving Average')
        plt.title(f'{ticker_symbol} Stock Price Analysis')
        plt.xlabel('Date')
        plt.ylabel('Price')
        plt.legend()
        plt.grid(True)
        plt.show()

def main():
    # Example usage with Apple stock
    ticker = "BTC"
    
    # Fetch stock data
    hist = fetch_stock_data(ticker)
    
    if hist is not None:
        # Calculate additional metrics
        hist = calculate_metrics(hist)
        
        # Print the historical data
        print(f"{ticker} Historical Data:")
        print(hist)
        
        # Plot stock analysis
        plot_stock_analysis(hist, ticker)
        
        # Optional: Save data to CSV
        hist.to_csv(f'{ticker}_stock_analysis.csv')

if __name__ == "__main__":
    main()