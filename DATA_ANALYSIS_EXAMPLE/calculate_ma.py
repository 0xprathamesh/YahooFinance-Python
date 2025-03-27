import pandas as pd
import numpy as np
from fetch_data import hist
# Calculate moving averages, volatility, and other metrics
hist['50_MA'] = hist['Close'].rolling(window=50).mean()
hist['Volatility'] = hist['Close'].pct_change().rolling(window=30).std()