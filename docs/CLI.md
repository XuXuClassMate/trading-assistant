# 🖥️ CLI Quick Reference / CLI 快速参考

## 🚀 Start / 启动

```bash
# Interactive mode / 交互模式
ta

# Or / 或
ta interactive

# Full name (also works) / 完整名称（也可用）
openclaw-trading-assistant
```

## 📋 Commands / 命令

| Command / 命令 | Shortcut / 快捷 | Description / 描述 |
|---------------|----------------|-------------------|
| `ta` | - | Start interactive mode / 交互模式 |
| `ta interactive` | `interact`, `cli` | Start interactive mode / 交互模式 |
| `ta sr` | `support-resistance` | Analyze support/resistance / 分析支撑阻力位 |
| `ta sig` | `signals` | Generate trading signals / 生成交易信号 |
| `ta pos` | `position`, `calc` | Calculate position size / 计算仓位大小 |
| `ta alerts` | `alert`, `alarm` | Manage price alerts / 管理价格提醒 |
| `ta all` | `full`, `analyze` | Run all analysis / 运行所有分析 |
| `ta v` | `version` | Show version / 显示版本 |
| `ta h` | `help` | Show help / 显示帮助 |

## 💡 Examples / 示例

### Interactive Mode / 交互模式

```bash
$ ta

============================================================
  OpenClaw Trading Assistant CLI
  Version: 1.3.0
============================================================

Welcome to OpenClaw Trading Assistant Interactive CLI
Type 'help' for available commands, 'exit' to quit

ta> help
ta> signals
ta> pos --symbol NVDA --price 175.64 --capital 10000
ta> sr
ta> exit
```

### Direct Commands / 直接命令

```bash
# Support/Resistance / 支撑阻力位
ta sr
ta support-resistance

# Signals / 信号
ta sig
ta sig --symbol NVDA

# Position / 仓位
ta pos --symbol NVDA --price 175.64 --capital 10000
ta pos --symbol AAPL --price 175 --capital 50000 --risk 2

# Alerts / 提醒
ta alerts check
ta alerts list
ta alerts create --symbol NVDA --entry 175 --stop 170 --target 185

# All Analysis / 全部分析
ta all
ta analyze
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
  ta sig
```

## 🎯 Position Calculator / 仓位计算器

```bash
# Basic / 基础
ta pos --symbol NVDA --price 175.64 --capital 10000

# With custom risk / 自定义风险
ta pos --symbol NVDA --price 175.64 --capital 10000 --risk 2
```

## 🔔 Alerts / 提醒

```bash
# Check all / 检查所有
ta alerts check

# List all / 列出所有
ta alerts list

# Create new / 创建新提醒
ta alerts create \
  --symbol NVDA \
  --entry 175 \
  --stop 170 \
  --target 185
```

## 📊 Output Examples / 输出示例

### Signals / 信号
```
$ ta sig

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
$ ta pos --symbol NVDA --price 175.64 --capital 10000

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
ta help
ta h

# In interactive mode / 在交互模式中
ta> help
```

## 🚀 Quick Start / 快速开始

1. **Setup / 设置**
   ```bash
   mkdir -p ta-config && cd ta-config
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
   ta
   ```

---

**Version**: v1.3.0  
**Release**: https://github.com/XuXuClassMate/trading-assistant/releases/tag/v1.3.0  
**Docker**: ghcr.io/xuxuclassmate/trading-assistant:latest
