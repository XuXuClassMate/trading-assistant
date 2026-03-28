---
hide:
  - navigation
  - toc
---

# 📊 OpenClaw Trading Assistant

<div class="grid" markdown>

<div class="feature-card" markdown>
### 🎯 Smart Signals

AI-powered trading signals combining RSI, MACD, and Moving Averages with confidence scoring.

[Learn more →](guides/trading-signals.md)
</div>

<div class="feature-card" markdown>
### 📈 Technical Analysis

Advanced support & resistance calculations using multiple proven algorithms.

[Learn more →](guides/technical-analysis.md)
</div>

<div class="feature-card" markdown>
### 💰 Position Sizing

Risk-based position calculator to optimize your capital allocation.

[Learn more →](guides/position-management.md)
</div>

<div class="feature-card" markdown>
### 🔔 Price Alerts

Automated monitoring for stop-loss and take-profit levels.

[Learn more →](guides/price-alerts.md)
</div>

</div>

---

## 🚀 Quick Start

=== "Docker (Recommended)"
    ```bash
    docker pull xuxuclassmate/trading-assistant:latest
    docker run --rm -it \
      -v $(pwd)/.env:/app/.env \
      -v $(pwd)/watchlist.txt:/app/watchlist.txt \
      xuxuclassmate/trading-assistant:latest
    ```
    
    <span class="badge badge-success">5 min setup</span>
    <span class="badge badge-info">No dependencies</span>

=== "pip (Python)"
    ```bash
    pip install openclaw-trading-assistant
    ta
    ```
    
    <span class="badge badge-success">10 min setup</span>
    <span class="badge badge-info">Python 3.11+</span>

=== "npm (Node.js)"
    ```bash
    npm install -g @xuxuclassmate/openclaw-trading-assistant
    ta
    ```
    
    <span class="badge badge-success">10 min setup</span>
    <span class="badge badge-info">Node 18+</span>

---

## 📊 Live Example

<div class="command-example" markdown>
```bash
$ ta sig --symbol NVDA

📈 Generating signals for NVDA...

┌─────────────────────────────────────┐
│  NVDA @ $175.64                     │
├─────────────────────────────────────┤
│  RSI (14):       52.34  [Neutral]   │
│  MACD:           0.1234 [Bullish]   │
│  MA (50):        $168.20 [Bullish]  │
│  MA (200):       $155.80 [Bullish]  │
├─────────────────────────────────────┤
│  Combined Score: 3/3 [Bullish]      │
│  Recommendation: BUY                │
│  Confidence:     Medium (67%)       │
└─────────────────────────────────────┘

✅ Analysis complete!
```
</div>

---

## 📈 Market Overview

<div class="grid" markdown>

<div class="feature-card" markdown>
#### 🌟 Featured Stocks
- **NVDA** - Bullish 📈
- **AAPL** - Neutral ➡️
- **MSFT** - Bullish 📈
- **TSLA** - Bearish 📉

[View Full Analysis →](guides/getting-started.md)
</div>

<div class="feature-card" markdown>
#### 🔥 Trending
1. **NVDA** - AI chip demand
2. **AMD** - Data center growth
3. **META** - VR investments
4. **GOOGL** - Cloud expansion

[See Why →](guides/trading-signals.md)
</div>

</div>

---

## 🎓 Learning Path

<div class="grid" markdown>

<div markdown>
### Beginner
1. [Getting Started](guides/getting-started.md)
2. [Installation](guides/install-overview.md)
3. [First Analysis](guides/getting-started.md#step-4-run-your-first-analysis)
</div>

<div markdown>
### Intermediate
1. [Advanced Indicators](guides/advanced-indicators.md)
2. [Risk Management](guides/risk-management.md)
3. [Position Sizing](guides/position-management.md)
</div>

<div markdown>
### Advanced
1. [Quant Strategies](guides/quant-strategies-a-share.md)
2. [Live Trading](guides/live-trading.md)
3. [Performance](guides/performance-optimization.md)
</div>

</div>

---

## 📦 Installation Options

| Method | Command | Time | Difficulty |
|--------|---------|------|------------|
| **Docker** ⭐ | `docker pull xuxuclassmate/trading-assistant:latest` | 5 min | Easy |
| **pip** | `pip install openclaw-trading-assistant` | 10 min | Medium |
| **npm** | `npm install -g @xuxuclassmate/openclaw-trading-assistant` | 10 min | Medium |
| **Source** | `git clone + pip install -e .` | 15 min | Advanced |

[→ Complete Installation Guide](guides/install-overview.md)

---

## 🎯 Why Trading Assistant?

<div class="grid" markdown>

<div class="feature-card" markdown>
### 🤖 AI-Powered
Combines multiple technical indicators with smart scoring algorithms.
</div>

<div class="feature-card" markdown>
### 🌐 Multi-Platform
Available on Docker, PyPI, npm - use it anywhere.
</div>

<div class="feature-card" markdown>
### 🔒 Privacy First
Runs locally, your data stays on your machine.
</div>

<div class="feature-card" markdown>
### 🆓 Free & Open Source
MIT licensed, community-driven development.
</div>

</div>

---

## 📊 Project Stats

<div class="grid" markdown>

<div class="feature-card" markdown>
### 📦 Downloads & Usage

**Latest Version**: v1.3.2 (March 25, 2026)

<div class="stat-badges" markdown>

[Docker Hub](https://hub.docker.com/r/xuxuclassmate/trading-assistant){ .badge .badge-success } 🆕 Just Launched

[PyPI](https://pypi.org/project/openclaw-trading-assistant/){ .badge .badge-info } ✅ Published

[GitHub Releases](https://github.com/XuXuClassMate/trading-assistant/releases){ .badge .badge-primary } ✅ Active

</div>

*Be the first to use it! Stats will appear here as the community grows.* 🚀
</div>

<div class="feature-card" markdown>
### ⭐ Community

<div class="community-stats" markdown>

<div class="stat-item" markdown>
<span class="stat-number">🆕</span>
<span class="stat-label">GitHub Stars</span>
<a href="https://github.com/XuXuClassMate/trading-assistant" class="stat-link">⭐ Be the first!</a>
</div>

<div class="stat-item" markdown>
<span class="stat-number">🆕</span>
<span class="stat-label">Forks</span>
<a href="https://github.com/XuXuClassMate/trading-assistant/fork" class="stat-link">🍴 Fork it!</a>
</div>

<div class="stat-item" markdown>
<span class="stat-number">🆕</span>
<span class="stat-label">Issues</span>
<a href="https://github.com/XuXuClassMate/trading-assistant/issues" class="stat-link">🐛 Report one!</a>
</div>

</div>

*This project just launched! Your star ⭐ and feedback help it grow.* 🌱
</div>

</div>

---

## 🆕 Latest Updates

<div class="grid" markdown>

<div class="feature-card" markdown>
### v1.3.2 - Author Update
- ✅ Updated PyPI author info
- ✅ Email: mail@xuxuclassmate.com
- 📦 All platforms updated

[Release Notes →](https://github.com/XuXuClassMate/trading-assistant/releases/tag/v1.3.2)
</div>

<div class="feature-card" markdown>
### v1.3.0 - CLI Revolution
- 🖥️ New `ta` command (2 letters!)
- 🎨 Interactive mode
- 📚 Complete documentation website

[What's New →](https://github.com/XuXuClassMate/trading-assistant/releases/tag/v1.3.0)
</div>

</div>

---

## 💬 Join the Community

<div class="grid" markdown>

<div markdown>
### 🐙 GitHub
- Report issues
- Request features
- Contribute code

[Contribute →](https://github.com/XuXuClassMate/trading-assistant)
</div>

<div markdown>
### 💬 Discussions
- Ask questions
- Share strategies
- Help others

[Join Discussion →](https://github.com/XuXuClassMate/trading-assistant/discussions)
</div>

</div>

---

## 📝 License

MIT License - Free for personal and commercial use.

[View License →](https://github.com/XuXuClassMate/trading-assistant/blob/main/LICENSE)

---

<div class="feature-card" style="text-align: center;" markdown>
### 🚀 Ready to Start?

[Get Started Now →](guides/getting-started.md){ .md-button .md-button--primary }

[View Documentation →](CLI.md){ .md-button }
</div>

---

<div align="center" markdown>
**Made with ❤️ by XuXuClassMate**

[![Version](https://img.shields.io/github/v/release/XuXuClassMate/trading-assistant?label=version)](https://github.com/XuXuClassMate/trading-assistant/releases)
[![License](https://img.shields.io/github/license/XuXuClassMate/trading-assistant)](https://github.com/XuXuClassMate/trading-assistant/blob/main/LICENSE)
[![Docker Pulls](https://img.shields.io/docker/pulls/xuxuclassmate/trading-assistant)](https://hub.docker.com/r/xuxuclassmate/trading-assistant)

</div>
