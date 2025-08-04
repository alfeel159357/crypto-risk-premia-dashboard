## Crypto Risk Premia Dashboard

Quant-grade intelligence for decoding hidden risk premia in crypto  and is fully reproducible, noise-engineered, and built for serious researchers and traders seeking alpha beyond the hype.

### Why This Project?
Crypto markets are wild, noisy, and poorly mapped — a frontier where meaningful factor signals are buried under extreme volatility and speculative noise. Traditional equity factor models don’t translate cleanly, leaving a gap between theory and actionable insight.

This dashboard closes that gap by delivering:
- Clean, factor-based analytics that extract systematic drivers of crypto returns.
- Noise-aware filtering to reveal true premia signals masked by daily chaos.
- Reproducible, research-ready frameworks ideal for academic studies, quant funds, and high-level strategy design.
- A single interactive environment that unifies market, momentum, low-volatility, and network-value factors — and lets you extend to new ones as the space evolves.


## Features
- Fetches and cleans OHLCV data for major cryptos (BTC, ETH, altcoins) via yfinance
- Applies rolling median, z-score clipping, EMA smoothing, and more to reduce noise
- Computes market, momentum, low-volatility, network value, and custom factors
- Multi-factor backtest integration (momentum + low-volatility)
- Interactive Streamlit dashboard with raw vs denoised data comparisons
- Expanded dashboard pages: Market Risk Premium, Momentum, Low Volatility, Network Value, Factor Portfolio
- Dark institutional theme for quant feel
- Extensible: add new factors, filters, or data sources easily

-----

<img width="942" height="428" alt="dashboard" src="https://github.com/user-attachments/assets/3b778220-2181-49db-8aba-3792971f7287" />

-----

<img width="953" height="425" alt="factor_combination_crypto_risk_premia" src="https://github.com/user-attachments/assets/f70698af-6538-4172-bd5a-14f7c4d181fd" />


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
🔜  Add more advanced noise reduction (Kalman, wavelets)Roadmap

🔜 Factor correlation heatmaps & regime detection

🔜 Machine learning–driven factor forecasts

🔜 Integration with DeFi metrics (on-chain activity, TVL factors)

🔜 Portfolio optimizer with transaction cost modeling

---

*For quant students, researchers, and funds seeking robust, noise-aware crypto analytics.*

# Disclaimer
This project is intended solely for educational purposes and as an innovative guide for 
quantitative researchers. It does not constitute investment advice or a recommendation to 
buy, sell, or hold any financial asset. Users should conduct their own due diligence and 
consult professional advisors before making investment decisions.

---

#### GitHub: https://github.com/QuantDevJayson
#### PyPI: https://pypi.org/user/jayson.ashioya
#### LinkedIn: https://www.linkedin.com/in/jayson-ashioya-c-082814176/
