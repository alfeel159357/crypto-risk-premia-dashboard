import pandas as pd

def compute_low_volatility_factor(price_series, window=30):
    # Calculate rolling volatility (standard deviation)
    vol = price_series.pct_change().rolling(window).std()
    # Invert volatility for low-vol factor
    low_vol_factor = -vol
    return low_vol_factor.dropna()
