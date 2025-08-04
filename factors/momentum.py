def compute_momentum_factor(price_series, lookback=90):
    momentum = price_series.pct_change(lookback).shift(1)
    return momentum.dropna()
