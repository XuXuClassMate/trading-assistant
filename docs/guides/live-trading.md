# Live Trading Interface

**Version**: v1.3.2  
**Last Updated**: 2026-03-25

---

## 📡 Overview

Trading Assistant provides **free/low-barrier** live trading data APIs, supporting A-shares, US stocks, and cryptocurrencies.

### Core Features

- ✅ **Free APIs** - Binance, CoinGecko, Sina Finance require no API Key
- ✅ **Simulated Trading** - Test strategies risk-free
- ✅ **Multiple Data Sources** - 5 sources with failover for stability
- ✅ **Real-Time Quotes** - Millisecond-level latency

---

## 🎯 Data Source Comparison

### Free APIs (Ready to Use)

| API | Market | Limit | Use | Status |
|-----|--------|-------|-----|--------|
| **Binance** | Crypto | None | Ticker/K-line | ✅ |
| **CoinGecko** | Crypto | 10-50/min | Prices | ✅ |
| **Sina Finance** | A-Share/HK/US | None | Real-time quotes | ✅ |

### Optional API Keys

| API | Free Tier | Market | Use | Status |
|-----|-----------|--------|-----|--------|
| **Twelve Data** | 800/day | Global | Primary source | ✅ |
| **Alpha Vantage** | 25/day | US Stocks | Backup source | ✅ |
| **Binance** | Unlimited | Crypto | Live trading | ✅ |

---

## 🚀 Quick Start

### 1. Test Free APIs

```bash
# Test all free APIs
ta live --test
```

**Output Example**:
```
📡 Live Trading Interface Info
============================================================

✅ Free APIs (Use Immediately):
   • Binance - Crypto ticker/K-line
   • CoinGecko - Crypto prices
   • Sina Finance - A-Share/HK/US quotes

🧪 Testing APIs...

1. Binance BTC Ticker:
   Price: $67,500.00
   24h: +2.35%

2. CoinGecko BTC Price:
   Price: $67,480.00
   24h: +2.30%

3. Sina Finance Kweichow Moutai:
   Kweichow Moutai: ¥1685.00
   Change: +0.93%

✅ Test Complete
```

### 2. Configure API Keys (Optional)

```bash
# Configure API Keys
ta live --config
```

**Config File Location**: `~/.trading_assistant/trading_config.json`

**Example Config**:
```json
{
  "twelve_data_api_key": "your_api_key_here",
  "alpha_vantage_api_key": "your_api_key_here",
  "use_cache": true,
  "cache_ttl_seconds": 300
}
```

---

## 📖 API Usage Guide

### Binance (Crypto)

**No API Key Required** - Public endpoints

#### Get Ticker

```python
from live_trading_interface import LiveTradingInterface

interface = LiveTradingInterface()

# Get 24h ticker
ticker = interface.get_binance_ticker('BTCUSDT')

print(f"Price: ${ticker['price']:,.2f}")
print(f"24h Change: {ticker['change_percent']:+.2f}%")
```

#### Get K-Line

```python
# Get 60 days K-line
kline = interface.get_binance_kline('BTCUSDT', '1d', 60)

for k in kline[-5:]:
    print(f"{k['timestamp']}: O:{k['open']} H:{k['high']} L:{k['low']} C:{k['close']}")
```

---

### CoinGecko (Crypto)

**Completely Free** - No API Key required

#### Get Price

```python
# Get BTC price
price = interface.get_coingecko_price('bitcoin')

print(f"BTC: ${price['price']:,.2f}")
print(f"24h Change: {price['change_24h']:+.2f}%")
```

**Supported Coin IDs**:
- `bitcoin` - BTC
- `ethereum` - ETH
- `solana` - SOL
- `binancecoin` - BNB
- `cardano` - ADA

---

### Sina Finance (A-Share/HK/US)

**Completely Free** - No API Key required

#### Get A-Share Quote

```python
# Kweichow Moutai (sh600519)
quote = interface.get_sina_quote('sh600519')

print(f"{quote['name']}: ¥{quote['current']:.2f}")
print(f"Change: {quote['change_percent']:+.2f}%")
```

#### Get US Stock Quote

```python
# Apple (gbAAPL)
quote = interface.get_sina_quote('gbAAPL')

print(f"{quote['name']}: ${quote['current']:.2f}")
print(f"Change: {quote['change_percent']:+.2f}%")
```

**Symbol Prefixes**:
- A-Share: `sh` (Shanghai) / `sz` (Shenzhen)
- HK Stock: `hk`
- US Stock: `gb`

---

## 💰 Simulated Trading

### Place Simulated Order

```python
from live_trading_interface import LiveTradingInterface

interface = LiveTradingInterface()

# Simulated BUY 0.1 BTC
order = interface.place_simulated_order(
    symbol='BTCUSDT',
    side='BUY',
    amount=0.1,
    price=None  # None = Market order
)

print(f"Order ID: {order['order_id']}")
print(f"Status: {order['status']}")
```

### Simulated Account

```python
# Get simulated balance
balance = interface.get_simulated_balance()

print(f"Available USDT: ${balance['usdt']:,.2f}")
print(f"Held BTC: {balance['btc']:.4f}")
```

---

## 🔧 CLI Commands

### Show API Info

```bash
ta live
```

### Test APIs

```bash
ta live --test
```

### Configure API Keys

```bash
ta live --config
```

**Interactive Configuration**:
```
📡 Live Trading Interface - API Key Configuration

Select API to configure:
1. Twelve Data (Recommended - 800/day)
2. Alpha Vantage (25/day)
3. Binance (Live trading)

Enter choice [1-3]: 1
Enter API Key: ****************

✅ Configuration saved: ~/.trading_assistant/trading_config.json
```

---

## 📊 Performance Comparison

### API Latency

| API | Avg Latency | Stability | Rating |
|-----|-------------|-----------|--------|
| Binance | 50ms | 99.9% | ⭐⭐⭐⭐⭐ |
| CoinGecko | 200ms | 99.5% | ⭐⭐⭐⭐ |
| Sina Finance | 100ms | 99.8% | ⭐⭐⭐⭐⭐ |
| Twelve Data | 150ms | 99.7% | ⭐⭐⭐⭐ |
| Alpha Vantage | 300ms | 98.0% | ⭐⭐⭐ |

### API Limit Comparison

| API | Free Tier | Paid Plan | Value |
|-----|-----------|-----------|-------|
| Binance | Unlimited | - | ⭐⭐⭐⭐⭐ |
| CoinGecko | 10-50/min | $129/month | ⭐⭐⭐⭐ |
| Sina Finance | Unlimited | - | ⭐⭐⭐⭐⭐ |
| Twelve Data | 800/day | $29/month (unlimited) | ⭐⭐⭐⭐ |
| Alpha Vantage | 25/day | $149.99/month | ⭐⭐⭐ |

---

## ⚠️ Considerations

### API Limitations

1. **Rate Limits**: Avoid excessive requests in short time
2. **Cache Strategy**: System auto-caches for 5 minutes
3. **Error Handling**: Auto-failover to backup sources

### Live Trading Risks

1. **Market Risk**: High crypto volatility
2. **Technical Risk**: API may fail
3. **Fund Security**: Use regulated exchanges
4. **Position Management**: Don't go all-in on single asset

### Best Practices

1. **Start with Simulation**: Practice before live trading
2. **Small Tests**: Verify with small amounts first
3. **Set Stop-Loss**: Control risk
4. **Monitor Logs**: Catch issues early

---

## 🔗 Related Documents

- [Technical Indicators](advanced-indicators.md) - 10 advanced indicators
- [Backtest Engine](realtime-backtest.md) - Strategy backtesting
- [Quantitative Strategies](quant-strategies-a-share.zh.md) - Strategy library

---

## 📞 Support & Feedback

**GitHub**: https://github.com/XuXuClassMate/trading-assistant  
**Docs**: https://xuxuclassmate.github.io/trading-assistant/  
**Issues**: GitHub Issues

---

**Last Updated**: 2026-03-25 12:00 UTC  
**Version**: v1.3.2  
**Data Sources**: 5 (3 free + 2 optional)
