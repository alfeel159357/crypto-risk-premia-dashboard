
# Project by @QuantDevJayson
# GitHub: https://github.com/QuantDevJayson
# PyPI: https://pypi.org/user/jayson.ashioya
# LinkedIn: https://www.linkedin.com/in/jayson-ashioya-c-082814176/
import pandas as pd

def backtest_factors(price_series, momentum, low_vol, weights=(0.5, 0.5)):
    # Combine factors
    combined_signal = weights[0]*momentum + weights[1]*low_vol
    import numpy as np
    positions = np.sign(combined_signal)
    # Ensure positions is a numpy array before flattening
    if isinstance(positions, pd.DataFrame) or isinstance(positions, pd.Series):
        positions = positions.values
    if hasattr(positions, 'shape') and positions.ndim > 1 and positions.shape[-1] == 1:
        positions = positions.flatten()
    positions = pd.Series(positions, index=combined_signal.index).replace(0, method='ffill').fillna(1)
    # Calculate daily returns
    returns = price_series.pct_change().shift(-1)
    strategy_returns = positions * returns
    return strategy_returns.dropna()
