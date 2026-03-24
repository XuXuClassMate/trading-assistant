# ⚙️ Configuration Guide / 配置指南

**Important**: All configuration is user-defined. Nothing is hardcoded.  
**重要**: 所有配置由用户自行定义，无硬编码。

---

## 📋 Quick Start / 快速开始

### Step 1: Copy Configuration Files / 复制配置文件

```bash
# Environment variables / 环境变量
cp .env.example .env

# Watchlist / 自选股列表
cp watchlist.txt.example watchlist.txt
```

### Step 2: Edit Configuration / 编辑配置

```bash
# Edit .env with your API Keys and preferences
# 编辑 .env 填入 API Keys 和偏好设置
nano .env

# Edit watchlist.txt with your stocks
# 编辑 watchlist.txt 填入你的股票
nano watchlist.txt
```

---

## 🔑 Required Configuration / 必填配置

### API Keys (Mandatory / 必须)

**Get your API Keys / 获取 API Keys**:
- Twelve Data: https://twelvedata.com/pricing (Free 800 calls/day)
- Alpha Vantage: https://www.alphavantage.co/support/#api-key (Free 25 calls/day)

**Edit `.env`**:
```bash
TWELVE_DATA_API_KEY=your_twelve_data_key_here
ALPHA_VANTAGE_API_KEY=your_alpha_vantage_key_here
```

---

## 📝 Stock Watchlist (Mandatory / 必须)

**Edit `watchlist.txt`** - Add your stocks (one per line):

```
# US Stocks / 美股
NVDA
AAPL
MSFT
GOOGL
TSLA

# A-Share Stocks / A 股 (with suffix)
600519.SH
000858.SZ
300750.SZ

# HK Stocks / 港股 (with suffix)
0700.HK
9988.HK
```

**Supported Formats / 支持格式**:
- **US Stocks**: `NVDA`, `AAPL`, `MSFT` (no suffix)
- **A-Share**: `600519.SH`, `000858.SZ` (`.SH` or `.SZ` suffix)
- **HK Stocks**: `0700.HK`, `9988.HK` (`.HK` suffix)

---

## 🔔 Notification Configuration (Optional / 可选)

**Leave all fields empty to disable notifications.**  
**留空所有字段以禁用推送通知。**

### Feishu / 飞书 (Optional)

```bash
FEISHU_APP_ID=
FEISHU_APP_SECRET=
FEISHU_CHAT_ID=
```

**How to get Feishu credentials**:
1. Create a Feishu app at https://open.feishu.cn
2. Get App ID and App Secret
3. Add bot to your chat and get Chat ID

### DingTalk / 钉钉 (Optional)

```bash
DINGTALK_APP_KEY=
DINGTALK_APP_SECRET=
DINGTALK_AGENT_ID=
DINGTALK_CHAT_ID=
```

### Email / 邮件 (Optional)

```bash
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SMTP_USER=your_email@gmail.com
SMTP_PASSWORD=your_app_password
NOTIFICATION_EMAIL=recipient@example.com
```

---

## 🎯 Trading Preferences (Optional / 可选)

### Risk Profile / 风险偏好

```bash
# Options: conservative / moderate / aggressive
# 选项：保守型 / 稳健型 / 进取型
RISK_PROFILE=moderate
```

**Risk Levels**:
- `conservative`: 1% risk per trade, suitable for beginners
- `moderate`: 2% risk per trade, balanced approach
- `aggressive`: 3% risk per trade, higher risk/reward

### Default Capital / 默认总资金

```bash
# Default capital in USD
# 默认总资金 (美元)
DEFAULT_CAPITAL=100000
```

### Language / 语言

```bash
# Options: en (English) or zh_CN (中文)
# 选项：en (英文) 或 zh_CN (中文)
TRADING_ASSISTANT_LANG=en
```

---

## 📁 Configuration Files

### `.env` - Environment Variables

Contains all your API Keys and settings. **Never commit this file to Git.**

包含所有 API Keys 和设置。**切勿提交到 Git。**

### `watchlist.txt` - Stock Watchlist

Your personal stock watchlist. **Never commit this file to Git.**

你的个人股票列表。**切勿提交到 Git。**

### `.env.example` - Environment Template

Template file with all available options. Safe to commit.

包含所有可用选项的模板文件。可以安全提交。

### `watchlist.txt.example` - Watchlist Template

Template with example stocks. Safe to commit.

包含示例股票的模板。可以安全提交。

---

## ✅ Verification / 验证配置

After configuration, test your setup:

配置完成后，测试你的设置：

```bash
# Test API connection / 测试 API 连接
python3 support_resistance.py

# Test with your watchlist / 测试自选股
python3 -c "
from config import get_watchlist
stocks = get_watchlist()
print(f'Watchlist: {stocks}')
"
```

---

## 🐛 Troubleshooting / 故障排除

### Issue: "API key not configured"

**Solution**: Check `.env` file exists and contains valid API Keys
```bash
cat .env | grep API_KEY
```

### Issue: "Watchlist is empty"

**Solution**: Create `watchlist.txt` and add at least one stock symbol
```bash
echo "NVDA" > watchlist.txt
```

### Issue: "Notifications not working"

**Solution**: Leave notification fields empty in `.env` to disable, or fill in correct credentials

---

## 📚 Additional Resources

- [README_CLAWHUB.md](README_CLAWHUB.md) - Main documentation
- [docs/I18N.md](docs/I18N.md) - Internationalization guide
- [.env.example](.env.example) - Configuration template
- [watchlist.txt.example](watchlist.txt.example) - Watchlist template

---

## 🔒 Security Best Practices

1. **Never commit `.env` or `watchlist.txt`** to Git
2. **Use environment variables** for sensitive data
3. **Rotate API Keys** periodically
4. **Use app-specific passwords** for email notifications
5. **Limit notification access** to necessary chats only

---

**Made with ❤️ for customizable trading**

*Last Updated*: 2026-03-24  
*Version*: v1.0.0
