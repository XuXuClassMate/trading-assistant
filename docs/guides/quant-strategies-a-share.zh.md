# 量化策略与 A 股支持

新增量化策略库和 A 股数据支持功能。

## 新增功能 🎯

### 1. 更多量化策略 (4 个)

| 策略 | 说明 | 适用场景 |
|------|------|---------|
| **多因子选股** | 5 因子评分系统 | 股票筛选 |
| **均值回归** | Z-Score 偏离分析 | 震荡市 |
| **动量突破** | N 日高低点突破 | 趋势市 |
| **网格交易** | 区间低买高卖 | 震荡市 |

### 2. 量化单进场提示 🚨

**功能**:
- 多条件入场检测
- 实时监控股票池
- 进场信号推送
- 条件单管理

**触发条件**:
1. ✅ 量化信号：BULLISH 且置信度 > 60%
2. ✅ 技术信号：BUY 或 STRONG_BUY
3. ✅ 风险收益比：≥ 1.5
4. ✅ 价格位置：< 30% 分位

### 3. A 股数据支持 🇨🇳

**数据源**: 新浪财经 API (免费实时)

**支持**:
- 实时行情
- K 线数据
- 股票列表
- 市场状态

---

## CLI 命令 (新增 3 个)

### 量化进场提示

```bash
# 检查入场信号
ta entry

# 检查特定标的
ta entry BTC

# 使用 A 股数据
ta entry --a-share

# 添加标的到监控列表
ta entry --add 600519

# 显示监控列表
ta entry --list

# 显示历史警报
ta entry --history

# 持续监控 (每 5 分钟)
ta entry --continuous --interval 300
```

### 量化策略演示

```bash
# 演示所有策略
ta strategies
```

### A 股数据查询

```bash
# 实时行情 (默认：贵州茅台)
ta a-share

# 指定股票
ta a-share 000858

# K 线数据
ta a-share 600519 --kline

# K 线 (90 天)
ta a-share 300750 --kline --days 90

# 股票列表
ta a-share --list

# 市场状态
ta a-share --status
```

---

## 量化策略详解 📊

### 1. 多因子选股策略

**因子体系**:

| 因子类别 | 权重 | 指标 |
|---------|------|------|
| 价值因子 | 25% | PE (越低越好) |
| 成长因子 | 25% | 营收增长率 |
| 动量因子 | 20% | 20 日收益率 |
| 质量因子 | 20% | ROE |
| 技术因子 | 10% | RSI |

**评分标准**:
```
总分 = 价值*0.25 + 成长*0.25 + 动量*0.20 + 质量*0.20 + 技术*0.10

80-100 分：STRONG_BUY
65-79 分：BUY
50-64 分：HOLD
35-49 分：SELL
0-34 分：STRONG_SELL
```

**示例**:
```bash
$ ta strategies

📊 1. 多因子选股策略
   #1 AAPL: 72.5 分 -> BUY
   #2 GOOGL: 68.0 分 -> BUY
   #3 TSLA: 55.5 分 -> HOLD
```

### 2. 均值回归策略

**原理**: 价格偏离均线过远时会回归

**Z-Score 计算**:
```
Z = (当前价格 - N 日均价) / N 日标准差
```

**信号规则**:
| Z-Score | 信号 | 置信度 |
|---------|------|--------|
| < -2.0 | STRONG_BUY | 100% |
| -2.0 ~ -1.6 | BUY | 80% |
| -1.6 ~ 1.6 | HOLD | - |
| 1.6 ~ 2.0 | SELL | 80% |
| > 2.0 | STRONG_SELL | 100% |

**使用示例**:
```python
from quantitative_strategies import MeanReversionStrategy

mr = MeanReversionStrategy(lookback=20, threshold=2.0)
prices = [100, 102, 98, ..., 90]  # 20 日价格
signal = mr.generate_signals(prices, prices[-1])

print(f"信号：{signal['signal']}")
print(f"原因：{signal['reason']}")
```

### 3. 动量突破策略

**原理**: 价格突破 N 日高点时买入，跌破低点时卖出

**信号规则**:
```
突破 20 日高点 + 成交量放大 1.5 倍 → BUY (置信度 80%)
突破 20 日高点 → BUY (置信度 60%)
跌破 20 日低点 + 成交量放大 → SELL (置信度 80%)
跌破 20 日低点 → SELL (置信度 60%)
```

**使用示例**:
```python
from quantitative_strategies import MomentumBreakoutStrategy

mo = MomentumBreakoutStrategy(lookback=20)
signal = mo.check_breakout(prices, volumes)

if signal['signal'] == 'BUY':
    print(f"突破确认！目标价：${signal['target']:.2f}")
    print(f"止损价：${signal['stop_loss']:.2f}")
```

### 4. 网格交易策略

**原理**: 在价格区间内设置多个买卖点，低买高卖

**网格设置**:
```
价格区间：$90 - $110
网格数量：10
网格大小：$2

网格位:
$90  $92  $94  $96  $98  $100  $102  $104  $106  $108  $110
买   买   买   买   买   中    卖    卖    卖    卖    卖
```

**信号规则**:
| 价格位置 | 信号 | 操作 |
|---------|------|------|
| 触及底部 | STRONG_BUY | 买入至 80% 仓位 |
| 接近买网格 | BUY | 买入 10% 仓位 |
| 中间区域 | HOLD | 持有 |
| 接近卖网格 | SELL | 卖出 10% 仓位 |
| 触及顶部 | STRONG_SELL | 卖出至 20% 仓位 |

---

## 量化进场提示系统 🚨

### 工作流程

```
1. 加载监控列表
   ↓
2. 对每个标的检查:
   - 量化信号 (置信度>60%)
   - 技术信号 (BUY/STRONG_BUY)
   - 风险收益比 (≥1.5)
   - 价格位置 (<30% 分位)
   ↓
3. 所有条件满足 → 生成进场信号
   ↓
4. 推送警报 + 保存历史
```

### 信号报告示例

```
============================================================
🚨 入场信号：AAPL
============================================================
时间：2026-03-25T09:30:00
当前价格：$175.50
信号强度：BUY (置信度:72%)

条件检查:
  ✅ quant_signal
  ✅ tech_signal
  ✅ risk_reward
  ✅ price_position

风险收益比：2.3
价格位置：25.0% (近 60 日)

建议操作:
  仓位：30%
  止损：$166.73 (-5%)
  止盈 1: $184.28 (+5%)
  止盈 2: $193.05 (+10%)
============================================================
```

### 持续监控模式

```bash
# 持续监控监控列表
ta entry --continuous

# 持续监控特定标的 (每 3 分钟)
ta entry BTC ETH --continuous --interval 180

# 使用 A 股数据监控
ta entry --a-share --continuous --interval 300
```

---

## A 股数据支持 🇨🇳

### 数据来源

**新浪财经 API**:
- ✅ 免费实时行情
- ✅ 无需 API Key
- ✅ 覆盖沪深两市
- ⚠️ 仅限境内访问

### 支持的股票

| 市场 | 代码前缀 | 示例 |
|------|---------|------|
| 上交所 | 60xxxx | 600519 (贵州茅台) |
| 深交所 | 00xxxx | 000858 (五粮液) |
| 深交所创业板 | 30xxxx | 300750 (宁德时代) |

### 实时行情数据

```bash
$ ta a-share 600519

📊 600519 - 贵州茅台 实时行情
==================================================
   现价：¥1685.00
   涨跌：+15.50 (+0.93%)
   今开：¥1670.00
   昨收：¥1669.50
   最高：¥1690.00
   最低：¥1665.00
   成交量：12,580 手
   成交额：¥211,234.5 万
   时间：2026-03-25 14:30:00
==================================================
```

### K 线数据

```bash
$ ta a-share 300750 --kline --days 60

📈 300750 K 线数据 (近 60 天)
   共 60 条记录
   最新：2026-03-25 O:185.5 H:190.2 L:184.0 C:188.5
```

### 市场状态

```bash
$ ta a-share --status

📊 A 股市场状态
   交易时间：是
   当前时间：2026-03-25 14:30:00 (北京时间)
   今日 15:00 收盘
```

---

## 综合应用案例 💡

### 案例 1: A 股量化选股

```bash
# 1. 获取 A 股股票列表
ta a-share --list

# 2. 对心仪股票进行量化分析
ta quant 600519 --days 60
ta quant 000858 --days 60
ta quant 300750 --days 60

# 3. 设置进场监控
ta entry --add 600519
ta entry --add 000858
ta entry --add 300750

# 4. 启动持续监控
ta entry --a-share --continuous --interval 300
```

### 案例 2: 多策略组合

```python
from quantitative_strategies import (
    MultiFactorStrategy,
    MeanReversionStrategy,
    MomentumBreakoutStrategy
)

# 1. 多因子选股
mf = MultiFactorStrategy()
stocks = [...]  # 股票池数据
ranked = mf.rank_stocks(stocks)
top_pick = ranked[0]['symbol']

# 2. 均值回归检查
mr = MeanReversionStrategy()
mr_signal = mr.generate_signals(prices, current_price)

# 3. 动量突破检查
mo = MomentumBreakoutStrategy()
mo_signal = mo.check_breakout(prices)

# 4. 综合判断
if (ranked[0]['recommendation'] == 'STRONG_BUY' and
    mr_signal['signal'] == 'STRONG_BUY' and
    mo_signal['signal'] == 'BUY'):
    print("三策略共振，强烈买入!")
```

### 案例 3: 网格交易实战

```python
from quantitative_strategies import GridTradingStrategy

# 设置网格 (基于支撑阻力位)
grid = GridTradingStrategy(
    lower_bound=160,   # 支撑位
    upper_bound=180,   # 阻力位
    grid_num=10        # 10 个网格
)

# 获取交易信号
signal = grid.get_grid_signal(current_price=165)

if signal['signal'] == 'BUY':
    print(f"网格买入信号：{signal['reason']}")
    print(f"建议操作：{signal['suggested_action']}")
```

---

## 注意事项 ⚠️

### A 股数据

1. **交易时间**: 仅在交易日 9:30-11:30, 13:00-15:00 有实时数据
2. **数据延迟**: 非交易时间显示最后收盘价
3. **代码格式**: 支持 6 位代码 (600519) 或带前缀 (sh600519)

### 量化策略

1. **回测必要**: 实盘前务必回测验证
2. **参数优化**: 不同标的需调整参数
3. **风险控制**: 设置止损，不要全仓
4. **多策略验证**: 单一策略可靠性有限

### 进场提示

1. **信号延迟**: 监控间隔 ≥ 60 秒
2. **API 限制**: 注意 Twelve Data 调用次数
3. **历史数据**: 仅保留最近 100 条警报

---

## 下一步

- 📚 查看 [量化成本分析](quantitative-analysis.md) 了解成本因子
- 📊 查看 [技术分析指南](technical-analysis.md) 学习指标
- 🔧 查看 [CLI 参考](CLI.md) 了解所有命令
