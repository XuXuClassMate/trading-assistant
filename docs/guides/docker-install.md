# 🐳 Docker Installation Guide

**Difficulty**: ⭐ Easy  
**Time**: 5 minutes

---

## ✅ Prerequisites

- Docker installed ([Get Docker](https://docs.docker.com/get-docker/))
- API Keys (Twelve Data, Alpha Vantage)

---

## 🚀 Quick Start

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
```

### 4. Run Docker Container

**Interactive Mode**:
```bash
docker run --rm -it \
  -v $(pwd)/.env:/app/.env \
  -v $(pwd)/watchlist.txt:/app/watchlist.txt \
  ghcr.io/xuxuclassmate/trading-assistant:latest
```

**Direct Command**:
```bash
docker run --rm -it \
  -v $(pwd)/.env:/app/.env \
  -v $(pwd)/watchlist.txt:/app/watchlist.txt \
  ghcr.io/xuxuclassmate/trading-assistant:latest \
  ta sig
```

---

## 📋 Available Images

| Registry | Image | Command |
|----------|-------|---------|
| **GitHub Packages** | `ghcr.io/xuxuclassmate/trading-assistant:latest` | Recommended |
| **Docker Hub** | `xuxuclassmate/trading-assistant:latest` | Alternative |

---

## 🎯 Usage Examples

### Interactive CLI

```bash
$ docker run --rm -it \
  -v $(pwd)/.env:/app/.env \
  -v $(pwd)/watchlist.txt:/app/watchlist.txt \
  ghcr.io/xuxuclassmate/trading-assistant:latest

ta> help
ta> sig
ta> pos --symbol NVDA --price 175 --capital 10000
ta> exit
```

### One-Command Analysis

```bash
# All analysis at once
docker run --rm -it \
  -v $(pwd)/.env:/app/.env \
  -v $(pwd)/watchlist.txt:/app/watchlist.txt \
  ghcr.io/xuxuclassmate/trading-assistant:latest \
  ta all
```

### Specific Symbol

```bash
# Signals for NVDA
docker run --rm -it \
  -v $(pwd)/.env:/app/.env \
  -v $(pwd)/watchlist.txt:/app/watchlist.txt \
  ghcr.io/xuxuclassmate/trading-assistant:latest \
  ta sig --symbol NVDA
```

---

## 🔧 Advanced Options

### Run in Background (Detached Mode)

```bash
docker run -d --name trading-assistant \
  -v $(pwd)/.env:/app/.env \
  -v $(pwd)/watchlist.txt:/app/watchlist.txt \
  ghcr.io/xuxuclassmate/trading-assistant:latest
```

### View Logs

```bash
docker logs -f trading-assistant
```

### Stop Container

```bash
docker stop trading-assistant
docker rm trading-assistant
```

### Update to Latest Version

```bash
docker pull ghcr.io/xuxuclassmate/trading-assistant:latest
docker stop trading-assistant
docker rm trading-assistant
# Re-run with same command as above
```

---

## ❓ Troubleshooting

### Permission Denied Error

```bash
# Run with current user
docker run --rm -it \
  -u $(id -u):$(id -g) \
  -v $(pwd)/.env:/app/.env \
  -v $(pwd)/watchlist.txt:/app/watchlist.txt \
  ghcr.io/xuxuclassmate/trading-assistant:latest
```

### API Key Errors

Make sure your `.env` file has valid API keys:
```env
TWELVE_DATA_API_KEY=your_actual_key
ALPHA_VANTAGE_API_KEY=your_actual_key
```

### Volume Mount Issues

Use absolute paths:
```bash
docker run --rm -it \
  -v /absolute/path/to/.env:/app/.env \
  -v /absolute/path/to/watchlist.txt:/app/watchlist.txt \
  ghcr.io/xuxuclassmate/trading-assistant:latest
```

---

## 📚 Next Steps

- [CLI Documentation](../CLI.md) - Learn all commands
- [Configuration Guide](configuration.md) - Advanced settings
- [API Setup](api-setup.md) - Get your API keys

---

## 🔗 Related Links

- [Docker Documentation](https://docs.docker.com/)
- [GitHub Packages](https://github.com/XuXuClassMate/trading-assistant/pkgs/container/trading-assistant)
- [Docker Hub](https://hub.docker.com/r/xuxuclassmate/trading-assistant)
