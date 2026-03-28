# 实时监控与回测

实时监控市场动态并回测交易策略。

## 实时监控 📊

### 启动监控

```bash
# 基本用法
ta monitor --watchlist BTC ETH AAPL --run

# 自定义监控间隔（秒）
ta monitor --watchlist BTC ETH --interval 60 --run

# 设置监控列表（不启动）
ta monitor --watchlist BTC ETH AAPL
```

### 监控功能

| 功能 | 说明 |
|------|------|
| **价格预警** | 突破关键价位时提醒 |
| **波动率检测** | 检测异常波动 (>5%) |
| **支撑/阻力位** | 自动计算关键价位 |
| **交易信号** | RSI/MACD 信号生成 |

### 监控列表管理

```bash
# 查看当前监控列表
ta monitor --list

# 添加标的
ta monitor --add TSLA

# 移除标的
ta monitor --remove TSLA

# 清空列表
ta monitor --clear
```

### 配置文件

监控列表保存在 `~/.trading_assistant/watchlist.json`

**示例内容**:
```json
{
  "symbols": ["BTC", "ETH", "AAPL", "TSLA"],
  "interval": 60,
  "alerts_enabled": true
}
```

---

## 策略回测 📈

### 支持策略

| 策略 | 代码 | 说明 |
|------|------|------|
| **SMA 交叉** | `sma_crossover` | 快慢均线交叉信号 |
| **RSI 超卖** | `rsi_oversold` | RSI<30 买入 |
| **RSI 超买** | `rsi_overbought` | RSI>70 卖出 |

### 基本用法

```bash
# SMA 交叉策略回测
ta backtest AAPL 2024-01-01 2024-12-31 --strategy sma_crossover

# RSI 策略回测
ta backtest BTC 2024-06-01 2024-12-31 --strategy rsi_oversold
```

### 参数说明

| 参数 | 说明 | 示例 |
|------|------|------|
| `SYMBOL` | 股票/加密货币代码 | AAPL, BTC, ETH |
| `START_DATE` | 开始日期 (YYYY-MM-DD) | 2024-01-01 |
| `END_DATE` | 结束日期 (YYYY-MM-DD) | 2024-12-31 |
| `--strategy` | 策略名称 | sma_crossover |
| `--initial-capital` | 初始资金 | 10000 |

### 回测输出

```
📈 回测结果：AAPL (2024-01-01 至 2024-12-31)
==================================================
策略：SMA 交叉 (快线=10, 慢线=30)

初始资金：$10,000.00
最终资金：$12,450.00
总收益率：+24.5%

交易次数：15
胜率：60.0%
盈亏比：1.8

最大回撤：-8.5%
夏普比率：1.42
==================================================
```

### 策略参数自定义

编辑 `~/.trading_assistant/strategies.json`:

```json
{
  "sma_crossover": {
    "fast_period": 10,
    "slow_period": 30
  },
  "rsi_oversold": {
    "threshold": 30,
    "period": 14
  },
  "rsi_overbought": {
    "threshold": 70,
    "period": 14
  }
}
```

---

## 高级功能 🚀

### 批量回测

创建回测脚本 `batch_backtest.py`:

```python
#!/usr/bin/env python3
from backtest_engine import BacktestEngine

engine = BacktestEngine()

symbols = ['AAPL', 'GOOGL', 'TSLA', 'MSFT']
for symbol in symbols:
    print(f"\n回测 {symbol}...")
    engine.run_backtest(symbol, '2024-01-01', '2024-12-31', 'sma_crossover')
```

### 性能优化

使用缓存加速回测：

```bash
# 启用缓存（默认开启）
export TRADING_ASSISTANT_CACHE=true

# 清除缓存
ta cache --clear
```

### 导出数据

```bash
# 导出回测结果为 CSV
ta backtest AAPL 2024-01-01 2024-12-31 --export csv

# 导出为 JSON
ta backtest AAPL 2024-01-01 2024-12-31 --export json
```

---

## 常见问题 ❓

### Q: 监控间隔设置多少合适？

**A**: 建议 ≥60 秒，避免触发 API 速率限制。
- Twelve Data: 800 次/天
- Alpha Vantage: 25 次/天

### Q: 回测数据从哪里获取？

**A**: 使用 Twelve Data API 获取历史数据。
- 免费账户：每日 800 次调用
- 数据覆盖：美股、加密货币、外汇

### Q: 如何优化策略参数？

**A**: 使用参数扫描：
```python
# 示例：测试不同 SMA 周期
for fast in [5, 10, 15, 20]:
    for slow in [20, 30, 50, 100]:
        # 回测并记录结果
```

### Q: 支持哪些市场？

**A**: 
- ✅ 美股 (AAPL, TSLA, GOOGL...)
- ✅ 加密货币 (BTC, ETH, SOL...)
- ✅ 外汇 (EURUSD, GBPUSD...)
- ⏳ A 股 (计划中)

---

## 下一步

- 📚 查看 [交易信号指南](trading-signals.md) 了解信号生成
- 📊 查看 [仓位管理指南](position-management.md) 学习风险控制
- 🔔 查看 [价格预警指南](price-alerts.md) 设置提醒
