# 🚀 OpenClaw 交易助手

<div align="center">

**版本**: v1.1.0  
**作者**: OpenClaw Community  
**许可证**: MIT

[功能特性](#-功能特性) • [安装](#-安装) • [使用](#-使用) • [配置](#-配置) • [文档](#-文档)

---

### 🌐 语言 / Language

**[切换到英文 →](README_en.md)**

---

</div>

---

## 📖 简介

**OpenClaw 交易助手** 是一个功能完整的交易辅助决策系统，提供技术分析、买卖信号、仓位管理和风险监控等功能。

### ✨ 核心功能

- 📊 **支撑/阻力位计算** - 多种算法自动计算关键价格位
- 📈 **买卖信号生成** - 多指标分析 (RSI, MACD, 均线)
- 💰 **智能仓位计算** - 基于风险承受能力的仓位管理
- 🎯 **止盈止损提醒** - 价格监控和触发检测
- ⚠️ **风险控制** - 风险收益比、潜在盈亏计算
- 🔔 **推送通知** - 飞书、钉钉、邮件 (可配置)

### 🎯 适合人群

- 股票/ETF 投资者
- 技术分析爱好者
- 量化交易初学者
- OpenClaw 用户

---

## ✨ 功能特性

### 1. 支撑/阻力位计算

- 自动计算关键价格位
- 多种算法：前高/前低、均线、斐波那契、枢轴点
- 强度指示 (强/中/弱)

**输出示例**:
```
NVDA 当前价格：$175.64
阻力位：$177.26 (+0.9%), $180.00 (+2.5%)
支撑位：$175.00 (-0.4%), $171.72 (-2.2%)
```

---

### 2. 买卖信号

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

---

### 3. 仓位计算器

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

---

## 🛠️ 安装

### 前置要求

- Python 3.11+
- Twelve Data API Key ([免费获取](https://twelvedata.com/pricing) - 800 次/天)
- Alpha Vantage API Key ([免费获取](https://www.alphavantage.co/support/#api-key) - 25 次/天)

### 快速开始

```bash
# 1. 克隆仓库
git clone https://github.com/XuXuClassMate/trading-assistant.git
cd trading-assistant

# 2. 安装依赖
pip install -r requirements.txt

# 3. 配置 API Keys
cp .env.example .env
# 编辑 .env 填入 API Keys

# 4. 配置自选股
cp watchlist.txt.example watchlist.txt
# 编辑 watchlist.txt 填入股票

# 5. (可选) 配置推送通知
# 编辑 .env 填入推送通知配置 (留空则禁用)

# 6. 测试安装
python3 support_resistance.py
python3 trading_signals.py
python3 position_calculator.py
```

---

## 🌍 国际化

**默认语言**: 简体中文 (`zh_CN`)

**切换语言**:

```bash
# 方式 1: 环境变量
export TRADING_ASSISTANT_LANG=en

# 方式 2: 代码中
from i18n import set_language
set_language("en")

# 方式 3: 配置文件
# 添加到 config.json: {"language": "en"}
```

**支持语言**:
- 简体中文 (`zh_CN`) - 默认
- 英文 (`en`)

📚 [查看国际化文档](docs/I18N.md)

---

## ⚙️ 配置

### 必填

1. **API Keys** - Twelve Data 和 Alpha Vantage
2. **自选股** - 你的股票列表

### 可选

1. **推送通知** - 飞书、钉钉、邮件 (留空禁用)
2. **风险偏好** - 保守型/稳健型/进取型
3. **语言** - 中文/英文

📚 [查看完整配置指南](docs/CONFIGURATION.md)

---

## 📖 使用

### 基础用法

```python
# 支撑/阻力位
from support_resistance import calculate_support_resistance
result = calculate_support_resistance("NVDA")

# 买卖信号
from trading_signals import generate_trading_signal
result = generate_trading_signal("AAPL")

# 仓位计算
from position_calculator import calculate_position_size
result = calculate_position_size(
    total_capital=100000,
    entry_price=175.64,
    stop_loss_price=165.00,
    risk_profile="moderate"
)
```

📚 [查看完整使用指南](README_CLAWHUB.md)

---

## 📁 项目结构

```
trading-assistant/
├── config.py                    # 配置管理
├── i18n.py                      # 国际化
├── support_resistance.py        # 支撑/阻力位
├── trading_signals.py           # 买卖信号
├── position_calculator.py       # 仓位计算
├── locales/
│   ├── en.json                  # 英文翻译
│   └── zh_CN.json               # 中文翻译
├── docs/
│   ├── I18N.md                  # 国际化文档
│   └── CONFIGURATION.md         # 配置指南
├── requirements.txt             # 依赖
├── .env.example                 # 环境模板
├── watchlist.txt.example        # 自选股模板
├── LICENSE                      # MIT 许可证
└── README_zh.md                 # 本文件 (中文)
```

---

## 🧪 测试

```bash
# 测试所有模块
python3 support_resistance.py
python3 trading_signals.py
python3 position_calculator.py

# 运行单元测试
python3 -m pytest tests/
```

---

## 📊 版本历史

### v1.0.0 (2026-03-24) - 初始版本

**功能**:
- ✅ 支撑/阻力位计算
- ✅ 买卖信号生成 (RSI, MACD, 均线)
- ✅ 仓位计算器
- ✅ 多语言支持 (中文/英文)
- ✅ 可配置推送通知
- ✅ 投资组合配置

📚 [查看完整发布说明](CHANGELOG.md)

---

## ⚠️ 免责声明

本软件仅供**学习和研究使用**，不构成投资建议。

- 市场有风险，投资需谨慎
- 过往表现不代表未来结果
- 请独立判断，自负盈亏
- 开发者不承担任何投资损失责任

---

## 🤝 贡献

欢迎贡献！请随时提交 issue 或 pull request。

---

## 📚 文档

- [📖 README_CLAWHUB.md](README_CLAWHUB.md) - 详细指南
- [🌍 docs/I18N.md](docs/I18N.md) - 国际化指南
- [⚙️ docs/CONFIGURATION.md](docs/CONFIGURATION.md) - 配置指南
- [📝 CHANGELOG.md](CHANGELOG.md) - 版本历史
- [❓ FAQ.md](FAQ.md) - 常见问题

---

## 🙏 致谢

感谢以下开源项目：

- **OpenClaw** - AI 助手框架
- **Twelve Data** - 金融市场数据 API
- **Alpha Vantage** - 股票/外汇数据 API
- **ClawHub** - OpenClaw 技能社区

---

## 📬 联系方式

- **GitHub**: https://github.com/XuXuClassMate/trading-assistant
- **Issues**: https://github.com/XuXuClassMate/trading-assistant/issues
- **ClawHub**: https://clawhub.com

---

<div align="center">

**Made with ❤️ by OpenClaw Community**

[📖 文档](#-文档) • [🐛 报告问题](https://github.com/XuXuClassMate/trading-assistant/issues) • [⭐ 收藏项目](https://github.com/XuXuClassMate/trading-assistant)

*最后更新*: 2026-03-24  
*版本*: v1.0.0

</div>
