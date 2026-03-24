# 📦 ClawHub 提交文档

**提交日期**: 2026-03-24
**项目名称**: OpenClaw Trading Assistant
**版本**: v1.0.0

---

## 📋 基本信息 (复制粘贴用)

```
名称：OpenClaw Trading Assistant
版本：1.0.0
作者：OpenClaw Community
许可证：MIT
分类：金融/交易
标签：trading, finance, technical-analysis, stock-market, investment, openclaw
```

---

## 📖 项目描述 (复制粘贴用)

```markdown
OpenClaw Trading Assistant 是一个功能完整的交易辅助决策系统，为投资者提供技术分析、买卖信号、仓位管理和风险监控等功能。

✨ 核心特性：
📊 支撑/阻力位自动计算（前高/前低、均线、斐波那契、枢轴点）
📈 多指标买卖信号生成（RSI、MACD、均线交叉）
💰 智能仓位计算器（风险偏好、置信度调整）
⚠️ 止盈止损提醒（价格监控、推送通知）
📱 飞书/钉钉推送集成

🎯 适合人群：
- 股票/ETF 投资者
- 技术分析爱好者
- 量化交易初学者
- OpenClaw 用户

⚙️ 技术栈：
- Python 3.11+
- Twelve Data API (免费 800 次/天)
- Alpha Vantage API (免费 25 次/天)
- OpenClaw v1.0+
```

---

## 🛠️ 安装说明 (复制粘贴用)

```markdown
## 快速安装

### 1. 下载技能包
```bash
# 方式 1: 从 ClawHub 下载
# 方式 2: Git 克隆
git clone https://github.com/XuXuClassMate/trading-assistant.git
cd trading-assistant
```

### 2. 安装依赖
```bash
pip install -r requirements.txt
```

### 3. 配置 API Keys
```bash
# 复制环境变量模板
cp .env.example .env

# 编辑 .env 填入你的 API Keys
# Twelve Data: https://twelvedata.com/pricing (免费 800 次/天)
# Alpha Vantage: https://www.alphavantage.co/support/#api-key (免费 25 次/天)
```

### 4. 测试安装
```bash
# 测试支撑/阻力位模块
python3 support_resistance.py

# 测试买卖信号模块
python3 trading_signals.py

# 测试仓位计算模块
python3 position_calculator.py
```

### 5. 开始使用
```python
from support_resistance import calculate_support_resistance

# 计算 NVDA 的支撑/阻力位
result = calculate_support_resistance("NVDA")
```
```

---

## 📸 截图素材

### 截图 1: 支撑/阻力位分析

**文件**: `screenshots/support_resistance_output.txt`

**说明文字**:
```
自动计算关键支撑位和阻力位，基于多种算法：
- 前高/前低法
- 移动平均线 (20/50/200 日)
- 斐波那契回撤
- 枢轴点 (Pivot Points)
- 心理价位

输出包含价格位、强度等级、距离百分比
```

---

### 截图 2: 买卖信号生成

**文件**: `screenshots/trading_signals_output.txt`

**说明文字**:
```
综合多个技术指标生成操作建议：
- RSI 超买/超卖信号
- MACD 金叉/死叉信号
- 均线交叉信号
- 综合信号 (强买/买/观望/卖/强卖)

每个信号包含置信度评估，帮助用户判断可靠性
```

---

### 截图 3: 仓位计算器

**文件**: `screenshots/position_calculator_output.txt`

**说明文字**:
```
智能仓位管理，根据风险承受能力自动计算：
- 风险偏好：保守/稳健/进取
- 置信度调整：高/中/低
- 止损位自动计算
- 投资组合配置优化

输出包含股数、仓位价值、风险金额、风险收益比
```

---

## 🎯 功能特性 (复制粘贴用)

```markdown
## 核心功能

### 1. 支撑/阻力位计算 📊
- 前高/前低法 - 识别关键价格位
- 移动平均线 - 动态支撑/阻力 (20/50/200 日)
- 斐波那契回撤 - 0%, 23.6%, 38.2%, 50%, 61.8%, 78.6%, 100%
- 枢轴点 - 经典 Pivot Points (R1/R2/R3, S1/S2/S3)
- 心理价位 - 整数关口识别
- 强度判断 - strong/medium/weak

### 2. 买卖信号生成 📈
- RSI 指标 - 超买 (>70) / 超卖 (<30)
- MACD 指标 - 金叉/死叉检测
- 均线交叉 - 短期/长期均线关系
- 综合信号 - 多指标加权评分
- 操作建议 - 强买/买/观望/卖/强卖
- 置信度 - high/medium/low

### 3. 智能仓位计算 💰
- 风险偏好 - conservative/moderate/aggressive
- 置信度调整 - 高置信度增加仓位
- 止损位计算 - 自动计算风险金额
- 最大仓位限制 - 防止过度集中
- 投资组合配置 - 多股票资金分配
- 风险收益比 - 1:2 以上推荐

### 4. 实时监控预警 ⚠️ (开发中)
- 价格波动监控 - >5% 即时推送
- 成交量异常 - >2 倍平均成交量
- 止盈止损提醒 - 价格到达自动通知
- 重大新闻推送 - 影响市场的事件

### 5. 飞书推送集成 📱
- 日报推送 - 早盘/盘后分析
- 实时预警 - 大波动即时通知
- 准确性统计 - 每周预测准确率报告
```

---

## 📊 使用示例 (复制粘贴用)

```markdown
## 基础用法

### 计算支撑/阻力位
```python
from support_resistance import calculate_support_resistance, print_support_resistance

result = calculate_support_resistance("NVDA")
print_support_resistance(result)

# 输出:
# NVDA 当前价：$175.64
# 阻力位：$177.26 (+0.9%), $180.00 (+2.5%)
# 支撑位：$175.00 (-0.4%), $171.72 (-2.2%)
```

### 生成买卖信号
```python
from trading_signals import generate_trading_signal, print_trading_signal

result = generate_trading_signal("AAPL")
print_trading_signal(result)

# 输出:
# RSI: 52.34 [中性]
# MACD: 0.1234 [看涨]
# 均线：[看涨]
# 综合建议：买入 (置信度：中)
```

### 计算仓位
```python
from position_calculator import calculate_position_size, print_position_result

result = calculate_position_size(
    total_capital=100000,      # 总资金 $100,000
    entry_price=175.64,        # 入场价
    stop_loss_price=165.00,    # 止损价
    risk_profile="moderate",   # 稳健型
    confidence="medium"        # 中置信度
)
print_position_result(result)

# 输出:
# 仓位：562 股 ($98,710, 98.7%)
# 风险：$5,964 (5.96%)
# 止损幅度：6.06%
```

### 投资组合配置
```python
from position_calculator import calculate_portfolio_allocation

positions = [
    {"symbol": "NVDA", "entry_price": 175.64, "confidence": "medium"},
    {"symbol": "AAPL", "entry_price": 251.49, "confidence": "high"},
    {"symbol": "SPY", "entry_price": 580.00, "confidence": "medium"}
]

portfolio = calculate_portfolio_allocation(
    total_capital=100000,
    positions=positions,
    risk_profile="moderate"
)
```
```

---

## ⚠️ 免责声明 (复制粘贴用)

```markdown
**重要提示**: 本软件仅供学习和研究使用，不构成投资建议。

- 市场有风险，投资需谨慎
- 过往表现不代表未来结果
- 请独立判断，自负盈亏
- 开发者不承担任何投资损失责任
- 建议使用模拟盘测试后再使用真实资金
```

---

## 🔗 相关链接

- **GitHub 仓库**: https://github.com/XuXuClassMate/trading-assistant
- **问题反馈**: https://github.com/XuXuClassMate/trading-assistant/issues
- **OpenClaw 官网**: https://openclaw.ai
- **ClawHub 社区**: https://clawhub.com
- **Twelve Data**: https://twelvedata.com
- **Alpha Vantage**: https://www.alphavantage.co

---

## 📝 提交流程

### 步骤 1: 登录 ClawHub
访问 https://clawhub.com 并登录账号

### 步骤 2: 发布技能
点击 "发布技能" 或 "Submit Skill"

### 步骤 3: 填写信息
复制粘贴上方提供的内容：
- 基本信息
- 项目描述
- 安装说明
- 功能特性
- 使用示例
- 免责声明

### 步骤 4: 上传截图
从 `screenshots/` 目录选择：
- `support_resistance_output.txt`
- `trading_signals_output.txt`
- `position_calculator_output.txt`

### 步骤 5: 填写 GitHub 链接
```
https://github.com/XuXuClassMate/trading-assistant
```

### 步骤 6: 提交审核
确认无误后提交，等待 1-3 个工作日审核

---

## ✅ 检查清单

提交前确认：
- [x] 所有敏感信息已移除
- [x] API Keys 使用环境变量
- [x] 文档完整清晰
- [x] 示例代码可运行
- [x] 截图素材已准备
- [x] GitHub 仓库已创建
- [x] 许可证已添加 (MIT)
- [x] .gitignore 已配置

---

**准备完成！可以开始提交了！** 🎉
