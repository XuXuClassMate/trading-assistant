# 🐳 Docker Usage Guide / Docker 使用指南

## Quick Start / 快速开始

### 1. Pull Image / 拉取镜像

**From GitHub Container Registry**:
```bash
docker pull ghcr.io/xuxuclassmate/trading-assistant:latest
```

**From Docker Hub**:
```bash
docker pull xuxuclassmate/trading-assistant:latest
```

### 2. Configure / 配置

```bash
# Create configuration directory
mkdir -p trading-assistant-config
cd trading-assistant-config

# Download example environment file
curl -O https://raw.githubusercontent.com/XuXuClassMate/trading-assistant/main/.env.example
cp .env.example .env

# Download example watchlist
curl -O https://raw.githubusercontent.com/XuXuClassMate/trading-assistant/main/watchlist.txt.example
cp watchlist.txt.example watchlist.txt

# Edit configuration files
nano .env        # Add your API keys
nano watchlist.txt  # Add your stocks
```

### 3. Run / 运行

```bash
# Show help
docker run --rm -it \
  -v $(pwd)/.env:/app/.env \
  -v $(pwd)/watchlist.txt:/app/watchlist.txt \
  ghcr.io/xuxuclassmate/trading-assistant:latest \
  --help

# Analyze support/resistance levels
docker run --rm -it \
  -v $(pwd)/.env:/app/.env \
  -v $(pwd)/watchlist.txt:/app/watchlist.txt \
  ghcr.io/xuxuclassmate/trading-assistant:latest \
  support-resistance

# Generate trading signals
docker run --rm -it \
  -v $(pwd)/.env:/app/.env \
  -v $(pwd)/watchlist.txt:/app/watchlist.txt \
  ghcr.io/xuxuclassmate/trading-assistant:latest \
  signals

# Calculate position size
docker run --rm -it \
  -v $(pwd)/.env:/app/.env \
  -v $(pwd)/watchlist.txt:/app/watchlist.txt \
  ghcr.io/xuxuclassmate/trading-assistant:latest \
  position --symbol NVDA --price 175.64 --capital 10000
```

---

## Available Commands / 可用命令

| Command / 命令 | Description / 描述 |
|---------------|-------------------|
| `--help` | Show help message / 显示帮助信息 |
| `support-resistance` | Analyze support/resistance levels / 分析支撑阻力位 |
| `signals` | Generate trading signals / 生成交易信号 |
| `position` | Calculate position size / 计算仓位大小 |
| `alerts` | Manage price alerts / 管理价格提醒 |
| `all` | Run all analysis / 运行所有分析 |

---

## Environment Variables / 环境变量

Create a `.env` file with the following variables:

```bash
# API Keys / API 密钥
TWELVE_DATA_API_KEY=your_twelve_data_key
ALPHA_VANTAGE_API_KEY=your_alpha_vantage_key

# Language / 语言
TRADING_ASSISTANT_LANG=en  # or zh_CN

# Notification Settings (Optional) / 通知设置（可选）
FEISHU_WEBHOOK=
DINGTALK_WEBHOOK=
EMAIL_SMTP_SERVER=
EMAIL_SMTP_PORT=
EMAIL_FROM=
EMAIL_TO=
EMAIL_PASSWORD=
```

---

## Volume Mounts / 卷挂载

| Container Path / 容器路径 | Host Path / 主机路径 | Purpose / 用途 |
|--------------------------|---------------------|---------------|
| `/app/.env` | `./.env` | API keys and config / API 密钥和配置 |
| `/app/watchlist.txt` | `./watchlist.txt` | Stock watchlist / 股票自选列表 |
| `/app/logs/` | `./logs/` | Log files / 日志文件 |

---

## Examples / 示例

### 1. Daily Analysis / 每日分析

```bash
docker run --rm -it \
  -v $(pwd)/.env:/app/.env \
  -v $(pwd)/watchlist.txt:/app/watchlist.txt \
  -v $(pwd)/logs:/app/logs \
  ghcr.io/xuxuclassmate/trading-assistant:latest \
  all
```

### 2. Single Stock Analysis / 单只股票分析

```bash
docker run --rm -it \
  -v $(pwd)/.env:/app/.env \
  ghcr.io/xuxuclassmate/trading-assistant:latest \
  signals --symbol NVDA
```

### 3. Create Price Alert / 创建价格提醒

```bash
docker run --rm -it \
  -v $(pwd)/.env:/app/.env \
  -v $(pwd)/alerts.json:/app/alerts.json \
  ghcr.io/xuxuclassmate/trading-assistant:latest \
  alerts create \
  --symbol NVDA \
  --entry-price 175.00 \
  --stop-loss 170.00 \
  --take-profit 185.00
```

### 4. Check Alerts / 检查提醒

```bash
docker run --rm -it \
  -v $(pwd)/.env:/app/.env \
  -v $(pwd)/alerts.json:/app/alerts.json \
  ghcr.io/xuxuclassmate/trading-assistant:latest \
  alerts check
```

---

## Image Tags / 镜像标签

| Tag / 标签 | Description / 描述 |
|-----------|-------------------|
| `latest` | Latest stable version / 最新稳定版 |
| `1.2.0` | Specific version / 特定版本 |
| `1.2` | Latest patch of minor version / 小版本最新补丁 |
| `1` | Latest minor of major version / 主版本最新小版本 |

---

## Troubleshooting / 故障排除

### Issue: "Permission denied" when mounting volumes

**Solution**: Ensure the `.env` and `watchlist.txt` files have proper permissions:
```bash
chmod 644 .env watchlist.txt
```

### Issue: "API key not found"

**Solution**: Verify the `.env` file is correctly mounted:
```bash
docker run --rm -it \
  -v $(pwd)/.env:/app/.env \
  ghcr.io/xuxuclassmate/trading-assistant:latest \
  cat /app/.env
```

### Issue: "Command not found"

**Solution**: Use the correct command from the available commands list above.

---

## Building Locally / 本地构建

```bash
# Build the image
docker build -t trading-assistant:local .

# Test the image
docker run --rm -it \
  -v $(pwd)/.env:/app/.env \
  -v $(pwd)/watchlist.txt:/app/watchlist.txt \
  trading-assistant:local \
  --help
```

---

## Security Best Practices / 安全最佳实践

1. **Never commit `.env` to Git** - Add to `.gitignore`
2. **Use Docker secrets** for sensitive data in production
3. **Run as non-root user** (future improvement)
4. **Regularly update** to latest security patches

---

## License / 许可证

MIT License - See [LICENSE](../LICENSE) for details.
