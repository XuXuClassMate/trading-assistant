# 🐍 pip Installation Guide

**Difficulty**: ⭐⭐ Medium  
**Time**: 10 minutes

---

## ✅ Prerequisites

- Python 3.11 or higher ([Get Python](https://www.python.org/downloads/))
- pip (Python package manager)
- API Keys (Twelve Data, Alpha Vantage)

---

## 🚀 Quick Start

### 1. Verify Python Version

```bash
python3 --version
# Should be 3.11 or higher
```

### 2. Install from PyPI

```bash
pip install trading-assistant
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
nano .env  # or use your favorite editor
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

### Set Environment Variables

```bash
# Option 1: Export before running
export TWELVE_DATA_API_KEY=your_key
export ALPHA_VANTAGE_API_KEY=your_key
ta

# Option 2: Use .env file (automatic)
cd ta-config
ta
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

## 🔧 Advanced Configuration

### Custom Configuration Path

```bash
export TA_CONFIG_PATH=/path/to/your/config
ta
```

### Debug Mode

```bash
export TA_DEBUG=true
ta
```

### Custom Language

```bash
export LANGUAGE=zh
ta
```

---

## 🔄 Update

```bash
# Check for updates
pip list | grep trading-assistant

# Update to latest version
pip install --upgrade trading-assistant

# Verify update
ta --version
```

---

## 🗑️ Uninstall

```bash
pip uninstall trading-assistant
```

---

## ❓ Troubleshooting

### Python Version Error

```bash
# Check Python version
python3 --version

# If < 3.11, upgrade Python
# macOS: brew install python@3.11
# Ubuntu: sudo apt install python3.11
# Windows: Download from python.org
```

### Permission Denied

```bash
# Install for current user only
pip install --user trading-assistant

# Or use sudo (not recommended)
sudo pip install trading-assistant
```

### Command Not Found

```bash
# Add pip bin directory to PATH
# Find pip path
pip show -f trading-assistant | grep Location

# Add to PATH (example for ~/.bashrc or ~/.zshrc)
export PATH=$PATH:~/.local/bin
source ~/.bashrc  # or source ~/.zshrc
```

### API Rate Limits

If you hit API rate limits:
- Twelve Data: 800 calls/day (free tier)
- Alpha Vantage: 25 calls/day (free tier)

**Solutions**:
1. Upgrade to paid tier
2. Reduce analysis frequency
3. Cache results locally

---

## 📚 Next Steps

- [CLI Documentation](../CLI.md) - Learn all commands
- [Configuration Guide](configuration.md) - Advanced settings
- [API Setup](api-setup.md) - Get your API keys

---

## 🔗 Related Links

- [PyPI Package](https://pypi.org/project/trading-assistant/)
- [Python Documentation](https://docs.python.org/)
- [pip Documentation](https://pip.pypa.io/)
