# 🚀 OpenClaw Trading Assistant

<div align="center">

**Version / 版本**: v1.0.0  
**Author / 作者**: OpenClaw Community  
**License / 许可证**: MIT  
**Languages / 语言**: 🇺🇸 English | 🇨🇳 简体中文

[Features](#-features--功能特性) • [Installation](#-installation--安装) • [Usage](#-usage--使用) • [Configuration](#-configuration--配置) • [Documentation](#-documentation--文档)

---

**🇺🇸 English** | [🇨🇳 中文](#-简介)

</div>

---

## 📖 Introduction / 简介

<details>
<summary><b>🇺🇸 Click to read in English</b></summary>

**OpenClaw Trading Assistant** is a complete trading decision support system that provides technical analysis, trading signals, position management, and risk monitoring.

### ✨ Key Features

- 📊 **Support & Resistance Levels** - Automatic calculation with multiple algorithms
- 📈 **Trading Signals** - Multi-indicator analysis (RSI, MACD, Moving Averages)
- 💰 **Position Calculator** - Risk-based position sizing
- ⚠️ **Risk Management** - Stop-loss, take-profit, portfolio allocation
- 🌍 **Multi-language** - English & Chinese support
- 🔔 **Notifications** - Feishu, DingTalk, Email (configurable)

### 🎯 Perfect For

- Stock/ETF investors
- Technical analysis enthusiasts
- Quantitative trading beginners
- OpenClaw users

</details>

<details>
<summary><b>🇨🇳 点击查看中文</b></summary>

**OpenClaw 交易助手** 是一个功能完整的交易辅助决策系统，提供技术分析、买卖信号、仓位管理和风险监控等功能。

### ✨ 核心功能

- 📊 **支撑/阻力位计算** - 多种算法自动计算关键价格位
- 📈 **买卖信号生成** - 多指标分析 (RSI, MACD, 均线)
- 💰 **智能仓位计算** - 基于风险承受能力的仓位管理
- ⚠️ **风险控制** - 止盈止损、投资组合配置
- 🌍 **多语言支持** - 英文和中文
- 🔔 **推送通知** - 飞书、钉钉、邮件 (可配置)

### 🎯 适合人群

- 股票/ETF 投资者
- 技术分析爱好者
- 量化交易初学者
- OpenClaw 用户

</details>

---

## ✨ Features / 功能特性

### 1. Support & Resistance Levels / 支撑/阻力位计算

<details>
<summary><b>🇺🇸 English</b></summary>

- Automatic calculation of key price levels
- Multiple algorithms: Previous High/Low, Moving Averages, Fibonacci, Pivot Points
- Strength indicator (strong/medium/weak)

**Example Output**:
```
NVDA Current Price: $175.64
Resistance: $177.26 (+0.9%), $180.00 (+2.5%)
Support: $175.00 (-0.4%), $171.72 (-2.2%)
```

</details>

<details>
<summary><b>🇨🇳 中文</b></summary>

- 自动计算关键价格位
- 多种算法：前高/前低、均线、斐波那契、枢轴点
- 强度指示 (强/中/弱)

**输出示例**:
```
NVDA 当前价格：$175.64
阻力位：$177.26 (+0.9%), $180.00 (+2.5%)
支撑位：$175.00 (-0.4%), $171.72 (-2.2%)
```

</details>

---

### 2. Trading Signals / 买卖信号

<details>
<summary><b>🇺🇸 English</b></summary>

- Multi-indicator analysis (RSI, MACD, Moving Averages)
- Combined signal scoring
- Recommendations: Strong Buy / Buy / Hold / Sell / Strong Sell

**Example Output**:
```
RSI: 52.34 [Neutral]
MACD: 0.1234 [Bullish]
Moving Averages: [Bullish]
Combined: Bullish (score: 3)
Recommendation: BUY (Confidence: Medium)
```

</details>

<details>
<summary><b>🇨🇳 中文</b></summary>

- 多指标分析 (RSI, MACD, 均线)
- 综合信号评分
- 操作建议：强买/买入/观望/卖出/强卖

**输出示例**:
```
RSI: 52.34 [中性]
MACD: 0.1234 [看涨]
均线：[看涨]
综合：看涨 (score: 3)
建议：买入 (置信度：中)
```

</details>

---

### 3. Position Calculator / 仓位计算器

<details>
<summary><b>🇺🇸 English</b></summary>

- Risk-based position sizing
- Risk profiles: Conservative / Moderate / Aggressive
- Confidence adjustment
- Stop-loss calculation
- Portfolio allocation

**Example Output**:
```
Total Capital: $100,000
Entry Price: $175.64
Stop Loss: $165.00
Risk Profile: Moderate

Position: 562 shares ($98,710, 98.7%)
Risk: $5,964 (5.96%)
Risk/Reward: 1:2.0
```

</details>

<details>
<summary><b>🇨🇳 中文</b></summary>

- 基于风险的仓位计算
- 风险偏好：保守型/稳健型/进取型
- 置信度调整
- 止损位计算
- 投资组合配置

**输出示例**:
```
总资金：$100,000
入场价：$175.64
止损价：$165.00
风险偏好：稳健型

仓位：562 股 ($98,710, 98.7%)
风险：$5,964 (5.96%)
风险收益比：1:2.0
```

</details>

---

## 🛠️ Installation / 安装

### Prerequisites / 前置要求

- Python 3.11+
- Twelve Data API Key ([Get Free](https://twelvedata.com/pricing) - 800 calls/day)
- Alpha Vantage API Key ([Get Free](https://www.alphavantage.co/support/#api-key) - 25 calls/day)

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
# Edit watchlist.txt with your stocks / 编辑 watchlist.txt 填入股票

# 5. (Optional) Configure Notifications / (可选) 配置推送通知
# Edit .env and fill in notification credentials (leave empty to disable)
# 编辑 .env 填入推送通知配置 (留空则禁用)

# 6. Test installation / 测试安装
python3 support_resistance.py
python3 trading_signals.py
python3 position_calculator.py
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
- 🇺🇸 English (`en`) - Default
- 🇨🇳 简体中文 (`zh_CN`)

📚 [See I18N Documentation](docs/I18N.md)

---

## ⚙️ Configuration / 配置

### Required / 必填

1. **API Keys** - Twelve Data & Alpha Vantage
2. **Watchlist** - Your stock list

### Optional / 可选

1. **Notifications** - Feishu, DingTalk, Email (leave empty to disable)
2. **Risk Profile** - Conservative/Moderate/Aggressive
3. **Language** - English/Chinese

📚 [See Full Configuration Guide](docs/CONFIGURATION.md)

---

## 📖 Usage / 使用

### Basic Usage / 基础用法

```python
# Support & Resistance / 支撑阻力位
from support_resistance import calculate_support_resistance
result = calculate_support_resistance("NVDA")

# Trading Signals / 交易信号
from trading_signals import generate_trading_signal
result = generate_trading_signal("AAPL")

# Position Calculation / 仓位计算
from position_calculator import calculate_position_size
result = calculate_position_size(
    total_capital=100000,
    entry_price=175.64,
    stop_loss_price=165.00,
    risk_profile="moderate"
)
```

📚 [See Full Usage Guide](README_CLAWHUB.md)

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
│   ├── I18N.md                  # i18n documentation
│   └── CONFIGURATION.md         # Configuration guide
├── requirements.txt             # Dependencies
├── .env.example                 # Environment template
├── watchlist.txt.example        # Watchlist template
├── LICENSE                      # MIT License
└── README.md                    # This file
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

## 📊 Version History / 版本历史

### v1.0.0 (2026-03-24) - Initial Release

**🇺🇸 Features**:
- ✅ Support & Resistance calculation
- ✅ Trading signal generation (RSI, MACD, MA)
- ✅ Position size calculator
- ✅ Multi-language support (EN/ZH)
- ✅ Configurable notifications
- ✅ Portfolio allocation

**🇨🇳 功能**:
- ✅ 支撑/阻力位计算
- ✅ 买卖信号生成 (RSI, MACD, 均线)
- ✅ 仓位计算器
- ✅ 多语言支持 (英文/中文)
- ✅ 可配置推送通知
- ✅ 投资组合配置

📚 [See Full Release Notes](CHANGELOG.md)

---

## ⚠️ Disclaimer / 免责声明

<details>
<summary><b>🇺🇸 English</b></summary>

This software is for **educational and research purposes only**. It does not constitute investment advice.

- Trading involves substantial risk
- Past performance does not guarantee future results
- Users should make independent decisions and bear their own risks
- The developers are not liable for any investment losses

</details>

<details>
<summary><b>🇨🇳 中文</b></summary>

本软件仅供**学习和研究使用**，不构成投资建议。

- 市场有风险，投资需谨慎
- 过往表现不代表未来结果
- 请独立判断，自负盈亏
- 开发者不承担任何投资损失责任

</details>

---

## 🤝 Contributing / 贡献

**🇺🇸**: Contributions are welcome! Please feel free to submit issues or pull requests.  
**🇨🇳**: 欢迎贡献！请随时提交 issue 或 pull request。

---

## 📚 Documentation / 文档

- [📖 README_CLAWHUB.md](README_CLAWHUB.md) - Detailed guide (bilingual)
- [🌍 docs/I18N.md](docs/I18N.md) - Internationalization guide
- [⚙️ docs/CONFIGURATION.md](docs/CONFIGURATION.md) - Configuration guide
- [📝 CHANGELOG.md](CHANGELOG.md) - Version history
- [❓ FAQ.md](FAQ.md) - Frequently asked questions

---

## 🙏 Acknowledgments / 致谢

**🇺🇸**: Thanks to these open-source projects:  
**🇨🇳**: 感谢以下开源项目：

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

<div align="center">

**Made with ❤️ by OpenClaw Community**

[📖 Documentation](#-documentation--文档) • [🐛 Report Issue](https://github.com/XuXuClassMate/trading-assistant/issues) • [⭐ Star Project](https://github.com/XuXuClassMate/trading-assistant)

*Last Updated*: 2026-03-24  
*Version*: v1.0.0

</div>
