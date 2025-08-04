import pandas as pd

def compute_market_risk_premium(price_series, risk_free_series):
    # Excess returns over risk-free rate
    excess_returns = price_series.pct_change() - risk_free_series.pct_change()
    return excess_returns.dropna()
