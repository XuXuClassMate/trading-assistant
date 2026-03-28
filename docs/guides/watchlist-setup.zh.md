# 📋 自选股设置指南

## 概述

自选股是你个人关注的股票/加密货币列表，交易助手会监控和分析这些标的。

## 快速设置

### 方法 1：手动创建

```bash
# 创建自选股文件
echo "NVDA" > watchlist.txt
echo "AAPL" >> watchlist.txt
echo "SPY" >> watchlist.txt
```

### 方法 2：复制示例

```bash
# 下载示例模板
curl -O https://raw.githubusercontent.com/XuXuClassMate/trading-assistant/main/watchlist.txt.example
cp watchlist.txt.example watchlist.txt
```

## 文件格式

**每行一个标的**：
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

## 支持的标的类型

### 美股
- 个股：`NVDA`, `AAPL`, `TSLA`
- ETF: `SPY`, `QQQ`, `IWM`

### 加密货币 (通过 Binance/CoinGecko)
- 比特币：`BTC-USD` 或 `BTCUSDT`
- 以太坊：`ETH-USD` 或 `ETHUSDT`
- 其他：`SOL-USD`, `BNB-USD`

### A 股 (中国)
- 上海：`600519.ss` (贵州茅台)
- 深圳：`000858.sz` (五粮液)

## 文件位置

将 `watchlist.txt` 放在工作目录：

```
your-working-directory/
├── .env              # API 密钥
├── watchlist.txt     # 你的股票列表
└── ...
```

## 使用示例

### 分析所有自选股
```bash
ta analyze
```

### 实时监控
```bash
ta monitor
```

### 回测信号
```bash
ta backtest --days 30
```

## 提示

1. **保持聚焦**: 5-20 个标的最适合日常分析
2. **定期更新**: 移除不再关注的股票
3. **不要提交到 Git**: 添加到 `.gitignore` (包含你的个人策略)

## 故障排除

### "No symbols in watchlist"
**解决**: 确保 `watchlist.txt` 存在且至少有一个标的：
```bash
echo "NVDA" > watchlist.txt
```

### "Invalid symbol"
**解决**: 检查标的格式：
- 美股：`NVDA` (大写)
- 加密货币：`BTC-USD` 或 `BTCUSDT`
- A 股：`600519.ss`

## 相关文档

- [API 密钥设置](api-keys.md)
- [入门指南](getting-started.md)
- [配置指南](../CONFIGURATION.md)
