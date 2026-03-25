# 📚 OpenClaw Trading Assistant Documentation

**Version**: v1.3.0  
**Last Updated**: 2026-03-25

---

## 🎯 Quick Start / 快速开始

Choose your installation method / 选择安装方式:

| Method | Command | Difficulty |
|--------|---------|------------|
| **Docker** (Recommended) | `docker run -it ghcr.io/xuxuclassmate/trading-assistant:latest` | ⭐ Easy |
| **pip** | `pip install openclaw-trading-assistant` | ⭐⭐ Medium |
| **npm** | `npm install @xuxuclassmate/openclaw-trading-assistant` | ⭐⭐ Medium |
| **Source** | `git clone + pip install -r requirements.txt` | ⭐⭐⭐ Advanced |

---

## 📖 Installation Guides / 安装指南

### 🐳 Docker Installation
**Best for**: Quick start, no Python setup needed  
**适合**: 快速开始，无需 Python 环境

[→ Read Docker Guide →](./guides/docker-install.md)

### 🐍 pip Installation
**Best for**: Python developers, integration with other Python tools  
**适合**: Python 开发者，与其他 Python 工具集成

[→ Read pip Guide →](./guides/pip-install.md)

### 📦 npm Installation
**Best for**: Node.js projects, OpenClaw skill integration  
**适合**: Node.js 项目，OpenClaw skill 集成

[→ Read npm Guide →](./guides/npm-install.md)

### 🔧 Source Installation
**Best for**: Developers, contributors, custom modifications  
**适合**: 开发者，贡献者，自定义修改

[→ Read Source Guide →](./guides/source-install.md)

---

## 🖥️ CLI Usage / 命令行使用

### Quick Reference / 快速参考

```bash
# Start interactive mode / 交互模式
ta

# Direct commands / 直接命令
ta sig          # Trading signals
ta sr           # Support/Resistance
ta pos          # Position calculator
ta alerts       # Price alerts
ta all          # Run all analysis
```

[→ Full CLI Documentation →](./CLI.md)

---

## 📊 Features / 功能

- 📈 **Support & Resistance** - Multiple algorithms
- 🎯 **Trading Signals** - RSI, MACD, Moving Averages
- 💰 **Position Calculator** - Risk-based sizing
- 🔔 **Price Alerts** - Stop loss & take profit
- 🌐 **Multi-language** - English & Chinese

---

## 🔗 Links

- **GitHub**: https://github.com/XuXuClassMate/trading-assistant
- **Docker (GitHub)**: https://github.com/XuXuClassMate/trading-assistant/pkgs/container/trading-assistant
- **Docker (Docker Hub)**: https://hub.docker.com/r/xuxuclassmate/trading-assistant
- **npm**: https://github.com/XuXuClassMate/trading-assistant/pkgs/npm/openclaw-trading-assistant
- **PyPI**: https://pypi.org/project/openclaw-trading-assistant/

---

## 📝 License

MIT License - See [LICENSE](../LICENSE) for details
