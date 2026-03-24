# 🚀 OpenClaw Trading Assistant

<div align="center">

**Version**: v1.1.0 (2026-03-24)  
**Author**: OpenClaw Community  
**License**: MIT

[Features](#-features) • [Installation](#-installation) • [Usage](#-usage) • [Configuration](#-configuration) • [Documentation](#-documentation)

---

### 🌐 Language / 语言

**[Switch to Chinese →](README_zh.md)**

---

</div>

---

## 📖 Introduction

**OpenClaw Trading Assistant** is a complete trading decision support system that provides technical analysis, trading signals, position management, and risk monitoring.

### ✨ Key Features

- 📊 **Support & Resistance Levels** - Automatic calculation with multiple algorithms
- 📈 **Trading Signals** - Multi-indicator analysis (RSI, MACD, Moving Averages)
- 💰 **Position Calculator** - Risk-based position sizing
- 🎯 **Stop Loss & Take Profit** - Price alerts and trigger detection
- ⚠️ **Risk Management** - Risk/Reward ratio, potential profit/loss
- 🔔 **Notifications** - Feishu, DingTalk, Email (configurable)

### 🎯 Perfect For

- Stock/ETF investors
- Technical analysis enthusiasts
- Quantitative trading beginners
- OpenClaw users

---

## ✨ Features

### 1. Support & Resistance Levels

- Automatic calculation of key price levels
- Multiple algorithms: Previous High/Low, Moving Averages, Fibonacci, Pivot Points
- Strength indicator (strong/medium/weak)

**Example Output**:
```
NVDA Current Price: $175.64
Resistance: $177.26 (+0.9%), $180.00 (+2.5%)
Support: $175.00 (-0.4%), $171.72 (-2.2%)
```

---

### 2. Trading Signals

- Multi-indicator analysis (RSI, MACD, Moving Averages)
- Combined signal scoring
- Recommendations: Strong Buy / Buy / Hold / Sell / Strong Sell

**Example Output**:
```
RSI: 52.34 [Neutral]
MACD: 0.1234 [Bullish]
Moving Averages: [Bullish]
Combined: Bullish (score: 3)
Recommendation: BUY (Confidence: Medium)
```

---

### 3. Position Calculator

- Risk-based position sizing
- Risk profiles: Conservative / Moderate / Aggressive
- Confidence adjustment
- Stop-loss calculation
- Portfolio allocation

**Example Output**:
```
Total Capital: $100,000
Entry Price: $175.64
Stop Loss: $165.00
Risk Profile: Moderate

Position: 562 shares ($98,710, 98.7%)
Risk: $5,964 (5.96%)
Risk/Reward: 1:2.0
```

---

## 🛠️ Installation

### Prerequisites

- Python 3.11+
- Twelve Data API Key ([Get Free](https://twelvedata.com/pricing) - 800 calls/day)
- Alpha Vantage API Key ([Get Free](https://www.alphavantage.co/support/#api-key) - 25 calls/day)

### Quick Start

```bash
# 1. Clone repository
git clone https://github.com/XuXuClassMate/trading-assistant.git
cd trading-assistant

# 2. Install dependencies
pip install -r requirements.txt

# 3. Configure API Keys
cp .env.example .env
# Edit .env with your API Keys

# 4. Configure Watchlist
cp watchlist.txt.example watchlist.txt
# Edit watchlist.txt with your stocks

# 5. (Optional) Configure Notifications
# Edit .env and fill in notification credentials (leave empty to disable)

# 6. Test installation
python3 support_resistance.py
python3 trading_signals.py
python3 position_calculator.py
```

---

## 🌍 Internationalization

**Default Language**: English (`en`)

**Switch Language**:

```bash
# Method 1: Environment Variable
export TRADING_ASSISTANT_LANG=zh_CN

# Method 2: In Code
from i18n import set_language
set_language("zh_CN")

# Method 3: Config File
# Add to config.json: {"language": "zh_CN"}
```

**Supported Languages**:
- English (`en`) - Default
- Chinese Simplified (`zh_CN`)

📚 [See I18N Documentation](docs/I18N.md)

---

## ⚙️ Configuration

### Required

1. **API Keys** - Twelve Data & Alpha Vantage
2. **Watchlist** - Your stock list

### Optional

1. **Notifications** - Feishu, DingTalk, Email (leave empty to disable)
2. **Risk Profile** - Conservative/Moderate/Aggressive
3. **Language** - English/Chinese

📚 [See Full Configuration Guide](docs/CONFIGURATION.md)

---

## 📖 Usage

### Basic Usage

```python
# Support & Resistance
from support_resistance import calculate_support_resistance
result = calculate_support_resistance("NVDA")

# Trading Signals
from trading_signals import generate_trading_signal
result = generate_trading_signal("AAPL")

# Position Calculation
from position_calculator import calculate_position_size
result = calculate_position_size(
    total_capital=100000,
    entry_price=175.64,
    stop_loss_price=165.00,
    risk_profile="moderate"
)
```

📚 [See Full Usage Guide](README_CLAWHUB.md)

---

## 📁 Project Structure

```
trading-assistant/
├── config.py                    # Configuration
├── i18n.py                      # Internationalization
├── support_resistance.py        # Support/Resistance (Day 1)
├── trading_signals.py           # Trading Signals (Day 1)
├── position_calculator.py       # Position Calculator (Day 1)
├── stop_loss_alerts.py          # Stop Loss & Take Profit (Day 2)
├── locales/
│   ├── en.json                  # English translations
│   └── zh_CN.json               # Chinese translations
├── data/
│   └── alerts/                  # Alert persistence (JSON)
├── logs/                        # Log files
├── docs/
│   ├── I18N.md                  # i18n documentation
│   ├── CONFIGURATION.md         # Configuration guide
│   ├── PUBLISHING.md            # Package publishing guide
│   └── V1.1.0_SUCCESS.md        # v1.1.0 release summary
├── .github/
│   └── workflows/
│       ├── publish.yml          # Auto-publish workflow
│       └── publish-gh.yml       # GitHub Packages workflow
├── scripts/                     # Utility scripts
├── requirements.txt             # Dependencies
├── pyproject.toml               # Python package config
├── .env.example                 # Environment template
├── watchlist.txt.example        # Watchlist template
├── LICENSE                      # MIT License
├── README.md                    # This file (English)
└── README_zh.md                 # Chinese version
```

---

## 🧪 Testing

```bash
# Test all modules
python3 support_resistance.py
python3 trading_signals.py
python3 position_calculator.py

# Run unit tests
python3 -m pytest tests/
```

---

## 📊 Version History

### v1.1.0 (2026-03-24) - Stop Loss & Take Profit Alerts

**New Features**:
- ✅ Stop Loss & Take Profit alert system
- ✅ Automatic price trigger detection
- ✅ Risk/Reward ratio calculation
- ✅ Potential profit/loss estimation
- ✅ JSON-based alert persistence
- ✅ Detailed logging

**Files Added**:
- `stop_loss_alerts.py` - Alert management module
- `data/alerts/` - Alert data storage
- `logs/` - Log file directory

**Usage Example**:
```python
from stop_loss_alerts import StopLossAlert, calculate_stop_loss_levels

# Calculate levels
levels = calculate_stop_loss_levels(
    entry_price=175.64,
    stop_loss_percent=5.0,
    take_profit_percent=10.0
)

# Create alert
alert = StopLossAlert("NVDA", 175.64)
alert.create_alert(
    entry_price=175.64,
    stop_loss_price=levels['stop_loss_price'],
    take_profit_price=levels['take_profit_price'],
    shares=100
)
```

---

### v1.0.0 (2026-03-24) - Initial Release

**Features**:
- ✅ Support & Resistance calculation
- ✅ Trading signal generation (RSI, MACD, MA)
- ✅ Position size calculator
- ✅ Multi-language support (EN/ZH)
- ✅ Configurable notifications
- ✅ Portfolio allocation

📚 [See Full Release Notes](CHANGELOG.md)

---

## ⚠️ Disclaimer

This software is for **educational and research purposes only**. It does not constitute investment advice.

- Trading involves substantial risk
- Past performance does not guarantee future results
- Users should make independent decisions and bear their own risks
- The developers are not liable for any investment losses

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit issues or pull requests.

---

## 📚 Documentation

- [📖 README_CLAWHUB.md](README_CLAWHUB.md) - Detailed guide
- [🌍 docs/I18N.md](docs/I18N.md) - Internationalization guide
- [⚙️ docs/CONFIGURATION.md](docs/CONFIGURATION.md) - Configuration guide
- [📝 CHANGELOG.md](CHANGELOG.md) - Version history
- [❓ FAQ.md](FAQ.md) - Frequently asked questions

---

## 🙏 Acknowledgments

Thanks to these open-source projects:

- **OpenClaw** - AI assistant framework
- **Twelve Data** - Financial market data API
- **Alpha Vantage** - Stock/Forex data API
- **ClawHub** - OpenClaw skills community

---

## 📬 Contact

- **GitHub**: https://github.com/XuXuClassMate/trading-assistant
- **Issues**: https://github.com/XuXuClassMate/trading-assistant/issues
- **ClawHub**: https://clawhub.com

---

<div align="center">

**Made with ❤️ by OpenClaw Community**

[📖 Documentation](#-documentation) • [🐛 Report Issue](https://github.com/XuXuClassMate/trading-assistant/issues) • [⭐ Star Project](https://github.com/XuXuClassMate/trading-assistant)

*Last Updated*: 2026-03-24 14:05 UTC  
*Version*: v1.1.0

</div>
