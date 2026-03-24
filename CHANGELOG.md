# 📊 Changelog / 版本历史

All notable changes to this project will be documented in this file.  
所有重要变更都将记录在此文件中。

**Format**: [Semantic Versioning](https://semver.org/)  
**格式**: [语义化版本](https://semver.org/lang/zh-CN/)

---

## [1.1.0] - 2026-03-24

### 🎯 Stop Loss & Take Profit Alerts / 止盈止损提醒

#### 🇺🇸 Added
- Stop Loss & Take Profit alert system
  - Create price alerts with entry, stop-loss, and take-profit levels
  - Automatic trigger detection
  - Risk/Reward ratio calculation
  - Potential profit/loss estimation
- Price level calculator
  - Percentage-based stop-loss/take-profit calculation
  - Customizable risk parameters
- Alert management
  - Active/Triggered/Cancelled status tracking
  - JSON-based persistence
  - Detailed logging

#### 🇨🇳 新增
- 止盈止损提醒系统
  - 创建包含入场价、止损价、止盈价的价格提醒
  - 自动触发检测
  - 风险收益比计算
  - 潜在盈亏估算
- 价格位计算器
  - 基于百分比的止损/止盈计算
  - 可配置风险参数
- 提醒管理
  - 活跃/已触发/已取消状态跟踪
  - JSON 持久化
  - 详细日志记录

---

## [1.0.0] - 2026-03-24

### 🎉 Initial Release / 初始版本

#### 🇺🇸 Added
- Support & Resistance level calculation
  - Multiple algorithms (Previous High/Low, Moving Averages, Fibonacci, Pivot Points)
  - Strength indicator (strong/medium/weak)
- Trading signal generation
  - RSI, MACD, Moving Averages analysis
  - Combined signal scoring
  - Recommendations: Strong Buy/Buy/Hold/Sell/Strong Sell
- Position size calculator
  - Risk-based position sizing
  - Risk profiles: Conservative/Moderate/Aggressive
  - Portfolio allocation
- Internationalization (i18n)
  - English and Chinese support
  - Language switching via environment variable
- Configuration system
  - User-configurable API Keys
  - Customizable watchlist
  - Optional notifications (Feishu, DingTalk, Email)
- Documentation
  - Bilingual README (EN/ZH)
  - Configuration guide
  - I18N guide
  - Usage examples

#### 🇨🇳 新增
- 支撑/阻力位计算
  - 多种算法（前高/前低、均线、斐波那契、枢轴点）
  - 强度指示（强/中/弱）
- 买卖信号生成
  - RSI, MACD, 均线分析
  - 综合信号评分
  - 操作建议：强买/买入/观望/卖出/强卖
- 仓位计算器
  - 基于风险的仓位计算
  - 风险偏好：保守型/稳健型/进取型
  - 投资组合配置
- 国际化支持
  - 英文和中文支持
  - 通过环境变量切换语言
- 配置系统
  - 用户可配置 API Keys
  - 自定义股票列表
  - 可选推送通知（飞书、钉钉、邮件）
- 文档
  - 双语 README (英文/中文)
  - 配置指南
  - 国际化指南
  - 使用示例

---

## 🔗 Links / 链接

- [GitHub Releases](https://github.com/XuXuClassMate/trading-assistant/releases)
- [Compare Versions](https://github.com/XuXuClassMate/trading-assistant/compare)

---

## 📝 Versioning Policy / 版本策略

**🇺🇸**: This project follows [Semantic Versioning](https://semver.org/):
- **MAJOR** version for incompatible changes
- **MINOR** version for backwards-compatible features
- **PATCH** version for backwards-compatible bug fixes

**🇨🇳**: 本项目遵循 [语义化版本](https://semver.org/lang/zh-CN/)：
- **主版本号**：不兼容的 API 修改
- **次版本号**：向下兼容的功能新增
- **修订号**：向下兼容的问题修正

---

*Last Updated: 2026-03-24*
