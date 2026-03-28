# 📚 Installation Overview

**Choose your installation method** / **选择安装方式**

---

## 🎯 Quick Comparison

| Method | Difficulty | Time | Best For |
|--------|------------|------|----------|
| [🐳 Docker](docker-install.md) | ⭐ Easy | 5 min | Quick start, no setup |
| [🐍 pip](pip-install.md) | ⭐⭐ Medium | 10 min | Python developers |
| [📦 npm](npm-install.md) | ⭐⭐ Medium | 10 min | Node.js projects |
| [🔧 Source](source-install.md) | ⭐⭐⭐ Advanced | 15 min | Developers, contributors |

---

## 🚀 Recommended Paths

### For Most Users → Docker

**Why**: No Python/Node.js setup, works everywhere

```bash
docker run --rm -it \
  -v $(pwd)/.env:/app/.env \
  ghcr.io/xuxuclassmate/trading-assistant:latest
```

[→ Docker Guide](docker-install.md)

---

### For Python Developers → pip

**Why**: Native Python integration, easy to extend

```bash
pip install openclaw-trading-assistant
```

[→ pip Guide](pip-install.md)

---

### For Node.js Developers → npm

**Why**: Use in JavaScript/TypeScript projects

```bash
npm install -g @xuxuclassmate/openclaw-trading-assistant
```

[→ npm Guide](npm-install.md)

---

### For Contributors → Source

**Why**: Full access to code, make modifications

```bash
git clone https://github.com/XuXuClassMate/trading-assistant.git
cd trading-assistant
pip install -e .
```

[→ Source Guide](source-install.md)

---

## 📋 Prerequisites

### API Keys Required

All methods require these free API keys:

1. **Twelve Data** - 800 calls/day free
   - Get: https://twelvedata.com/pricing
   
2. **Alpha Vantage** - 25 calls/day free
   - Get: https://www.alphavantage.co/support/#api-key

[→ API Setup Guide](api-keys.md)

---

## 🎯 Next Steps

After installation:

1. [Configure API Keys](api-keys.md)
2. [Setup Watchlist](watchlist-setup.md)
3. [Learn CLI Commands](../CLI.md)
4. [First Analysis](../guides/getting-started.md)

---

## ❓ Need Help?

- [FAQ](../faq.md) - Common questions
- [GitHub Issues](https://github.com/XuXuClassMate/trading-assistant/issues) - Report bugs
- [Discussions](https://github.com/XuXuClassMate/trading-assistant/discussions) - Ask questions
