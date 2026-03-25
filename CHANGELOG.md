# 📊 Changelog / 版本历史

All notable changes to this project will be documented in this file.  
所有重要变更都将记录在此文件中。

**Format**: [Semantic Versioning](https://semver.org/)  
**格式**: [语义化版本](https://semver.org/lang/zh-CN/)

---

## [1.3.0] - 2026-03-25

### 🖥️ CLI Interactive Mode

#### ✨ New Features

- 🖥️ **Interactive CLI Mode**
  - Full interactive command-line interface
  - Command history and auto-completion support
  - Bilingual prompts (English/Chinese)
  - Built-in help system

- 📋 **Available Commands**
  - `interactive` - Start interactive mode / 交互模式
  - `support-resistance` - Analyze support/resistance levels
  - `signals` - Generate trading signals
  - `position` - Calculate position size
  - `alerts` - Manage price alerts
  - `all` - Run all analysis
  - `version` - Show version info
  - `help` - Show help message

- 🎯 **Command Shortcuts**
  - `sr` → support-resistance
  - `sig` → signals
  - `pos` → position
  - `calc` → position calculator

#### 🔧 Improvements

- 📦 **Package Entry Point**
  - Added `[project.scripts]` to pyproject.toml
  - CLI accessible via `openclaw-trading-assistant` command
  - Works in Docker containers and pip installations

#### 📚 Documentation

- Updated README with CLI usage examples
- Added interactive mode screenshots
- Docker documentation updated

---

### 🖥️ CLI 交互模式

#### ✨ 新功能

- 🖥️ **交互式命令行界面**
  - 完整的交互式 CLI
  - 支持命令历史和自动补全
  - 双语提示（英文/中文）
  - 内置帮助系统

- 📋 **可用命令**
  - `interactive` - 启动交互模式
  - `support-resistance` - 分析支撑阻力位
  - `signals` - 生成交易信号
  - `position` - 计算仓位大小
  - `alerts` - 管理价格提醒
  - `all` - 运行所有分析
  - `version` - 显示版本信息
  - `help` - 显示帮助信息

- 🎯 **命令快捷方式**
  - `sr` → support-resistance
  - `sig` → signals
  - `pos` → position
  - `calc` → 仓位计算器

#### 🔧 改进

- 📦 **包入口点**
  - 在 pyproject.toml 中添加 [project.scripts]
  - 可通过 `openclaw-trading-assistant` 命令访问
  - 支持 Docker 容器和 pip 安装

#### 📚 文档

- README 更新 CLI 使用示例
- 添加交互模式截图
- Docker 文档更新

---

## [1.2.0] - 2026-03-24

### 🐳 Docker Support & Multi-Platform Distribution

#### ✨ New Features

- 🐳 **Docker Container Support**
  - Official Docker image with Python 3.11
  - Multi-platform builds (linux/amd64, linux/arm64)
  - Optimized image size (~150MB)
  - Ready-to-run CLI interface

- 📦 **Multi-Registry Distribution**
  - GitHub Container Registry (ghcr.io)
  - Docker Hub (docker.io)
  - Automated CI/CD pipeline
  - Version tags + latest tag

- 📚 **Docker Documentation**
  - Quick start guide
  - Configuration examples
  - Volume mount instructions
  - Environment variable reference

#### 🔧 Improvements

- 🧹 **Code Cleanup**
  - Removed redundant npm/PyPI GitHub workflows
  - Simplified publish pipeline
  - Better separation of concerns

- 📝 **Updated Documentation**
  - README with Docker installation
  - Bilingual installation guides
  - Clear distribution channel info

---

### 🐳 Docker 支持与多平台分发

#### ✨ 新功能

- 🐳 **Docker 容器支持**
  - 官方 Python 3.11 Docker 镜像
  - 多平台构建 (linux/amd64, linux/arm64)
  - 优化的镜像大小 (~150MB)
  - 开箱即用的 CLI 界面

- 📦 **多仓库分发**
  - GitHub Container Registry (ghcr.io)
  - Docker Hub (docker.io)
  - 自动化 CI/CD 流水线
  - 版本标签 + latest 标签

- 📚 **Docker 文档**
  - 快速入门指南
  - 配置示例
  - 卷挂载说明
  - 环境变量参考

#### 🔧 改进

- 🧹 **代码清理**
  - 删除冗余的 npm/PyPI GitHub 工作流
  - 简化发布流程
  - 更好的职责分离

- 📝 **文档更新**
  - README 添加 Docker 安装说明
  - 双语安装指南
  - 清晰的分发渠道说明

---

## [1.1.0] - 2026-03-24

### 🎯 Stop Loss & Take Profit Alerts

#### ✨ New Features

- 🎯 **Stop Loss & Take Profit Alert System**
  - Create price alerts with entry, stop-loss, and take-profit levels
  - Automatic trigger detection
  - Risk/Reward ratio calculation
  - Potential profit/loss estimation
  - Alert history logging

- 📊 **Price Level Calculator**
  - Percentage-based stop-loss/take-profit calculation
  - Customizable risk parameters

- 📝 **Alert Management**
  - Active/Triggered/Cancelled status tracking
  - JSON-based persistence
  - Detailed logging

---

### 🎯 止盈止损提醒

#### ✨ 新功能

- 🎯 **止盈止损提醒系统**
  - 创建包含入场价、止损价、止盈价的价格提醒
  - 自动触发检测
  - 风险收益比计算
  - 潜在盈亏估算
  - 提醒历史记录

- 📊 **价格位计算器**
  - 基于百分比的止损/止盈计算
  - 可配置风险参数

- 📝 **提醒管理**
  - 活跃/已触发/已取消状态跟踪
  - JSON 持久化
  - 详细日志记录

---

## [1.0.0] - 2026-03-24

### 🎉 Initial Release

#### ✨ New Features

- 📊 **Support & Resistance Level Calculation**
  - Multiple algorithms (Previous High/Low, Moving Averages, Fibonacci, Pivot Points)
  - Strength indicator (strong/medium/weak)

- 📈 **Trading Signal Generation**
  - RSI, MACD, Moving Averages analysis
  - Combined signal scoring
  - Recommendations: Strong Buy/Buy/Hold/Sell/Strong Sell

- 💰 **Position Size Calculator**
  - Risk-based position sizing
  - Risk profiles: Conservative/Moderate/Aggressive
  - Portfolio allocation

- 🌍 **Internationalization (i18n)**
  - English and Chinese support
  - Language switching via environment variable

- ⚙️ **Configuration System**
  - User-configurable API Keys
  - Customizable watchlist
  - Optional notifications (Feishu, DingTalk, Email)

- 📚 **Documentation**
  - Bilingual README (English/Chinese)
  - Configuration guide
  - I18N guide
  - Usage examples

---

### 🎉 初始版本

#### ✨ 新功能

- 📊 **支撑/阻力位计算**
  - 多种算法（前高/前低、均线、斐波那契、枢轴点）
  - 强度指示（强/中/弱）

- 📈 **买卖信号生成**
  - RSI, MACD, 均线分析
  - 综合信号评分
  - 操作建议：强买/买入/观望/卖出/强卖

- 💰 **仓位计算器**
  - 基于风险的仓位计算
  - 风险偏好：保守型/稳健型/进取型
  - 投资组合配置

- 🌍 **国际化支持**
  - 英文和中文支持
  - 通过环境变量切换语言

- ⚙️ **配置系统**
  - 用户可配置 API Keys
  - 自定义股票列表
  - 可选推送通知（飞书、钉钉、邮件）

- 📚 **文档**
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

### English

This project follows [Semantic Versioning](https://semver.org/):

- **MAJOR** version for incompatible changes
- **MINOR** version for backwards-compatible features
- **PATCH** version for backwards-compatible bug fixes

---

### 中文

本项目遵循 [语义化版本](https://semver.org/lang/zh-CN/)：

- **主版本号**：不兼容的 API 修改
- **次版本号**：向下兼容的功能新增
- **修订号**：向下兼容的问题修正

---

*Last Updated: 2026-03-24*
