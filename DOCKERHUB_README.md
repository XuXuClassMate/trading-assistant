# 🚀 OpenClaw Trading Assistant

<div align="center">

**Your AI-Powered Trading Decision Support System**

[![Version](https://img.shields.io/github/v/release/XuXuClassMate/trading-assistant?label=version)](https://github.com/XuXuClassMate/trading-assistant/releases)
[![Docker Pulls](https://img.shields.io/docker/pulls/xuxuclassmate/trading-assistant)](https://hub.docker.com/r/xuxuclassmate/trading-assistant)
[![License](https://img.shields.io/github/license/XuXuClassMate/trading-assistant)](https://github.com/XuXuClassMate/trading-assistant/blob/main/LICENSE)

[📚 Documentation](https://xuxuclassmate.github.io/trading-assistant/) • [🐙 GitHub](https://github.com/XuXuClassMate/trading-assistant) • [📦 PyPI](https://pypi.org/project/openclaw-trading-assistant/)

</div>

---

## 📖 What is Trading Assistant?

**Trading Assistant** is a comprehensive trading decision support system that provides:

- 📊 **Technical Analysis** - Support & Resistance levels with multiple algorithms
- 🎯 **Trading Signals** - RSI, MACD, Moving Averages combined signals
- 💰 **Position Calculator** - Risk-based position sizing
- 🔔 **Price Alerts** - Automated stop-loss and take-profit monitoring
- 🌐 **Multi-language** - English & Chinese support

Perfect for traders who want data-driven insights without the noise.

---

## 🚀 Quick Start

### 1️⃣ Pull the Image

```bash
docker pull xuxuclassmate/trading-assistant:latest
```

### 2️⃣ Create Configuration

```bash
# Create config directory
mkdir -p ta-config && cd ta-config

# Download .env template
curl -O https://raw.githubusercontent.com/XuXuClassMate/trading-assistant/main/.env.example
cp .env.example .env

# Download watchlist template
curl -O https://raw.githubusercontent.com/XuXuClassMate/trading-assistant/main/watchlist.txt.example
cp watchlist.txt.example watchlist.txt
```

### 3️⃣ Configure API Keys

Edit `.env` with your free API keys:

```bash
nano .env
```

```env
# Get free API keys:
# Twelve Data: https://twelvedata.com/pricing (800 calls/day)
# Alpha Vantage: https://www.alphavantage.co/support/#api-key (25 calls/day)

TWELVE_DATA_API_KEY=your_key_here
ALPHA_VANTAGE_API_KEY=your_key_here
LANGUAGE=en  # or 'zh' for Chinese
```

### 4️⃣ Run!

**Interactive Mode**:
```bash
docker run --rm -it \
  -v $(pwd)/.env:/app/.env \
  -v $(pwd)/watchlist.txt:/app/watchlist.txt \
  xuxuclassmate/trading-assistant:latest
```

**One-Command Analysis**:
```bash
docker run --rm -it \
  -v $(pwd)/.env:/app/.env \
  -v $(pwd)/watchlist.txt:/app/watchlist.txt \
  xuxuclassmate/trading-assistant:latest \
  ta all
```

---

## 🖥️ CLI Commands

| Command | Shortcut | Description |
|---------|----------|-------------|
| `ta` | - | Start interactive mode |
| `ta sig` | `ta signals` | Generate trading signals |
| `ta sr` | `ta support-resistance` | Analyze support/resistance |
| `ta pos` | `ta position` | Calculate position size |
| `ta alerts` | `ta alert` | Manage price alerts |
| `ta all` | `ta analyze` | Run all analysis |
| `ta v` | `ta version` | Show version |
| `ta h` | `ta help` | Show help |

---

## 📊 Example Output

### Trading Signals
```
$ docker run --rm -it xuxuclassmate/trading-assistant:latest ta sig

📈 Generating signals...

NVDA:
  RSI: 52.34 [Neutral]
  MACD: 0.1234 [Bullish]
  Moving Averages: [Bullish]
  Combined: Bullish (score: 3)
  Recommendation: BUY (Confidence: Medium)

AAPL:
  RSI: 45.67 [Neutral]
  MACD: -0.0567 [Bearish]
  Moving Averages: [Neutral]
  Combined: Neutral (score: 1)
  Recommendation: HOLD (Confidence: Low)

✅ Done!
```

### Position Calculator
```
$ docker run --rm -it xuxuclassmate/trading-assistant:latest \
  ta pos --symbol NVDA --price 175 --capital 10000 --risk 2

💰 Calculating position...

Symbol: NVDA
Entry Price: $175.00
Total Capital: $10,000.00
Risk Percentage: 2%
Risk Amount: $200.00

Recommended Position:
  Shares: 57
  Position Value: $9,975.00
  Stop Loss: $171.50 (2% below entry)
  Max Loss: $200.00

✅ Done!
```

---

## 📋 Watchlist Configuration

Edit `watchlist.txt` with your favorite stocks:

```txt
NVDA
AAPL
MSFT
GOOGL
TSLA
AMD
META
AMZN
```

One symbol per line. The assistant will analyze all stocks in your watchlist.

---

## 🔧 Advanced Usage

### Run in Background

```bash
docker run -d --name trading-assistant \
  -v $(pwd)/.env:/app/.env \
  -v $(pwd)/watchlist.txt:/app/watchlist.txt \
  xuxuclassmate/trading-assistant:latest
```

### View Logs

```bash
docker logs -f trading-assistant
```

### Update to Latest

```bash
docker pull xuxuclassmate/trading-assistant:latest
docker stop trading-assistant
docker rm trading-assistant
# Re-run with same command
```

### Custom Environment Variables

```bash
docker run --rm -it \
  -e TWELVE_DATA_API_KEY=your_key \
  -e ALPHA_VANTAGE_API_KEY=your_key \
  -e LANGUAGE=en \
  xuxuclassmate/trading-assistant:latest
```

---

## 📚 Documentation

For complete guides, visit:

- **[Full Documentation](https://xuxuclassmate.github.io/trading-assistant/)**
- [Installation Guides](https://xuxuclassmate.github.io/trading-assistant/guides/install-overview/)
- [CLI Reference](https://xuxuclassmate.github.io/trading-assistant/CLI.md)
- [Configuration](https://xuxuclassmate.github.io/trading-assistant/config/api-keys.md)

---

## 🛠️ Alternative Installation Methods

| Method | Command | Time |
|--------|---------|------|
| **Docker** ⭐ | `docker pull xuxuclassmate/trading-assistant:latest` | 5 min |
| **pip** | `pip install openclaw-trading-assistant` | 10 min |
| **npm** | `npm install -g @xuxuclassmate/openclaw-trading-assistant` | 10 min |
| **Source** | `git clone + pip install -e .` | 15 min |

---

## ❓ FAQ

### Q: Where do I get API keys?
**A:** Both are free:
- **Twelve Data**: https://twelvedata.com/pricing (800 calls/day free)
- **Alpha Vantage**: https://www.alphavantage.co/support/#api-key (25 calls/day free)

### Q: Can I use this for real trading?
**A:** This is a **decision support tool**, not financial advice. Always do your own research and consult with a financial advisor.

### Q: How often should I run analysis?
**A:** Depends on your trading style:
- **Day traders**: Every 15-30 minutes during market hours
- **Swing traders**: Once or twice daily
- **Long-term**: Weekly is sufficient

### Q: My API calls are rate limited!
**A:** Upgrade to paid tier or reduce analysis frequency. Twelve Data offers more generous free limits (800/day vs 25/day).

---

## 🐛 Troubleshooting

### Permission Denied
```bash
# Run with current user
docker run --rm -it \
  -u $(id -u):$(id -g) \
  -v $(pwd)/.env:/app/.env \
  -v $(pwd)/watchlist.txt:/app/watchlist.txt \
  xuxuclassmate/trading-assistant:latest
```

### Command Not Found
Make sure you're using the correct command:
```bash
# Correct
ta
ta sig
ta all

# Also works (full name)
openclaw-trading-assistant
```

### Volume Mount Issues
Use absolute paths:
```bash
docker run --rm -it \
  -v /absolute/path/to/.env:/app/.env \
  -v /absolute/path/to/watchlist.txt:/app/watchlist.txt \
  xuxuclassmate/trading-assistant:latest
```

---

## 📦 Image Tags

| Tag | Description |
|-----|-------------|
| `latest` | Latest stable release |
| `1.3.1` | Specific version |
| `1.3` | Latest 1.3.x |

---

## 🔗 Links

- **GitHub**: https://github.com/XuXuClassMate/trading-assistant
- **Documentation**: https://xuxuclassmate.github.io/trading-assistant/
- **PyPI**: https://pypi.org/project/openclaw-trading-assistant/
- **npm**: https://github.com/XuXuClassMate/trading-assistant/pkgs/npm/openclaw-trading-assistant
- **Issues**: https://github.com/XuXuClassMate/trading-assistant/issues
- **Discussions**: https://github.com/XuXuClassMate/trading-assistant/discussions

---

## 📝 License

MIT License - See [LICENSE](https://github.com/XuXuClassMate/trading-assistant/blob/main/LICENSE)

---

<div align="center">

**Made with ❤️ by XuXuClassMate**

[⭐ Star on GitHub](https://github.com/XuXuClassMate/trading-assistant) • [📦 Pull on Docker Hub](https://hub.docker.com/r/xuxuclassmate/trading-assistant)

</div>
