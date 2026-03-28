# Daily Report System

**Version**: v1.5.0 | **Last Updated**: 2026-03-26

Comprehensive guide to the Trading Assistant's automated daily report system with three-tier analysis levels.

---

## 📊 Overview

The Daily Report System provides automated market analysis at three detail levels, designed for different use cases and time constraints.

### Three Report Levels

| Level | Read Time | Content | Use Case |
|-------|-----------|---------|----------|
| **Small** 📝 | 10 seconds | Key data + market sentiment | Quick daily brief |
| **Medium** 📊 | 1 minute | Technical analysis + strategies | Daily review |
| **Large** 📈 | 5 minutes | Deep analysis + holdings report | Weekend/monthly summary |

---

## 🚀 Quick Start

### Generate Reports Manually

```bash
cd trading-assistant

# Morning brief (Small)
python3 daily_report.py morning small

# Evening standard (Medium)
python3 daily_report.py evening medium

# Evening deep analysis (Large)
python3 daily_report.py evening large
```

### Automated Schedule (Heartbeat)

Add to your `HEARTBEAT.md`:

```markdown
## Trading Daily Reports

### Morning Brief (HKT 09:00 = UTC 01:00)
- Time: Daily UTC 01:00-02:00
- Execute:
  ```bash
  cd ~/skills/trading-assistant && python3 daily_report.py morning small
  ```

### Evening Summary (HKT 17:00 = UTC 09:00)
- Time: Daily UTC 09:00-10:00
- Execute:
  ```bash
  cd ~/skills/trading-assistant && python3 daily_report.py evening medium
  ```

### Deep Analysis (HKT 20:00 = UTC 12:00)
- Time: Daily UTC 12:00-13:00
- Execute:
  ```bash
  cd ~/skills/trading-assistant && python3 daily_report.py evening large
  ```
```

---

## 📝 Report Levels Explained

### Small Report 📝 (10 seconds)

**Purpose**: Quick market snapshot for busy traders

**Content**:
- Market status overview
- Key sentiment indicators
- Expected volatility
- Major support/resistance levels

**Best For**:
- Morning pre-market check
- Quick evening review
- Mobile notifications

**Example Output**:
```
📊 Morning Brief - 2026-03-26

Market Status: OPEN
Sentiment: BULLISH (65%)
Expected Range: +0.5% to +1.2%

Key Levels:
- SPY Resistance: $582.50
- SPY Support: $578.00

Have a great trading day! 🚀
```

---

### Medium Report 📊 (1 minute)

**Purpose**: Standard daily analysis with actionable insights

**Content**:
- All Small report content
- Technical indicator summary (RSI, MACD, BB)
- Trading signals for watchlist stocks
- Entry/exit recommendations
- Risk management notes

**Best For**:
- Daily trading decisions
- Portfolio review
- Strategy adjustment

**Example Output**:
```
📊 Evening Summary - 2026-03-26

Market Performance:
- SPY: +0.85% (Bullish)
- QQQ: +1.23% (Bullish)

Technical Signals:
🟢 AAPL: BUY (RSI: 45, MACD: Bullish)
🟡 NVDA: HOLD (RSI: 68, Near resistance)
🟢 TSLA: STRONG_BUY (Breakout confirmed)

Watchlist Summary:
- 3 Buy signals
- 2 Hold signals
- 0 Sell signals

Key Events Tomorrow:
- Fed speech at 14:00 EST
- Earnings: MSFT (after close)
```

---

### Large Report 📈 (5 minutes)

**Purpose**: Comprehensive analysis for serious traders

**Content**:
- All Medium report content
- Detailed technical analysis (10 indicators)
- Holdings performance breakdown
- Sector analysis
- News sentiment analysis
- Risk assessment
- Next day/week outlook

**Best For**:
- Weekend deep dive
- Monthly portfolio review
- Strategy optimization
- Learning and research

**Example Sections**:
```
📊 Deep Analysis - 2026-03-26

1. Market Overview
   - Major indices performance
   - Volume analysis
   - Breadth indicators

2. Technical Deep Dive
   - RSI analysis across sectors
   - MACD divergence/convergence
   - Bollinger Band positions
   - Moving average alignments

3. Holdings Analysis
   - Individual stock performance
   - Cost basis vs current
   - Unrealized P&L
   - Position sizing review

4. Sector Rotation
   - Strongest sectors
   - Weakest sectors
   - Money flow analysis

5. News Sentiment
   - Positive catalysts
   - Risk factors
   - Earnings surprises

6. Outlook & Strategy
   - Next day expectations
   - Key levels to watch
   - Recommended actions
```

---

## 📁 File Locations

### Generated Reports

```
trading-assistant/reports/
├── 2026-03-26_morning_small.md
├── 2026-03-26_evening_medium.md
└── 2026-03-26_evening_large.md
```

### Sent Reports

```
trading-assistant/sent/
├── 2026-03-26_morning_small.md
└── 2026-03-26_evening_medium.md
```

### Learning Data

```
trading-assistant/learning/
├── predictions_2026-03.json
└── accuracy_stats.json
```

---

## 🔧 Configuration

### Environment Variables

```bash
# API Keys
TWELVE_DATA_API_KEY=your_key
ALPHA_VANTAGE_API_KEY=your_key

# LLM Provider (for analysis generation)
DASHSCOPE_API_KEY=your_key
QWEN_MODEL=qwen3.5-plus

# Notification (Feishu)
FEISHU_APP_ID=your_app_id
FEISHU_APP_SECRET=your_app_secret
FEISHU_WEBHOOK_URL=https://...

# Trading Settings
TRADING_LANG=en  # or zh_CN
DEFAULT_RISK_PROFILE=moderate
```

### Watchlist Configuration

Edit `watchlist.txt`:

```
# US Stocks
AAPL|Apple Inc.
NVDA|NVIDIA Corporation
TSLA|Tesla Inc.
MSFT|Microsoft Corporation

# A-Shares (if applicable)
600519|贵州茅台
000858|五粮液

# Crypto (if applicable)
BTCUSDT|Bitcoin
ETHUSDT|Ethereum
```

---

## 📊 Learning System

### Prediction Tracking

The system automatically:
1. Saves predictions to `learning/predictions_YYYY-MM.json`
2. Validates predictions against actual prices
3. Calculates accuracy statistics
4. Generates weekly/monthly reports

### Accuracy Reports

```bash
# Generate 30-day accuracy report
python3 daily_report.py accuracy 30

# Show learning statistics
python3 daily_report.py stats
```

### Continuous Improvement

The learning system analyzes:
- Signal accuracy (BUY/SELL/HOLD)
- Confidence calibration
- Best/worst performing stocks
- Time-based patterns
- Sector performance

---

## 🎯 Best Practices

### Morning Routine (10-15 min)

1. **Check Small Report** (10 sec)
   - Quick market status
   - Key levels to watch

2. **Review Medium Report** (1 min)
   - Trading signals
   - Entry/exit points

3. **Adjust Watchlist** (5-10 min)
   - Add/remove stocks
   - Update price targets

### Evening Routine (15-30 min)

1. **Review Medium Report** (1 min)
   - Day's performance
   - Signal accuracy

2. **Read Large Report** (5 min, optional)
   - Deep analysis
   - Holdings review

3. **Plan Tomorrow** (5-10 min)
   - Set alerts
   - Prepare watchlist

### Weekly Review (30-60 min, Weekend)

1. **Read Large Reports** from the week
2. **Check Accuracy Statistics**
3. **Adjust Strategy** based on performance
4. **Update Watchlist** for next week

---

## ⚠️ Troubleshooting

### Common Issues

**Issue**: Reports not generating

**Solution**:
```bash
# Check API keys
cat .env | grep API_KEY

# Test data connection
python3 -c "from config import get_api_key; print(get_api_key('TWELVE_DATA'))"

# Check logs
tail -f logs/daily_report.log
```

**Issue**: Feishu notifications not sending

**Solution**:
```bash
# Test Feishu connection
python3 -c "from feishu_utils import test_webhook; test_webhook()"

# Verify webhook URL
cat .env | grep FEISHU_WEBHOOK
```

**Issue**: Slow report generation

**Solution**:
```bash
# Reduce watchlist size
# Enable caching
# Use fewer indicators in config
```

---

## 📚 Related Documentation

- [Getting Started](../index.md) - Installation and setup
- [Technical Analysis](technical-analysis.md) - Indicator details
- [Position Management](position-management.md) - Holdings tracking
- [Risk Management](risk-management.md) - Stop-loss and position sizing
- [API Keys Setup](api-keys.md) - Getting API credentials

---

## 🔗 Resources

- **GitHub**: https://github.com/XuXuClassMate/trading-assistant
- **Issues**: https://github.com/XuXuClassMate/trading-assistant/issues
- **PyPI**: https://pypi.org/project/trading-assistant/

---

**Last Updated**: 2026-03-26 | **Version**: v1.5.0
