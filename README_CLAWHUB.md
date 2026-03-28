# 🚀 OpenClaw Trading Assistant

**Version**: v1.0.0  
**Author**: OpenClaw Community  
**License**: MIT  
**Languages**:  English,  简体中文  
**Category**: Trading / Finance / Technical Analysis

---

## 📖 Introduction / 简介

**English**:  
OpenClaw Trading Assistant is a complete trading decision support system that provides technical analysis, trading signals, position management, and risk monitoring.

**中文**:  
OpenClaw 交易助手是一个功能完整的交易辅助决策系统，提供技术分析、买卖信号、仓位管理和风险监控等功能。

---

## ✨ Features / 功能特性

### 1. Support & Resistance Levels / 支撑/阻力位计算

**English**:
- Automatic calculation of key price levels
- Multiple algorithms: Previous High/Low, Moving Averages, Fibonacci, Pivot Points
- Strength indicator (strong/medium/weak)

**中文**:
- 自动计算关键价格位
- 多种算法：前高/前低、均线、斐波那契、枢轴点
- 强度指示 (强/中/弱)

**Example**:
```
NVDA Current Price: $175.64
Resistance: $177.26 (+0.9%), $180.00 (+2.5%)
Support: $175.00 (-0.4%), $171.72 (-2.2%)
```

---

### 2. Trading Signals / 买卖信号

**English**:
- Multi-indicator analysis (RSI, MACD, Moving Averages)
- Combined signal scoring
- Recommendations: Strong Buy / Buy / Hold / Sell / Strong Sell

**中文**:
- 多指标分析 (RSI, MACD, 均线)
- 综合信号评分
- 操作建议：强买/买入/观望/卖出/强卖

**Example**:
```
RSI: 52.34 [Neutral]
MACD: 0.1234 [Bullish]
Moving Averages: [Bullish]
Combined: Bullish (score: 3)
Recommendation: BUY (Confidence: Medium)
```

---

### 3. Position Calculator / 仓位计算器

**English**:
- Risk-based position sizing
- Risk profiles: Conservative / Moderate / Aggressive
- Confidence adjustment
- Stop-loss calculation
- Portfolio allocation

**中文**:
- 基于风险的仓位计算
- 风险偏好：保守型/稳健型/进取型
- 置信度调整
- 止损位计算
- 投资组合配置

**Example**:
```
Total Capital: $100,000
Entry Price: $175.64
Stop Loss: $165.00
Risk Profile: Moderate

Position: 562 shares ($98,710, 98.7%)
Risk: $5,964 (5.96%)
Risk/Reward: 1:2.0
```

---

## 🌍 Internationalization / 国际化

**Default Language**: English (`en`)

**Switch Language / 切换语言**:

```bash
# Method 1: Environment Variable / 环境变量
export TRADING_ASSISTANT_LANG=zh_CN

# Method 2: In Code / 代码中
from i18n import set_language
set_language("zh_CN")

# Method 3: Config File / 配置文件
# Add to config.json: {"language": "zh_CN"}
```

**Supported Languages / 支持语言**:
-  English (`en`) - Default
-  简体中文 (`zh_CN`)

See [docs/I18N.md](docs/I18N.md) for details.

---

## 🛠️ Installation / 安装

### Prerequisites / 前置要求

- Python 3.11+
- Twelve Data API Key (Free 800 calls/day)
- Alpha Vantage API Key (Free 25 calls/day)

### Quick Start / 快速开始

```bash
# 1. Clone repository / 克隆仓库
git clone https://github.com/XuXuClassMate/trading-assistant.git
cd trading-assistant

# 2. Install dependencies / 安装依赖
pip install -r requirements.txt

# 3. Configure API Keys / 配置 API Keys
cp .env.example .env
# Edit .env with your API Keys / 编辑 .env 填入 API Keys

# 4. Configure Watchlist / 配置自选股
cp watchlist.txt.example watchlist.txt
# Edit watchlist.txt with your stocks / 编辑 watchlist.txt 填入你的股票

# 5. (Optional) Configure Notifications / (可选) 配置推送通知
# Edit .env and fill in your notification credentials
# 编辑 .env 填入推送通知配置 (留空则禁用)

# 6. Test installation / 测试安装
python3 support_resistance.py
python3 trading_signals.py
python3 position_calculator.py
```

---

## 📖 Usage / 使用

### Basic Usage / 基础用法

#### 1. Support & Resistance / 支撑阻力位

```python
from support_resistance import calculate_support_resistance

result = calculate_support_resistance("NVDA")
```

#### 2. Trading Signals / 交易信号

```python
from trading_signals import generate_trading_signal

result = generate_trading_signal("AAPL")
```

#### 3. Position Calculation / 仓位计算

```python
from position_calculator import calculate_position_size

result = calculate_position_size(
    total_capital=100000,
    entry_price=175.64,
    stop_loss_price=165.00,
    risk_profile="moderate",
    confidence="medium"
)
```

### Advanced Usage / 高级用法

#### Portfolio Allocation / 投资组合配置

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

## ⚙️ Configuration / 配置

### Step 1: API Keys (Required / 必填)

```bash
# Copy the example environment file
cp .env.example .env

# Edit .env and add your API Keys
# 编辑 .env 并填入你的 API Keys
```

**Get API Keys / 获取 API Key**:
- Twelve Data: https://twelvedata.com/pricing (Free 800 calls/day)
- Alpha Vantage: https://www.alphavantage.co/support/#api-key (Free 25 calls/day)

---

### Step 2: Notification Configuration (Optional / 可选)

**Leave all notification fields empty to disable notifications.**
**留空所有通知配置项以禁用推送。**

#### Feishu / 飞书 (Optional)
```bash
FEISHU_APP_ID=
FEISHU_APP_SECRET=
FEISHU_CHAT_ID=
```

#### DingTalk / 钉钉 (Optional)
```bash
DINGTALK_APP_KEY=
DINGTALK_APP_SECRET=
DINGTALK_AGENT_ID=
DINGTALK_CHAT_ID=
```

#### Email / 邮件 (Optional)
```bash
SMTP_HOST=
SMTP_PORT=
SMTP_USER=
SMTP_PASSWORD=
NOTIFICATION_EMAIL=
```

---

### Step 3: Watchlist Configuration (Required / 必填)

**Copy the example watchlist file:**
```bash
cp watchlist.txt.example watchlist.txt
```

**Edit `watchlist.txt` and add your stocks (one per line):**
```
# US Stocks / 美股
NVDA
AAPL
MSFT
TSLA

# A-Share Stocks / A 股
600519.SH
000858.SZ

# HK Stocks / 港股
0700.HK
9988.HK
```

**Supported Formats / 支持格式**:
- US Stocks: `NVDA`, `AAPL`, `MSFT`
- A-Share: `600519.SH`, `000858.SZ`, `300750.SZ`
- HK Stocks: `0700.HK`, `9988.HK`, `1024.HK`

---

### Step 4: Trading Preferences (Optional / 可选)

```bash
# Risk Profile: conservative / moderate / aggressive
# 风险偏好：保守型 / 稳健型 / 进取型
RISK_PROFILE=moderate

# Default Capital ($)
# 默认总资金 (美元)
DEFAULT_CAPITAL=100000

# Language: en (English) or zh_CN (中文)
TRADING_ASSISTANT_LANG=en
```

---

## 📁 Project Structure / 项目结构

```
trading-assistant/
├── config.py                    # Configuration / 配置管理
├── i18n.py                      # Internationalization / 国际化
├── support_resistance.py        # Support/Resistance / 支撑阻力位
├── trading_signals.py           # Trading Signals / 买卖信号
├── position_calculator.py       # Position Calculator / 仓位计算
├── locales/
│   ├── en.json                  # English translations
│   └── zh_CN.json               # Chinese translations
├── docs/
│   └── I18N.md                  # i18n documentation
├── requirements.txt             # Dependencies
├── .env.example                 # Environment template
├── watchlist.txt.example        # Watchlist template
├── LICENSE                      # MIT License
└── README_CLAWHUB.md            # This file

# User Configuration (not included in repo)
.env                             # Your API Keys & settings
watchlist.txt                    # Your stock watchlist
```

---

## 🧪 Testing / 测试

```bash
# Test all modules / 测试所有模块
python3 support_resistance.py
python3 trading_signals.py
python3 position_calculator.py

# Run unit tests / 运行单元测试
python3 -m pytest tests/
```

---

## ⚠️ Disclaimer / 免责声明

**English**:  
This software is for educational and research purposes only. It does not constitute investment advice. Trading involves substantial risk. Past performance does not guarantee future results. Users should make independent decisions and bear their own risks. The developers are not liable for any investment losses.

**中文**:  
本软件仅供学习和研究使用，不构成投资建议。市场有风险，投资需谨慎。过往表现不代表未来结果。请独立判断，自负盈亏。开发者不承担任何投资损失责任。

---

## 🤝 Contributing / 贡献

Contributions are welcome! Please feel free to submit issues or pull requests.

欢迎贡献！请随时提交 issue 或 pull request。

---

## 📚 Documentation / 文档

- [Internationalization Guide](docs/I18N.md) - Multi-language support
- [API Reference](docs/API.md) - Function documentation
- [Examples](examples/) - Usage examples

---

## 🙏 Acknowledgments / 致谢

Thanks to these open-source projects:
- **OpenClaw** - AI assistant framework
- **Twelve Data** - Financial market data API
- **Alpha Vantage** - Stock/Forex data API
- **ClawHub** - OpenClaw skills community

---

## 📬 Contact / 联系方式

- **GitHub**: https://github.com/XuXuClassMate/trading-assistant
- **Issues**: https://github.com/XuXuClassMate/trading-assistant/issues
- **ClawHub**: https://clawhub.com

---

**Made with ❤️ by OpenClaw Community**

*Last Updated*: 2026-03-24  
*Version*: v1.3.0
