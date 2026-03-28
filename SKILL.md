---
name: trading-assistant
description: Advanced trading analysis system with technical indicators, trading signals, and position management
version: 2.0.0
author: OpenClaw Community
license: MIT
category: Finance
tags:
  - trading
  - finance
  - technical-analysis
  - stock-market
  - investment
  - openclaw
metadata:
  openclaw:
    requires:
      env:
        - TWELVE_DATA_API_KEY
        - ALPHA_VANTAGE_API_KEY
      bins:
        - python3
        - pip
    primaryEnv: TWELVE_DATA_API_KEY
    emoji: 📊
    homepage: https://github.com/XuXuClassMate/trading-assistant
---

# 📊 Trading Assistant

**Version**: v2.0.0 (Security Hardened) | **License**: MIT

Advanced trading analysis system providing technical indicators, trading signals, and position management for stock and crypto investors.

**Security Improvements in v2.0.0:**
- ✅ No external package dependencies (removed TradingAgents imports)
- ✅ No reading of sibling/parent .env files
- ✅ Direct API calls to Twelve Data and Alpha Vantage only
- ✅ All API keys loaded from standard environment variables only
- ✅ No access to files outside the project directory

---

## ✨ Features

- **Technical Indicators**: RSI, MACD, Bollinger Bands, KDJ, CCI, ADX, ATR, OBV, VWAP
- **Trading Signals**: Auto-generated BUY/SELL/HOLD signals with confidence scores
- **Position Sizing**: Smart position calculator based on risk profile and stop-loss
- **Support/Resistance**: Automatic calculation of key price levels
- **Multi-Market**: Support for A-shares, US stocks, and cryptocurrencies
- **Daily Reports**: Small (10s), Medium (1min), Large (5min) report formats
- **News Sentiment**: Alpha Vantage news sentiment analysis
- **Portfolio Management**: Track holdings and P&L

---

## 🚀 Quick Start

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Configure API Keys

Create `.env` file in the project directory:

```bash
TWELVE_DATA_API_KEY=your_twelve_data_key
ALPHA_VANTAGE_API_KEY=your_alpha_vantage_key
```

Get free API keys:
- **Twelve Data**: https://twelvedata.com (800 calls/day)
- **Alpha Vantage**: https://www.alphavantage.co (25 calls/day)

### 3. Test Installation

```bash
python3 support_resistance.py
python3 trading_signals.py
python3 position_calculator.py
```

---

## 📖 Basic Usage

### Generate Trading Signal

```python
from trading_signals import generate_trading_signal
result = generate_trading_signal("AAPL")
print(result)
```

### Calculate Position Size

```python
from position_calculator import calculate_position_size
result = calculate_position_size(
    total_capital=100000,
    entry_price=175.64,
    stop_loss_price=165.00,
    risk_profile="moderate"
)
```

### Calculate Support/Resistance

```python
from support_resistance import calculate_support_resistance
result = calculate_support_resistance("NVDA")
```

---

## 📁 Directory Structure

```
trading-assistant/
├── SKILL.md                 # This file
├── README.md                # Full documentation (Chinese)
├── README_en.md             # Full documentation (English)
├── requirements.txt         # Dependencies
├── .env.example             # Config template
├── config.py                # Configuration (v2.0: no external .env access)
├── support_resistance.py    # Support/resistance module
├── trading_signals.py       # Signal generator
├── position_calculator.py   # Position sizing
├── daily_report.py          # Daily report generator
├── portfolio_manager.py     # Portfolio tracking
└── news_sentiment_monitor.py # News sentiment analysis
```

---

## 🔒 Security Model

### What This Skill Does:
- ✅ Reads API keys from **standard environment variables** only
- ✅ Reads `.env` file **in its own directory** only
- ✅ Makes HTTP requests to **Twelve Data** and **Alpha Vantage** APIs
- ✅ Writes logs and reports to **its own directory** (`logs/`, `reports/`, `data/`)
- ✅ Reads user-configured `watchlist.txt` and `config.json`

### What This Skill Does NOT Do:
- ❌ Does NOT read `.env` files from parent directories or sibling projects
- ❌ Does NOT import or execute external packages (e.g., TradingAgents)
- ❌ Does NOT access files outside its project directory
- ❌ Does NOT send data to unauthorized endpoints
- ❌ Does NOT execute background tasks or autonomous actions
- ❌ Does NOT require brokerage or trading credentials

### API Keys Security:
- Only provide `TWELVE_DATA_API_KEY` and `ALPHA_VANTAGE_API_KEY`
- **DO NOT** provide brokerage credentials (IBKR, Robinhood, etc.)
- **DO NOT** provide exchange API keys (Binance, Coinbase, etc.)
- This tool is **read-only** - it analyzes data but does not trade

---

## 📚 Documentation

For detailed usage including daily reports, learning system, and automation setup, see:

- **Chinese**: `README.md`
- **English**: `README_en.md`
- **GitHub**: https://github.com/XuXuClassMate/trading-assistant

---

## ⚠️ Disclaimer

**For educational and research purposes only. Not financial advice.**

- Market investments carry risks
- Past performance does not guarantee future results
- Users are responsible for their own investment decisions
- This tool does not execute trades or provide brokerage services

---

## 🔗 Links

- **GitHub**: https://github.com/XuXuClassMate/trading-assistant
- **Issues**: https://github.com/XuXuClassMate/trading-assistant/issues
- **OpenClaw**: https://openclaw.ai
- **ClawHub**: https://clawhub.com

---

**Last Updated**: 2026-03-28
**Security Audit**: v2.0.0 - Removed external dependencies, hardened API key handling
