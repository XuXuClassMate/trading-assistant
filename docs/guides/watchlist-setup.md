# 📋 Watchlist Setup Guide

## Overview

The watchlist is your personal list of stocks/crypto symbols that the Trading Assistant monitors and analyzes.

## Quick Setup

### Method 1: Create Manually

```bash
# Create watchlist file
echo "NVDA" > watchlist.txt
echo "AAPL" >> watchlist.txt
echo "SPY" >> watchlist.txt
```

### Method 2: Copy Example

```bash
# Download example template
curl -O https://raw.githubusercontent.com/XuXuClassMate/trading-assistant/main/watchlist.txt.example
cp watchlist.txt.example watchlist.txt
```

## File Format

**One symbol per line**:
```
NVDA
AAPL
MSFT
GOOGL
TSLA
SPY
QQQ
BTC-USD
ETH-USD
```

## Supported Symbols

### US Stocks
- Individual stocks: `NVDA`, `AAPL`, `TSLA`
- ETFs: `SPY`, `QQQ`, `IWM`

### Cryptocurrency (via Binance/CoinGecko)
- Bitcoin: `BTC-USD` or `BTCUSDT`
- Ethereum: `ETH-USD` or `ETHUSDT`
- Others: `SOL-USD`, `BNB-USD`

### A-Share Stocks (China)
- Shanghai: `600519.ss` (Kweichow Moutai)
- Shenzhen: `000858.sz` (Wuliangye)

## Location

Place `watchlist.txt` in your working directory:

```
your-working-directory/
├── .env              # API keys
├── watchlist.txt     # Your stock list
└── ...
```

## Usage Examples

### Analyze All Stocks in Watchlist
```bash
ta analyze
```

### Real-time Monitor
```bash
ta monitor
```

### Backtest Signals
```bash
ta backtest --days 30
```

## Tips

1. **Keep it focused**: 5-20 symbols is ideal for daily analysis
2. **Update regularly**: Remove stocks you're no longer tracking
3. **Never commit to Git**: Add to `.gitignore` (contains your personal strategy)

## Troubleshooting

### "No symbols in watchlist"
**Solution**: Make sure `watchlist.txt` exists and has at least one symbol:
```bash
echo "NVDA" > watchlist.txt
```

### "Invalid symbol"
**Solution**: Check symbol format:
- US stocks: `NVDA` (uppercase)
- Crypto: `BTC-USD` or `BTCUSDT`
- A-shares: `600519.ss`

## Related

- [API Keys Setup](api-keys.md)
- [Getting Started](getting-started.md)
- [Configuration Guide](../CONFIGURATION.md)
