import yfinance as yf
import pandas as pd
import numpy as np

def download_crypto_data(ticker="BTC-USD", start="2015-01-01", end=None, interval="1d"):
    df = yf.download(ticker, start=start, end=end, interval=interval)
    df = df[['Open', 'High', 'Low', 'Close', 'Volume']].dropna()
    df.index.name = "Date"
    return df

def remove_noise(df, method="rolling_median", window=3):
    cleaned = df.copy()
    if method == "rolling_median":
        for col in ['Open', 'High', 'Low', 'Close']:
            cleaned[col] = cleaned[col].rolling(window, center=True).median().fillna(method="bfill").fillna(method="ffill")
    elif method == "zscore_clip":
        for col in ['Open', 'High', 'Low', 'Close']:
            z = (cleaned[col] - cleaned[col].mean()) / cleaned[col].std()
            cleaned[col] = np.where(abs(z) > 3, np.nan, cleaned[col])
            cleaned[col] = cleaned[col].interpolate().fillna(method="bfill").fillna(method="ffill")
    elif method == "ema":
        for col in ['Close']:
            cleaned[col] = cleaned[col].ewm(span=5).mean()
    elif method == "sma":
        for col in ['Close']:
            cleaned[col] = cleaned[col].rolling(window).mean().fillna(method="bfill").fillna(method="ffill")
    elif method == "minmax_clip":
        for col in ['Open', 'High', 'Low', 'Close']:
            arr = cleaned[col]
            if hasattr(arr, 'shape') and arr.ndim > 1:
                arr = arr.to_numpy().flatten() if hasattr(arr, 'to_numpy') else arr.flatten()
            s = pd.Series(arr, index=cleaned.index)
            cleaned[col] = s.clip(lower=s.quantile(0.01), upper=s.quantile(0.99))
    elif method == "median_absolute_deviation":
        for col in ['Open', 'High', 'Low', 'Close']:
            med = cleaned[col].median()
            mad = np.median(np.abs(cleaned[col] - med))
            arr = np.where(np.abs(cleaned[col] - med) > 3*mad, med, cleaned[col])
            arr = arr.flatten() if hasattr(arr, 'shape') and arr.ndim > 1 else arr
            cleaned[col] = pd.Series(arr, index=cleaned.index).interpolate().fillna(method="bfill").fillna(method="ffill")
    return cleaned
