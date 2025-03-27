import yfinance as yf

apple = yf.Ticker("AAPL")
hist = apple.history(period="1mo");
print(hist)