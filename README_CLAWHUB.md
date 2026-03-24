# 🚀 OpenClaw Trading Assistant

**版本**: v1.0.0
**作者**: OpenClaw Community
**许可证**: MIT
**分类**: 交易/金融/数据分析

---

## 📖 简介

OpenClaw Trading Assistant 是一个功能完整的交易辅助决策系统，为投资者提供技术分析、买卖信号、仓位管理和风险监控等功能。

**核心特性**:
- 📊 支撑/阻力位自动计算
- 📈 多指标买卖信号生成
- 💰 智能仓位计算器
- ⚠️ 止盈止损提醒
- 🔔 实时市场监控
- 📱 飞书/钉钉推送集成

---

## ✨ 功能亮点

### 1. 支撑/阻力位计算

基于多种算法自动计算关键价格位：
- 前高/前低法
- 移动平均线 (20/50/200 日)
- 斐波那契回撤
- 枢轴点 (Pivot Points)
- 心理价位

**输出示例**:
```
NVDA 当前价：$175.64
阻力位：$177.26 (+0.9%), $180.00 (+2.5%)
支撑位：$175.00 (-0.4%), $171.72 (-2.2%)
```

### 2. 买卖信号生成

综合多个技术指标生成操作建议：
- RSI 超买/超卖
- MACD 金叉/死叉
- 均线交叉
- 综合信号 (强买/买/观望/卖/强卖)

**输出示例**:
```
RSI: 52.34 [中性]
MACD: 0.1234 [看涨]
均线：[看涨]
综合建议：买入 (置信度：中)
```

### 3. 智能仓位计算

根据风险承受能力和信号置信度自动计算：
- 风险偏好：保守/稳健/进取
- 置信度调整：高/中/低
- 止损位自动计算
- 投资组合配置优化

**输出示例**:
```
总资金：$100,000
入场价：$175.64
止损价：$165.00
建议仓位：562 股 ($98,710, 98.7%)
风险金额：$5,964 (5.96%)
```

---

## 🛠️ 安装

### 前置要求

- Python 3.11+
- OpenClaw v1.0+
- Twelve Data API Key (免费 800 次/天)
- Alpha Vantage API Key (免费 25 次/天)

### 快速安装

```bash
# 1. 克隆或下载技能包
git clone https://github.com/your-repo/trading-assistant.git
cd trading-assistant

# 2. 安装依赖
pip install -r requirements.txt

# 3. 配置 API Keys
cp .env.example .env
# 编辑 .env 填入你的 API Keys

# 4. 测试安装
python3 support_resistance.py
python3 trading_signals.py
python3 position_calculator.py
```

---

## 📖 使用指南

### 基础用法

#### 1. 计算支撑/阻力位

```python
from support_resistance import calculate_support_resistance, print_support_resistance

# 计算 NVDA 的支撑/阻力位
result = calculate_support_resistance("NVDA")

# 打印结果
print_support_resistance(result)
```

#### 2. 生成买卖信号

```python
from trading_signals import generate_trading_signal, print_trading_signal

# 生成 AAPL 的买卖信号
result = generate_trading_signal("AAPL")

# 打印结果
print_trading_signal(result)
```

#### 3. 计算仓位

```python
from position_calculator import calculate_position_size, print_position_result

# 计算仓位
result = calculate_position_size(
    total_capital=100000,      # 总资金 $100,000
    entry_price=175.64,        # 入场价
    stop_loss_price=165.00,    # 止损价
    risk_profile="moderate",   # 稳健型
    confidence="medium"        # 中置信度
)

# 打印结果
print_position_result(result)
```

### 高级用法

#### 投资组合配置

```python
from position_calculator import calculate_portfolio_allocation

positions = [
    {"symbol": "NVDA", "entry_price": 175.64, "confidence": "medium"},
    {"symbol": "AAPL", "entry_price": 251.49, "confidence": "high"},
    {"symbol": "SPY", "entry_price": 580.00, "confidence": "medium"}
]

portfolio = calculate_portfolio_allocation(
    total_capital=100000,
    positions=positions,
    risk_profile="moderate"
)
```

---

## ⚙️ 配置

### 环境变量 (.env)

```bash
# Twelve Data API (免费 800 次/天)
TWELVE_DATA_API_KEY=your_api_key_here

# Alpha Vantage API (免费 25 次/天)
ALPHA_VANTAGE_API_KEY=your_api_key_here

# 飞书推送 (可选)
FEISHU_APP_ID=your_app_id
FEISHU_APP_SECRET=your_app_secret
FEISHU_CHAT_ID=your_chat_id
```

### 配置文件 (config.json)

```json
{
  "risk_profile": "moderate",
  "watchlist": ["NVDA", "AAPL", "SPY", "QQQ"],
  "technical_analysis": {
    "support_resistance": {
      "lookback_days": 60,
      "min_touches": 2
    },
    "trading_signals": {
      "rsi_period": 14,
      "rsi_oversold": 30,
      "rsi_overbought": 70
    },
    "position_sizing": {
      "default_risk_pct": 2.0,
      "max_position_pct": 20.0
    }
  }
}
```

---

## 📊 API 参考

### 支撑/阻力位模块

```python
calculate_support_resistance(symbol: str, days: int = 60) -> dict
```

**返回**:
```json
{
  "symbol": "NVDA",
  "current_price": 175.64,
  "resistance_levels": [
    {"price": 180.0, "strength": "strong", "type": "previous_high"}
  ],
  "support_levels": [
    {"price": 165.0, "strength": "strong", "type": "previous_low"}
  ]
}
```

### 买卖信号模块

```python
generate_trading_signal(symbol: str) -> dict
```

**返回**:
```json
{
  "symbol": "NVDA",
  "recommendation": "buy",
  "confidence": "medium",
  "indicators": {
    "rsi": {"value": 52.34, "signal": "neutral"},
    "macd": {"value": 0.1234, "signal": "bullish"}
  }
}
```

### 仓位计算模块

```python
calculate_position_size(
    total_capital: float,
    entry_price: float,
    stop_loss_price: float,
    risk_profile: str,
    confidence: str
) -> dict
```

**返回**:
```json
{
  "shares": 562,
  "position_value": 98710,
  "position_pct": 98.7,
  "risk_amount": 5964,
  "risk_pct": 5.96
}
```

---

## 🧪 测试

### 运行单元测试

```bash
# 支撑/阻力位测试
python3 support_resistance.py

# 买卖信号测试
python3 trading_signals.py

# 仓位计算测试
python3 position_calculator.py

# 全部测试
python3 -m pytest tests/
```

### 测试覆盖率

目标：>80%

```bash
pytest --cov=trading_assistant tests/
```

---

## 📝 示例项目

### 每日交易报告

```python
#!/usr/bin/env python3
"""生成每日交易报告"""

from support_resistance import calculate_support_resistance
from trading_signals import generate_trading_signal
from position_calculator import calculate_position_size

symbols = ["NVDA", "AAPL", "SPY"]

for symbol in symbols:
    print(f"\n{'='*60}")
    print(f"📈 {symbol}")
    print(f"{'='*60}")
    
    # 支撑/阻力位
    sr = calculate_support_resistance(symbol)
    
    # 买卖信号
    signal = generate_trading_signal(symbol)
    
    # 仓位建议 (假设有信号)
    if signal["recommendation"] in ["buy", "strong_buy"]:
        position = calculate_position_size(
            total_capital=100000,
            entry_price=signal["current_price"],
            stop_loss_price=sr["support_levels"][0]["price"],
            risk_profile="moderate",
            confidence=signal["confidence"]
        )
```

---

## ⚠️ 免责声明

**重要提示**: 本软件仅供学习和研究使用，不构成投资建议。

- 市场有风险，投资需谨慎
- 过往表现不代表未来结果
- 请独立判断，自负盈亏
- 开发者不承担任何投资损失责任

---

## 🤝 贡献

欢迎贡献代码、报告 Bug 或提出新功能建议！

### 贡献指南

1. Fork 本项目
2. 创建功能分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启 Pull Request

### 开发环境

```bash
# 克隆项目
git clone https://github.com/your-repo/trading-assistant.git

# 安装开发依赖
pip install -r requirements-dev.txt

# 运行测试
pytest tests/
```

---

## 📚 文档

- [项目计划](PROJECT_PLAN.md)
- [使用指南](docs/USAGE.md)
- [API 参考](docs/API.md)
- [常见问题](docs/FAQ.md)

---

## 🙏 致谢

感谢以下开源项目：

- **OpenClaw** - AI 助手框架
- **Twelve Data** - 金融市场数据 API
- **Alpha Vantage** - 股票/外汇数据 API
- **ClawHub** - OpenClaw 技能社区

---

## 📬 联系方式

- **项目主页**: https://clawhub.com/trading-assistant
- **问题反馈**: https://github.com/your-repo/trading-assistant/issues
- **社区讨论**: https://discord.gg/clawd

---

**Made with ❤️ by OpenClaw Community**

*最后更新*: 2026-03-24
*版本*: v1.0.0
