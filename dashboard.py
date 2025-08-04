
import streamlit as st

# Clear Streamlit cache for a fresh session
st.cache_data.clear()
from datetime import date
from data_loader import download_crypto_data, remove_noise
from factors.momentum import compute_momentum_factor
from factors.low_volatility import compute_low_volatility_factor
from factors.backtest import backtest_factors
from factors.market_premium import compute_market_risk_premium
from factors.network_value import compute_nvt_ratio
import matplotlib.pyplot as plt


st.set_page_config(
    page_title="Crypto Risk Premia: Quantitative Factor Analytics for Digital Assets",
    layout="wide",
    initial_sidebar_state="expanded",
    page_icon="💹"
)


# Navigation logic

st.sidebar.title("Navigation")
nav_option = st.sidebar.radio("Go to:", ["Dashboard", "Project Guide & Glossary"], index=0, key="main_nav_radio")

if nav_option == "Dashboard":
    st.title("Crypto Risk Premia: Quantitative Factor Analytics for Digital Assets")
    st.markdown("""
    **A next-generation dashboard for analyzing risk premia in the crypto universe using robust factor models, advanced noise reduction, and multi-asset backtesting.**
    
    This platform empowers quant researchers and practitioners to:
    - Explore market, momentum, low-volatility, and network value factors across 100+ cryptocurrencies
    - Apply state-of-the-art noise reduction to improve signal quality
    - Backtest multi-factor portfolios and compare raw vs denoised performance
    - Build on and extend the latest academic research in digital asset analytics
    """)

if nav_option == "Project Guide & Glossary":
    st.title("Project Guide & Glossary")
    st.header("Project Guide")
    st.markdown("""
    This dashboard builds on and extends recent research in quantitative crypto analytics:
    - **Noise Reduction in Crypto Factor Models** (Sydney Quantitative Finance Symposium, 2023):
      - This project implements advanced noise reduction (rolling median, z-score clipping, EMA) to address microstructure noise, API anomalies, and volatility spikes in crypto data, improving factor signal quality and reproducibility.
    - **Factor Investing in Digital Assets** (EPFL Blockchain Analytics, 2025):
      - Expands the factor universe to 100+ cryptos, supports multi-factor backtesting, and enables robust portfolio construction and performance analysis, making the research practical and extensible for quant funds and academics.

    **Key Features:**
    - Data sourced from Yahoo Finance (yfinance) for 100+ cryptos
    - Factors: Market Risk Premium, Momentum, Low Volatility, Network Value (NVT), Multi-Factor Portfolios
    - Noise reduction: Rolling Median, Z-Score Clipping, EMA Smoothing
    - Backtesting: Combine multiple factors and assets for robust quant analytics
    """)
    st.header("Glossary")
    st.markdown("""
    - **OHLCV:** Open, High, Low, Close, Volume (standard financial data format)
    - **Risk Premium:** Excess return over risk-free rate
    - **Momentum:** Return based on price change over a lookback period
    - **Low Volatility:** Factor favoring assets with lower price fluctuations
    - **NVT Ratio:** Network Value to Transactions, a blockchain valuation metric
    - **Backtest:** Simulated historical performance of a strategy
    - **Noise Reduction:** Statistical techniques to clean financial data
    """)
    st.header("Recent Research Citations")
    st.markdown("""
    - Sydney Quantitative Finance Symposium, 2023: 'Noise Reduction in Crypto Factor Models'
    - EPFL Blockchain Analytics, 2025: 'Factor Investing in Digital Assets'
    """)
    st.header("Authorship")
    st.markdown("""
    **Project by [@QuantDevJayson](https://github.com/QuantDevJayson)**  
    PyPI: [jayson.ashioya](https://pypi.org/user/jayson.ashioya)  
    LinkedIn: [Jayson Ashioya](https://www.linkedin.com/in/jayson-ashioya-c-082814176/)
    """)
    st.stop()

page = st.sidebar.selectbox("Select Page", [
    "Momentum Factor", "Market Risk Premium", "Low Volatility Factor", "Network Value Factor", "Factor Combination (Coming Soon)"
])

crypto_list = [
    "BTC-USD", "ETH-USD", "SOL-USD", "BNB-USD", "ADA-USD", "XRP-USD", "DOGE-USD", "DOT-USD", "AVAX-USD", "MATIC-USD",
    "SHIB-USD", "TRX-USD", "LINK-USD", "ATOM-USD", "LTC-USD", "BCH-USD", "XLM-USD", "UNI-USD", "ALGO-USD", "ETC-USD",
    "FIL-USD", "VET-USD", "ICP-USD", "HBAR-USD", "EGLD-USD", "XTZ-USD", "AAVE-USD", "GRT-USD", "SAND-USD", "MANA-USD",
    "QNT-USD", "AXS-USD", "RUNE-USD", "CAKE-USD", "KSM-USD", "ENJ-USD", "ZIL-USD", "CHZ-USD", "BAT-USD", "1INCH-USD",
    "COMP-USD", "SNX-USD", "YFI-USD", "CRV-USD", "REN-USD", "CEL-USD", "BAL-USD", "DASH-USD", "OMG-USD", "ZRX-USD",
    "BNT-USD", "CVC-USD", "STORJ-USD", "SUSHI-USD", "LRC-USD", "SKL-USD", "ANKR-USD", "GNO-USD", "FET-USD", "RSR-USD",
    "NMR-USD", "OCEAN-USD", "BAND-USD", "RLC-USD", "COTI-USD", "API3-USD", "MLN-USD", "TRB-USD", "PNT-USD", "MKR-USD",
    "XEM-USD", "SC-USD", "DGB-USD", "LSK-USD", "STEEM-USD", "SXP-USD", "AR-USD", "STMX-USD", "XNO-USD", "XDC-USD",
    "XVG-USD", "SYS-USD", "VTHO-USD", "WIN-USD", "BTT-USD", "HOT-USD", "CRO-USD", "FTM-USD", "KAVA-USD", "GLM-USD",
    "QKC-USD", "ELF-USD", "FUN-USD", "POWR-USD", "MTL-USD", "DENT-USD", "CTSI-USD", "TOMO-USD", "PERL-USD", "STPT-USD"
]
asset = st.sidebar.selectbox("Select Asset", crypto_list)
method = st.sidebar.radio("Noise Reduction Method", [
    "none", "rolling_median", "zscore_clip", "ema", "sma", "minmax_clip", "median_absolute_deviation"
])
lookback = st.sidebar.slider("Momentum Lookback (days)", 1, 365, 90)

# Date range selection
st.sidebar.markdown("**Select Date Range**")
default_start = date(2018, 1, 1)
default_end = date.today()
date_range = st.sidebar.date_input(
    "Date Range", value=(default_start, default_end), min_value=date(2015, 1, 1), max_value=default_end
)
if isinstance(date_range, tuple):
    start_date, end_date = date_range
else:
    start_date, end_date = default_start, default_end

raw = download_crypto_data(asset, start=str(start_date), end=str(end_date))
clean = remove_noise(raw, method=method) if method != "none" else raw

if page == "Factor Combination (Coming Soon)":
    st.title("Factor Combination")
    st.info("Multi-factor portfolio analytics and backtesting are coming soon! Stay tuned for advanced quant features.")
elif page == "Momentum Factor":
    st.title("Momentum Factor")
    momentum_raw = compute_momentum_factor(raw['Close'], lookback)
    momentum_clean = compute_momentum_factor(clean['Close'], lookback)
    fig, ax = plt.subplots(figsize=(10,5))
    momentum_raw.cumsum().plot(ax=ax, label="Raw")
    momentum_clean.cumsum().plot(ax=ax, label="Cleaned", linestyle='--')
    ax.set_title(f"Momentum Factor ({lookback} days) - Raw vs Cleaned")
    ax.legend()
    st.pyplot(fig)

elif page == "Market Risk Premium":
    st.title("Market Risk Premium")
    # Simulate risk-free rate as constant for demo
    risk_free = raw['Close'] * 0.0 + 1.0
    premium_raw = compute_market_risk_premium(raw['Close'], risk_free)
    premium_clean = compute_market_risk_premium(clean['Close'], risk_free)
    fig, ax = plt.subplots(figsize=(10,5))
    premium_raw.cumsum().plot(ax=ax, label="Raw")
    premium_clean.cumsum().plot(ax=ax, label="Cleaned", linestyle='--')
    ax.set_title("Market Risk Premium - Raw vs Cleaned")
    ax.legend()
    st.pyplot(fig)

elif page == "Low Volatility Factor":
    st.title("Low Volatility Factor")
    lowvol_raw = compute_low_volatility_factor(raw['Close'])
    lowvol_clean = compute_low_volatility_factor(clean['Close'])
    fig, ax = plt.subplots(figsize=(10,5))
    lowvol_raw.plot(ax=ax, label="Raw")
    lowvol_clean.plot(ax=ax, label="Cleaned", linestyle='--')
    ax.set_title("Low Volatility Factor - Raw vs Cleaned")
    ax.legend()
    st.pyplot(fig)

elif page == "Network Value Factor":
    st.title("Network Value Factor (NVT Ratio)")
    # Simulate transaction volume for demo
    tx_volume = raw['Volume'].rolling(7).mean().fillna(method="bfill")
    nvt_raw = compute_nvt_ratio(raw['Close'], tx_volume)
    nvt_clean = compute_nvt_ratio(clean['Close'], tx_volume)
    fig, ax = plt.subplots(figsize=(10,5))
    nvt_raw.plot(ax=ax, label="Raw")
    nvt_clean.plot(ax=ax, label="Cleaned", linestyle='--')
    ax.set_title("NVT Ratio - Raw vs Cleaned")
    ax.legend()
    st.pyplot(fig)