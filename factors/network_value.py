import pandas as pd

def compute_nvt_ratio(price_series, tx_volume_series):
    # Network Value to Transactions (NVT) ratio
    nvt = price_series / tx_volume_series
    return nvt.dropna()
