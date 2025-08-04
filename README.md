# Disclaimer
This project is intended solely for educational purposes and as an innovative guide for 
quantitative researchers. It does not constitute investment advice or a recommendation to 
buy, sell, or hold any financial asset. Users should conduct their own due diligence and 
consult professional advisors before making investment decisions.
# Crypto Risk Premia Dashboard

A reproducible, noise-aware dashboard for quantifying crypto risk premia factors using Yahoo Finance data and advanced statistical filtering.

## Features
- Fetches and cleans OHLCV data for major cryptos (BTC, ETH, altcoins) via yfinance
- Applies rolling median, z-score clipping, EMA smoothing, and more to reduce noise
- Computes market, momentum, low-volatility, network value, and custom factors
- Multi-factor backtest integration (momentum + low-volatility)
- Interactive Streamlit dashboard with raw vs denoised data comparisons
- Expanded dashboard pages: Market Risk Premium, Momentum, Low Volatility, Network Value, Factor Portfolio
- Dark institutional theme for quant feel
- Extensible: add new factors, filters, or data sources easily

## Data Pipeline
1. **Source:** Yahoo Finance (yfinance) for daily/hourly OHLCV
2. **Noise Reduction:** Rolling median, z-score clipping, EMA, optional Kalman filter
3. **Factor Computation:** Market premium, momentum, low-volatility anomaly, etc.
4. **Visualization:** Streamlit dashboard with toggles for raw/cleaned data

## Getting Started
1. Clone the repo
2. Install dependencies: `pip install -r requirements.txt`
3. Run the dashboard: `streamlit run dashboard.py`

## Example Modules
- `data_loader.py`: Data fetching and cleaning
- `factors/`: Factor computation modules
- `dashboard.py`: Streamlit dashboard

## Research Citations
- Sydney Quantitative Finance Symposium, 2023: 'Noise Reduction in Crypto Factor Models'
- EPFL Blockchain Analytics, 2025: 'Factor Investing in Digital Assets'

## Next Steps
- Add more advanced noise reduction (Kalman, wavelets)

---

*For quant students, researchers, and funds seeking robust, noise-aware crypto analytics.*
