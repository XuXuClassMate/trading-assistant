# 🚀 Getting Started Guide

**Time**: 15 minutes  
**Level**: Beginner

---

## ✅ Prerequisites

- Trading Assistant installed ([Installation Guide](install-overview.md))
- API keys configured ([API Settings](api-keys.md))

---

## 📝 Step 1: Verify Installation

```bash
ta --version
```

Expected output:
```
OpenClaw Trading Assistant CLI v1.3.2
```

---

## 📝 Step 2: Configure API Keys

Create `.env` file in your working directory:

```bash
# Create .env file
cat > .env << EOF
TWELVE_DATA_API_KEY=your_key_here
ALPHA_VANTAGE_API_KEY=your_key_here
LANGUAGE=en
EOF
```

[→ API Setup Guide](api-keys.md)

---

## 📝 Step 3: Setup Watchlist

Create `watchlist.txt` with stocks to monitor:

```bash
cat > watchlist.txt << EOF
NVDA
AAPL
MSFT
GOOGL
TSLA
EOF
```

[→ Watchlist Setup](install-overview.md#watchlist)

---

## 📝 Step 4: Run Your First Analysis

### Interactive Mode

```bash
ta
```

You'll see:
```
============================================================
  OpenClaw Trading Assistant CLI
  Version: 1.3.2
============================================================

ta> 
```

Type commands:
```
ta> help
ta> sig
ta> exit
```

### Direct Command

```bash
# Analyze all stocks in watchlist
ta all
```

---

## 📊 Understanding Output

### Trading Signals Example

```
📈 Generating signals...

NVDA:
  RSI: 52.34 [Neutral]
  MACD: 0.1234 [Bullish]
  Moving Averages: [Bullish]
  Combined: Bullish (score: 3)
  Recommendation: BUY (Confidence: Medium)

✅ Done!
```

**What it means**:
- **RSI**: Momentum indicator (30-70 is neutral)
- **MACD**: Trend indicator (positive = bullish)
- **Moving Averages**: Price trend direction
- **Combined**: Overall signal
- **Recommendation**: Action suggestion

---

## 🎯 Common Workflows

### Daily Market Check

```bash
# Quick signals for watchlist
ta sig

# Detailed analysis for specific stock
ta sig --symbol NVDA

# All analysis (SR + Signals + Position)
ta all
```

### Position Planning

```bash
# Calculate position for trade
ta pos --symbol NVDA --price 175 --capital 10000 --risk 2

# Output shows:
# - Shares to buy
# - Position value
# - Risk amount
# - Stop loss level
```

### Price Alerts

```bash
# List existing alerts
ta alerts list

# Create new alert
ta alerts create --symbol NVDA --entry 175 --stop 170 --target 185

# Check if alerts triggered
ta alerts check
```

---

## 📚 Learn More

### CLI Commands

| Command | Description |
|---------|-------------|
| `ta` | Interactive mode |
| `ta sig` | Trading signals |
| `ta sr` | Support/Resistance |
| `ta pos` | Position calculator |
| `ta alerts` | Price alerts |
| `ta all` | Full analysis |

[→ Full CLI Reference](../CLI.md)

### Advanced Topics

- [Advanced Indicators](advanced-indicators.md)
- [Risk Management](risk-management.md)
- [Price Alerts](price-alerts.md)

---

## ❓ Troubleshooting

### "API Key Invalid"

Check your `.env` file:
```bash
cat .env
```

Make sure keys are correct (no extra spaces).

### "No stocks in watchlist"

Create watchlist.txt:
```bash
echo "NVDA" > watchlist.txt
echo "AAPL" >> watchlist.txt
```

### "Command not found: ta"

Make sure installation completed:
```bash
# For pip
pip show openclaw-trading-assistant

# For npm
npm list -g @xuxuclassmate/openclaw-trading-assistant
```

---

## 🎉 You're Ready!

Now you can:
- ✅ Generate trading signals
- ✅ Analyze support/resistance
- ✅ Calculate position sizes
- ✅ Set price alerts

**Next**: [Trading Signals Guide](trading-signals.md)
