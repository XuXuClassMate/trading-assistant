---
hide:
  - navigation
  - toc
---

---
title: 首页
---

# 📊 OpenClaw 交易助手

<div class="grid" markdown>

<div class="feature-card" markdown>
### 🎯 智能信号

结合 RSI、MACD 和移动平均线的 AI 驱动交易信号，附带置信度评分。

[了解更多 →](guides/trading-signals.md)
</div>

<div class="feature-card" markdown>
### 📈 技术分析

使用多种成熟算法计算支撑位和阻力位。

[了解更多 →](guides/technical-analysis.md)
</div>

<div class="feature-card" markdown>
### 💰 仓位管理

基于风险的仓位计算器，优化资金配置。

[了解更多 →](guides/position-management.md)
</div>

<div class="feature-card" markdown>
### 🔔 价格提醒

自动监控止盈和止损水平。

[了解更多 →](guides/price-alerts.md)
</div>

</div>

---

## 🚀 快速开始

=== "Docker (推荐)"
    ```bash
    docker pull xuxuclassmate/trading-assistant:latest
    docker run --rm -it \
      -v $(pwd)/.env:/app/.env \
      -v $(pwd)/watchlist.txt:/app/watchlist.txt \
      xuxuclassmate/trading-assistant:latest
    ```
    
    <span class="badge badge-success">5 分钟配置</span>
    <span class="badge badge-info">无需依赖</span>

=== "pip (Python)"
    ```bash
    pip install trading-assistant
    ta
    ```
    
    <span class="badge badge-success">10 分钟配置</span>
    <span class="badge badge-info">Python 3.11+</span>

=== "npm (Node.js)"
    ```bash
    npm install -g @xuxuclassmate/trading-assistant
    ta
    ```
    
    <span class="badge badge-success">10 分钟配置</span>
    <span class="badge badge-info">Node 18+</span>

---

## 📊 实时示例

<div class="command-example" markdown>
```bash
$ ta sig --symbol NVDA

📈 正在为 NVDA 生成信号...

┌─────────────────────────────────────┐
│  NVDA @ $175.64                     │
├─────────────────────────────────────┤
│  RSI (14):       52.34  [中性]      │
│  MACD:           0.1234 [看涨]      │
│  MA (50):        $168.20 [看涨]     │
│  MA (200):       $155.80 [看涨]     │
├─────────────────────────────────────┤
│  综合评分：3/3 [看涨]               │
│  推荐：买入                         │
│  置信度：中等 (67%)                 │
└─────────────────────────────────────┘

✅ 分析完成！
```
</div>

---

## 📈 市场概览

<div class="grid" markdown>

<div class="feature-card" markdown>
#### 🌟 精选股票
- **NVDA** - 看涨 📈
- **AAPL** - 中性 ➡️
- **MSFT** - 看涨 📈
- **TSLA** - 看跌 📉

[查看完整分析 →](guides/getting-started.md)
</div>

<div class="feature-card" markdown>
#### 🔥 热门
1. **NVDA** - AI 芯片需求
2. **AMD** - 数据中心增长
3. **META** - VR 投资
4. **GOOGL** - 云扩展

[了解原因 →](guides/trading-signals.md)
</div>

</div>

---

## 🎓 学习路径

<div class="grid" markdown>

<div markdown>
### 初学者
1. [入门指南](guides/getting-started.md)
2. [安装说明](guides/install-overview.md)
3. [第一次分析](guides/getting-started.md#步骤-4运行第一次分析)
</div>

<div markdown>
### 中级
1. [技术指标](guides/advanced-indicators.md)
2. [风险管理](guides/risk-management.md)
3. [仓位管理](guides/position-management.md)
</div>

<div markdown>
### 高级
1. [量化策略](guides/quant-strategies-a-share.md)
2. [实盘接口](guides/live-trading.md)
3. [性能优化](guides/performance-optimization.md)
</div>

</div>

---

## 📦 安装选项

| 方法 | 命令 | 时间 | 难度 |
|------|------|------|------|
| **Docker** ⭐ | `docker pull xuxuclassmate/trading-assistant:latest` | 5 分钟 | 简单 |
| **pip** | `pip install trading-assistant` | 10 分钟 | 中等 |
| **npm** | `npm install -g @xuxuclassmate/trading-assistant` | 10 分钟 | 中等 |
| **源码** | `git clone + pip install -e .` | 15 分钟 | 高级 |

[→ 完整安装指南](guides/install-overview.md)

---

## 🎯 为什么选择交易助手？

<div class="grid" markdown>

<div class="feature-card" markdown>
### 🤖 AI 驱动
结合多个技术指标与智能评分算法。
</div>

<div class="feature-card" markdown>
### 🌐 多平台
支持 Docker、PyPI、npm - 随时随地使用。
</div>

<div class="feature-card" markdown>
### 🔒 隐私优先
本地运行，数据留在你的机器上。
</div>

<div class="feature-card" markdown>
### 🆓 免费开源
MIT 许可，社区驱动开发。
</div>

</div>

---

## 📊 项目统计

<div class="grid" markdown>

<div class="feature-card" markdown>
### 📦 下载与使用

**最新版本**: v1.3.1 (2026 年 3 月 25 日)

<div class="stat-badges" markdown>

[Docker Hub](https://hub.docker.com/r/xuxuclassmate/trading-assistant){ .badge .badge-success } 🆕 刚刚发布

[PyPI](https://pypi.org/project/trading-assistant/){ .badge .badge-info } ✅ 已发布

[GitHub Releases](https://github.com/XuXuClassMate/trading-assistant/releases){ .badge .badge-primary } ✅ 活跃

</div>

*第一个使用者！随着社区成长，统计数据将在此显示。* 🚀
</div>

<div class="feature-card" markdown>
### ⭐ 社区

<div class="community-stats" markdown>

<div class="stat-item" markdown>
<span class="stat-number">🆕</span>
<span class="stat-label">GitHub Stars</span>
<a href="https://github.com/XuXuClassMate/trading-assistant" class="stat-link">⭐ 成为第一个！</a>
</div>

<div class="stat-item" markdown>
<span class="stat-number">🆕</span>
<span class="stat-label">Forks</span>
<a href="https://github.com/XuXuClassMate/trading-assistant/fork" class="stat-link">🍴 Fork 它！</a>
</div>

<div class="stat-item" markdown>
<span class="stat-number">🆕</span>
<span class="stat-label">Issues</span>
<a href="https://github.com/XuXuClassMate/trading-assistant/issues" class="stat-link">🐛 报告一个！</a>
</div>

</div>

*这个项目刚刚发布！你的 ⭐ 和反馈帮助它成长。* 🌱
</div>

</div>

---

## 🆕 最近更新

<div class="grid" markdown>

<div class="feature-card" markdown>
### v1.3.1 - 作者更新
- ✅ 更新 PyPI 作者信息
- ✅ 邮箱：mail@xuxuclassmate.com
- 📦 所有平台已更新

[发布说明 →](https://github.com/XuXuClassMate/trading-assistant/releases/tag/v1.3.1)
</div>

<div class="feature-card" markdown>
### v1.3.0 - CLI 革命
- 🖥️ 新 `ta` 命令（2 个字母！）
- 🎨 交互模式
- 📚 完整的文档网站

[新功能 →](https://github.com/XuXuClassMate/trading-assistant/releases/tag/v1.3.0)
</div>

</div>

---

## 💬 加入社区

<div class="grid" markdown>

<div markdown>
### 🐙 GitHub
- 报告问题
- 请求功能
- 贡献代码

[贡献 →](https://github.com/XuXuClassMate/trading-assistant)
</div>

<div markdown>
### 💬 讨论
- 提问
- 分享策略
- 帮助他人

[加入讨论 →](https://github.com/XuXuClassMate/trading-assistant/discussions)
</div>

</div>

---

## 📝 许可证

MIT 许可证 - 免费用于个人和商业用途。

[查看许可证 →](https://github.com/XuXuClassMate/trading-assistant/blob/main/LICENSE)

---

<div class="feature-card" style="text-align: center;" markdown>
### 🚀 准备好开始了吗？

[立即开始 →](guides/getting-started.md){ .md-button .md-button--primary }

[查看文档 →](CLI.md){ .md-button }
</div>

---

<div align="center" markdown>
**Made with ❤️ by XuXuClassMate**

[![Version](https://img.shields.io/github/v/release/XuXuClassMate/trading-assistant?label=version)](https://github.com/XuXuClassMate/trading-assistant/releases)
[![License](https://img.shields.io/github/license/XuXuClassMate/trading-assistant)](https://github.com/XuXuClassMate/trading-assistant/blob/main/LICENSE)
[![Docker Pulls](https://img.shields.io/docker/pulls/xuxuclassmate/trading-assistant)](https://hub.docker.com/r/xuxuclassmate/trading-assistant)

</div>
