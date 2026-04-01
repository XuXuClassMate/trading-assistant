# 📦 npm Installation Guide

**Difficulty**: ⭐⭐ Medium  
**Time**: 10 minutes

---

## ✅ Prerequisites

- Node.js 18+ ([Get Node.js](https://nodejs.org/))
- npm (comes with Node.js)
- API Keys (Twelve Data, Alpha Vantage)

---

## 🚀 Quick Start

### 1. Verify Node.js Version

```bash
node --version
# Should be v18 or higher
```

### 2. Install from npm

```bash
npm install -g @xuxuclassmate/trading-assistant
```

### 3. Verify Installation

```bash
ta --version
# Output: OpenClaw Trading Assistant CLI v1.3.0
```

---

## ⚙️ Configuration

### 1. Create Configuration Directory

```bash
mkdir -p ta-config && cd ta-config
```

### 2. Download Configuration Files

```bash
# Download .env template
curl -O https://raw.githubusercontent.com/XuXuClassMate/trading-assistant/main/.env.example
cp .env.example .env

# Download watchlist template
curl -O https://raw.githubusercontent.com/XuXuClassMate/trading-assistant/main/watchlist.txt.example
cp watchlist.txt.example watchlist.txt
```

### 3. Edit Configuration

```bash
# Edit .env with your API keys
nano .env
```

**Required API Keys**:
```env
TWELVE_DATA_API_KEY=your_key_here
ALPHA_VANTAGE_API_KEY=your_key_here
LANGUAGE=en  # or 'zh' for Chinese
```

---

## 🎯 Usage

### Interactive Mode

```bash
ta
```

### Direct Commands

```bash
# Trading signals
ta sig

# Support/Resistance
ta sr

# Position calculator
ta pos --symbol NVDA --price 175 --capital 10000

# All analysis
ta all
```

---

## 📋 Command Reference

| Command | Shortcut | Description |
|---------|----------|-------------|
| `ta` | - | Start interactive mode |
| `ta sig` | `ta signals` | Generate trading signals |
| `ta sr` | `ta support-resistance` | Analyze support/resistance |
| `ta pos` | `ta position` | Calculate position size |
| `ta alerts` | `ta alert` | Manage price alerts |
| `ta all` | `ta analyze` | Run all analysis |
| `ta v` | `ta version` | Show version |
| `ta h` | `ta help` | Show help |

---

## 🔧 Advanced Usage

### Use in Node.js Projects

```javascript
const { TradingAssistant } = require('@xuxuclassmate/trading-assistant');

const ta = new TradingAssistant({
  twelveDataKey: 'your_key',
  alphaVantageKey: 'your_key'
});

// Get trading signals
const signals = await ta.getSignals('NVDA');
console.log(signals);

// Calculate position
const position = await ta.calculatePosition({
  symbol: 'NVDA',
  price: 175.64,
  capital: 10000,
  risk: 1
});
console.log(position);
```

### Use in TypeScript

```typescript
import { TradingAssistant, Signal } from '@xuxuclassmate/trading-assistant';

const ta = new TradingAssistant({
  twelveDataKey: process.env.TWELVE_DATA_API_KEY,
  alphaVantageKey: process.env.ALPHA_VANTAGE_API_KEY
});

const signals: Signal[] = await ta.getSignals('NVDA');
```

---

## 🔄 Update

```bash
# Check for updates
npm outdated @xuxuclassmate/trading-assistant

# Update to latest version
npm update -g @xuxuclassmate/trading-assistant

# Verify update
ta --version
```

---

## 🗑️ Uninstall

```bash
npm uninstall -g @xuxuclassmate/trading-assistant
```

---

## ❓ Troubleshooting

### Permission Denied (Linux/macOS)

```bash
# Fix npm permissions
mkdir ~/.npm-global
npm config set prefix '~/.npm-global'
echo 'export PATH=~/.npm-global/bin:$PATH' >> ~/.bashrc
source ~/.bashrc

# Then install
npm install -g @xuxuclassmate/trading-assistant
```

### Command Not Found

```bash
# Find npm global bin directory
npm bin -g

# Add to PATH if not already there
export PATH=$(npm bin -g):$PATH
```

### Node Version Too Old

```bash
# Check Node version
node --version

# Update Node.js
# macOS: brew upgrade node
# Ubuntu: curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -
# Windows: Download from nodejs.org
```

---

## 📦 Package Info

- **Package Name**: `@xuxuclassmate/trading-assistant`
- **Registry**: GitHub Packages
- **Version**: 1.1.3
- **License**: MIT

---

## 🔗 Related Links

- [npm Package](https://github.com/XuXuClassMate/trading-assistant/pkgs/npm/trading-assistant)
- [Node.js Documentation](https://nodejs.org/docs/)
- [npm Documentation](https://docs.npmjs.com/)

---

## 📚 Next Steps

- [CLI Documentation](../CLI.md) - Learn all commands
- [JavaScript API](javascript-api.md) - Use in Node.js projects
- [Configuration Guide](configuration.md) - Advanced settings
