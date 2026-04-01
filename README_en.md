# Trading Assistant v2.0.0

**Professional Stock Trading Analysis System**

[![GitHub Release](https://img.shields.io/github/v/release/XuXuClassMate/trading-assistant)](https://github.com/XuXuClassMate/trading-assistant/releases)
[![License](https://img.shields.io/github/license/XuXuClassMate/trading-assistant)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)

---

## 📋 Overview

Trading Assistant is a professional stock trading analysis system with technical indicators, trading signals, and position management. Supports A-shares, US stocks, and cryptocurrency markets.

### Key Features

- 📊 **Technical Analysis** - Support/resistance levels, trend lines, chart patterns
- 📈 **Trading Signals** - Buy/sell signals based on technical indicators
- 💰 **Position Management** - Position sizing, cost basis analysis
- 🔔 **Price Alerts** - Real-time monitoring and alerts
- 📉 **Backtesting** - Strategy backtesting with detailed statistics
- 🌍 **Multi-market** - A-shares, US stocks, cryptocurrency
- 🌐 **Bilingual** - Chinese and English support

---

## 🚀 Installation

### Option 1: Python pip (Recommended)

```bash
# Download release
wget https://github.com/XuXuClassMate/trading-assistant/releases/download/v2.0.0/trading-assistant-v2.0.0-security.tar.gz

# Extract
tar -xzf trading-assistant-v2.0.0-security.tar.gz
cd trading-assistant

# Install dependencies
pip install -r requirements.txt

# Set environment variables
export TWELVE_DATA_API_KEY=your_twelve_data_key
export ALPHA_VANTAGE_API_KEY=your_alpha_vantage_key

# Test installation
python3 cli.py --help
```

### Option 2: Docker

```bash
# Pull image
docker pull ghcr.io/XuXuClassMate/trading-assistant:v2.0.0

# Run with environment variables
docker run -it \
  -e TWELVE_DATA_API_KEY=your_key \
  -e ALPHA_VANTAGE_API_KEY=your_key \
  ghcr.io/XuXuClassMate/trading-assistant:v2.0.0
```

### Option 3: npm (if available)

```bash
npm install trading-assistant-v2.0.0.tgz
```

### Option 4: ClawHub (OpenClaw)

```bash
clawhub install trading-assistant@2.0.0
```

---

## ⚙️ Configuration

### Environment Variables

**Required**:
```bash
export TWELVE_DATA_API_KEY=your_twelve_data_key
export ALPHA_VANTAGE_API_KEY=your_alpha_vantage_key
```

**Optional**:
```bash
export TZ=Asia/Shanghai  # Timezone
export LANG=en_US.UTF-8  # Language (en or zh_CN)
```

### Getting API Keys

1. **Twelve Data**: https://twelvedata.com/pricing
   - Free tier: 800 requests/day
   
2. **Alpha Vantage**: https://www.alphavantage.co/support/#api-key
   - Free tier: 25 requests/day

---

## 📖 Usage

### CLI Commands

```bash
# Start interactive mode
python3 cli.py

# Support/resistance analysis
python3 support_resistance.py

# Trading signals
python3 trading_signals.py

# Position calculation
python3 position_calculator.py

# Backtesting
python3 backtest_engine_v2.py

# Real-time monitoring
python3 realtime_monitor.py

# Show help
python3 cli.py --help
```

### Interactive Mode

```bash
$ python3 cli.py

Trading Assistant v2.0.0
========================

Available commands:
  support-resistance  - Analyze support/resistance levels
  signals            - Generate trading signals
  position           - Calculate position size
  backtest           - Strategy backtesting
  monitor            - Real-time market monitoring
  alerts             - Manage price alerts
  ...

trading-assistant> 
```

---

## 🔒 Security Features (v2.0.0)

### What Changed

- ✅ Removed all `sys.path.insert()` calls
- ✅ Removed runtime `.env` file loading
- ✅ Removed `load_dotenv()` from config
- ✅ Removed sibling module imports
- ✅ API keys via environment variables only

### Security Guarantees

1. **No sibling .env access** - Only reads from standard environment variables
2. **No path manipulation** - Zero `sys.path.insert()` calls
3. **No runtime .env loading** - No automatic .env file parsing
4. **Isolated imports** - Standard Python imports only
5. **Direct API calls** - Only Twelve Data and Alpha Vantage endpoints

---

## 📁 Project Structure

```
trading-assistant/
├── cli.py                      # Command-line interface
├── config.py                   # Configuration management
├── i18n.py                     # Internationalization
├── locales/
│   ├── en.json                 # English translations
│   └── zh_CN.json              # Chinese translations
├── support_resistance.py       # Support/resistance analysis
├── trading_signals.py          # Signal generation
├── position_calculator.py      # Position sizing
├── backtest_engine_v2.py       # Backtesting engine
├── realtime_monitor.py         # Real-time monitoring
├── requirements.txt            # Python dependencies
├── pyproject.toml              # Python project metadata
└── README.md                   # This file
```

---

## 🧪 Testing

```bash
# Run tests
pytest tests/

# Test specific module
python3 -m pytest tests/test_trading_signals.py -v

# Check code style
flake8 .
black --check .
```

---

## 📊 Supported Markets

### A-Shares (China)
- Shanghai Stock Exchange (SSE)
- Shenzhen Stock Exchange (SZSE)
- Data source: Sina Finance

### US Stocks
- NYSE, NASDAQ
- Data source: Twelve Data, Alpha Vantage

### Cryptocurrency
- Bitcoin, Ethereum, etc.
- Data source: Binance, CoinGecko

---

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📝 Changelog

### v2.0.0 (2026-04-01) - Security Hardened

**Security Fixes**:
- Removed all `sys.path.insert()` calls (9 files)
- Removed runtime `.env` file loading (4 files)
- Removed `load_dotenv()` from `config.py`
- Removed sibling module imports
- Updated SKILL.md security model

**Breaking Changes**:
- API keys must be set via environment variables (no `.env` file loading)
- Removed `python-dotenv` dependency

### v1.3.1 (2026-03-28)

- Bug fixes and improvements

---

## ⚠️ Disclaimer

This software is for **educational and research purposes only**.

- ❌ Not financial advice
- ❌ Not recommended for actual trading
- ❌ Use at your own risk
- ✅ Past performance does not guarantee future results

---

## 📞 Support

- **GitHub Issues**: https://github.com/XuXuClassMate/trading-assistant/issues
- **Email**: mail@xuxuclassmate.com
- **Documentation**: https://github.com/XuXuClassMate/trading-assistant#readme

---

## 📄 License

MIT License - see [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- [Twelve Data](https://twelvedata.com/) - Market data API
- [Alpha Vantage](https://www.alphavantage.co/) - Stock market API
- [OpenClaw](https://openclaw.ai/) - AI agent framework

---

**Author**: XuXuClassMate  
**Version**: 2.0.0  
**Last Updated**: 2026-04-01
