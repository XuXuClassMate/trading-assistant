# 🖥️ CLI Quick Reference / CLI 快速参考

## 🚀 Start / 启动

```bash
# Interactive mode / 交互模式
openclaw-trading-assistant

# Or / 或
openclaw-trading-assistant interactive
```

## 📋 Commands / 命令

| Command / 命令 | Shortcut / 快捷 | Description / 描述 |
|---------------|----------------|-------------------|
| `interactive` | `interact`, `cli` | Start interactive mode / 交互模式 |
| `support-resistance` | `sr` | Analyze support/resistance / 分析支撑阻力位 |
| `signals` | `sig` | Generate trading signals / 生成交易信号 |
| `position` | `pos`, `calc` | Calculate position size / 计算仓位大小 |
| `alerts` | `alert`, `alarm` | Manage price alerts / 管理价格提醒 |
| `all` | `full`, `analyze` | Run all analysis / 运行所有分析 |
| `version` | `v` | Show version / 显示版本 |
| `help` | `h` | Show help / 显示帮助 |

## 💡 Examples / 示例

### Interactive Mode / 交互模式

```bash
$ openclaw-trading-assistant

============================================================
  OpenClaw Trading Assistant CLI
  Version: 1.3.0
============================================================

Welcome to OpenClaw Trading Assistant Interactive CLI
Type 'help' for available commands, 'exit' to quit

trading-assistant> help
trading-assistant> signals
trading-assistant> position --symbol NVDA --price 175.64 --capital 10000
trading-assistant> sr
trading-assistant> exit
```

### Direct Commands / 直接命令

```bash
# Support/Resistance / 支撑阻力位
openclaw-trading-assistant support-resistance
openclaw-trading-assistant sr

# Signals / 信号
openclaw-trading-assistant signals
openclaw-trading-assistant sig --symbol NVDA

# Position / 仓位
openclaw-trading-assistant position --symbol NVDA --price 175.64 --capital 10000
openclaw-trading-assistant pos --symbol AAPL --price 175 --capital 50000 --risk 2

# Alerts / 提醒
openclaw-trading-assistant alerts check
openclaw-trading-assistant alerts list
openclaw-trading-assistant alerts create --symbol NVDA --entry 175 --stop 170 --target 185

# All Analysis / 全部分析
openclaw-trading-assistant all
openclaw-trading-assistant analyze
```

## 🐳 Docker Usage / Docker 使用

```bash
# Interactive / 交互模式
docker run --rm -it \
  -v $(pwd)/.env:/app/.env \
  -v $(pwd)/watchlist.txt:/app/watchlist.txt \
  ghcr.io/xuxuclassmate/trading-assistant:latest

# Direct Command / 直接命令
docker run --rm -it \
  -v $(pwd)/.env:/app/.env \
  -v $(pwd)/watchlist.txt:/app/watchlist.txt \
  ghcr.io/xuxuclassmate/trading-assistant:latest \
  signals
```

## 🎯 Position Calculator / 仓位计算器

```bash
# Basic / 基础
openclaw-trading-assistant position --symbol NVDA --price 175.64 --capital 10000

# With custom risk / 自定义风险
openclaw-trading-assistant position --symbol NVDA --price 175.64 --capital 10000 --risk 2
```

## 🔔 Alerts / 提醒

```bash
# Check all / 检查所有
openclaw-trading-assistant alerts check

# List all / 列出所有
openclaw-trading-assistant alerts list

# Create new / 创建新提醒
openclaw-trading-assistant alerts create \
  --symbol NVDA \
  --entry 175 \
  --stop 170 \
  --target 185
```

## 📊 Output Examples / 输出示例

### Signals / 信号
```
📈 Generating signals...

NVDA:
  RSI: 52.34 [Neutral]
  MACD: 0.1234 [Bullish]
  Moving Averages: [Bullish]
  Combined: Bullish (score: 3)
  Recommendation: BUY (Confidence: Medium)

✅ Done!
```

### Position / 仓位
```
💰 Calculating position...

Symbol: NVDA
Entry Price: $175.64
Total Capital: $10000.00
Position Size: 56 shares
Position Value: $9835.84
Risk Amount: $100.00

✅ Done!
```

## 🆘 Help / 帮助

```bash
# Show help / 显示帮助
openclaw-trading-assistant help
openclaw-trading-assistant h

# In interactive mode / 在交互模式中
trading-assistant> help
```

## 🚀 Quick Start / 快速开始

1. **Setup / 设置**
   ```bash
   mkdir -p trading-assistant-config
   cd trading-assistant-config
   curl -O https://raw.githubusercontent.com/XuXuClassMate/trading-assistant/main/.env.example
   curl -O https://raw.githubusercontent.com/XuXuClassMate/trading-assistant/main/watchlist.txt.example
   cp .env.example .env
   cp watchlist.txt.example watchlist.txt
   # Edit .env with your API keys
   ```

2. **Run / 运行**
   ```bash
   # Docker
   docker run --rm -it \
     -v $(pwd)/.env:/app/.env \
     -v $(pwd)/watchlist.txt:/app/watchlist.txt \
     ghcr.io/xuxuclassmate/trading-assistant:latest
   
   # Or pip (after PyPI token)
   pip install openclaw-trading-assistant
   openclaw-trading-assistant
   ```

---

**Version**: v1.3.0  
**Release**: https://github.com/XuXuClassMate/trading-assistant/releases/tag/v1.3.0  
**Docker**: ghcr.io/xuxuclassmate/trading-assistant:latest
