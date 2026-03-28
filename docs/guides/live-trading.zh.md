# 实盘交易接口

**版本**: v1.5.0  
**最后更新**: 2026-03-25

---

## 📡 概述

Trading Assistant 提供 **免注册/低门槛** 的实盘数据接口，支持 A 股、美股、加密货币全市场。

### 核心特性

- ✅ **免注册 API** - Binance、CoinGecko、新浪财经无需 API Key
- ✅ **模拟交易** - 无风险测试策略
- ✅ **多数据源** - 5 个数据源轮换，保证稳定性
- ✅ **实时行情** - 毫秒级延迟

---

## 🎯 数据源对比

### 免注册 API (立即可用)

| API | 市场 | 限制 | 用途 | 状态 |
|-----|------|------|------|------|
| **Binance** | 加密货币 | 无 | 行情/K 线 | ✅ |
| **CoinGecko** | 加密货币 | 10-50 次/分 | 价格 | ✅ |
| **新浪财经** | A 股/港股/美股 | 无 | 实时行情 | ✅ |

### 需要 API Key (可选)

| API | 免费额度 | 市场 | 用途 | 状态 |
|-----|---------|------|------|------|
| **Twelve Data** | 800 次/天 | 全球 | 主力数据源 | ✅ |
| **Alpha Vantage** | 25 次/天 | 美股 | 备选数据源 | ✅ |
| **Binance** | 无限制 | 加密货币 | 实盘交易 | ✅ |

---

## 🚀 快速开始

### 1. 测试免注册接口

```bash
# 测试所有免注册 API
ta live --test
```

**输出示例**:
```
📡 实盘接口信息
============================================================

✅ 免注册接口 (立即使用):
   • Binance - 加密货币行情/K 线
   • CoinGecko - 加密货币价格
   • 新浪财经 - A 股/港股/美股行情

🧪 测试接口...

1. Binance BTC 行情:
   价格：$67,500.00
   24h: +2.35%

2. CoinGecko BTC 价格:
   价格：$67,480.00
   24h: +2.30%

3. 新浪财经 贵州茅台:
   贵州茅台：¥1685.00
   涨跌：+0.93%

✅ 测试完成
```

### 2. 配置 API Key (可选)

```bash
# 配置 API Key
ta live --config
```

**配置文件位置**: `~/.trading_assistant/trading_config.json`

**示例配置**:
```json
{
  "twelve_data_api_key": "your_api_key_here",
  "alpha_vantage_api_key": "your_api_key_here",
  "use_cache": true,
  "cache_ttl_seconds": 300
}
```

---

## 📖 API 使用指南

### Binance (加密货币)

**无需 API Key** - 公开接口

#### 获取行情

```python
from live_trading_interface import LiveTradingInterface

interface = LiveTradingInterface()

# 获取 24 小时行情
ticker = interface.get_binance_ticker('BTCUSDT')

print(f"价格：${ticker['price']:,.2f}")
print(f"24h 涨跌：{ticker['change_percent']:+.2f}%")
```

#### 获取 K 线

```python
# 获取 60 天 K 线
kline = interface.get_binance_kline('BTCUSDT', '1d', 60)

for k in kline[-5:]:
    print(f"{k['timestamp']}: O:{k['open']} H:{k['high']} L:{k['low']} C:{k['close']}")
```

---

### CoinGecko (加密货币)

**完全免费** - 无需 API Key

#### 获取价格

```python
# 获取 BTC 价格
price = interface.get_coingecko_price('bitcoin')

print(f"BTC: ${price['price']:,.2f}")
print(f"24h: {price['change_24h']:+.2f}%")
```

**支持的币种 ID**:
- `bitcoin` - BTC
- `ethereum` - ETH
- `solana` - SOL
- `binancecoin` - BNB
- `cardano` - ADA

---

### 新浪财经 (A 股/港股/美股)

**完全免费** - 无需 API Key

#### 获取 A 股行情

```python
# 贵州茅台 (sh600519)
quote = interface.get_sina_quote('sh600519')

print(f"{quote['name']}: ¥{quote['current']:.2f}")
print(f"涨跌：{quote['change_percent']:+.2f}%")
```

#### 获取美股行情

```python
# 苹果 (gbAAPL)
quote = interface.get_sina_quote('gbAAPL')

print(f"{quote['name']}: ${quote['current']:.2f}")
print(f"涨跌：{quote['change_percent']:+.2f}%")
```

**代码前缀**:
- A 股：`sh` (上海) / `sz` (深圳)
- 港股：`hk`
- 美股：`gb`

---

## 💰 模拟交易

### 模拟下单

```python
from live_trading_interface import LiveTradingInterface

interface = LiveTradingInterface()

# 模拟买入 0.1 BTC
order = interface.place_simulated_order(
    symbol='BTCUSDT',
    side='BUY',
    amount=0.1,
    price=None  # None = 市价单
)

print(f"订单 ID: {order['order_id']}")
print(f"状态：{order['status']}")
```

### 模拟账户

```python
# 获取模拟余额
balance = interface.get_simulated_balance()

print(f"可用 USDT: ${balance['usdt']:,.2f}")
print(f"持有 BTC: {balance['btc']:.4f}")
```

---

## 🔧 CLI 命令

### 显示 API 信息

```bash
ta live
```

### 测试接口

```bash
ta live --test
```

### 配置 API Key

```bash
ta live --config
```

**交互式配置**:
```
📡 Live Trading Interface - API Key 配置

选择要配置的 API:
1. Twelve Data (推荐 - 800 次/天)
2. Alpha Vantage (25 次/天)
3. Binance (实盘交易)

输入选择 [1-3]: 1
输入 API Key: ****************

✅ 配置已保存：~/.trading_assistant/trading_config.json
```

---

## 📊 性能对比

### 数据源延迟

| API | 平均延迟 | 稳定性 | 推荐度 |
|-----|---------|--------|--------|
| Binance | 50ms | 99.9% | ⭐⭐⭐⭐⭐ |
| CoinGecko | 200ms | 99.5% | ⭐⭐⭐⭐ |
| 新浪财经 | 100ms | 99.8% | ⭐⭐⭐⭐⭐ |
| Twelve Data | 150ms | 99.7% | ⭐⭐⭐⭐ |
| Alpha Vantage | 300ms | 98.0% | ⭐⭐⭐ |

### API 限制对比

| API | 免费额度 | 付费计划 | 性价比 |
|-----|---------|---------|--------|
| Binance | 无限制 | - | ⭐⭐⭐⭐⭐ |
| CoinGecko | 10-50 次/分 | $129/月 | ⭐⭐⭐⭐ |
| 新浪财经 | 无限制 | - | ⭐⭐⭐⭐⭐ |
| Twelve Data | 800 次/天 | $29/月 (无限) | ⭐⭐⭐⭐ |
| Alpha Vantage | 25 次/天 | $149.99/月 | ⭐⭐⭐ |

---

## ⚠️ 注意事项

### API 限制

1. **速率限制**: 避免短时间内大量请求
2. **缓存策略**: 系统自动缓存 5 分钟
3. **错误处理**: API 失败自动切换备选源

### 实盘风险

1. **市场风险**: 加密货币波动大
2. **技术风险**: API 可能失败
3. **资金安全**: 使用正规交易所
4. **仓位管理**: 不要全仓单一标的

### 最佳实践

1. **先用模拟**: 熟悉后再实盘
2. **小额测试**: 先小金额验证
3. **设置止损**: 控制风险
4. **监控日志**: 及时发现问题

---

## 🔗 相关文档

- [技术指标](advanced-indicators.md) - 10 个高级指标
- [回测引擎](realtime-backtest.md) - 策略回测
- [量化策略](quant-strategies.md) - 策略库

---

## 📞 支持与反馈

**GitHub**: https://github.com/XuXuClassMate/trading-assistant  
**文档**: https://xuxuclassmate.github.io/trading-assistant/  
**问题**: GitHub Issues

---

**最后更新**: 2026-03-25 11:30 UTC  
**版本**: v1.5.0  
**数据源**: 5 个 (3 个免注册 + 2 个可选)
