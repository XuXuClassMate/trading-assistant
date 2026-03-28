# 日报系统使用指南

**版本**: v1.5.0 | **最后更新**: 2026-03-26

Trading Assistant 自动化日报系统的完整使用指南，包含三级分析详解。

---

## 📊 功能概览

日报系统提供三种详细程度的自动化市场分析，适用于不同场景和时间需求。

### 三级报告

| 等级 | 阅读时间 | 内容 | 使用场景 |
|------|---------|------|---------|
| **Small** 📝 | 10 秒 | 关键数据 + 市场情绪 | 日常快速推送 |
| **Medium** 📊 | 1 分钟 | 技术分析 + 操作策略 | 日常复盘 |
| **Large** 📈 | 5 分钟 | 深度分析 + 持仓报告 | 周末/月度总结 |

---

## 🚀 快速开始

### 手动生成报告

```bash
cd trading-assistant

# 早盘简报 (Small)
python3 daily_report.py morning small

# 盘后标准 (Medium)
python3 daily_report.py evening medium

# 盘后深度 (Large)
python3 daily_report.py evening large
```

### 自动化定时任务 (Heartbeat)

在 `HEARTBEAT.md` 中添加：

```markdown
## 股票日报

### 早盘预期 (HKT 09:00 = UTC 01:00)
- 时间：每天 UTC 01:00-02:00
- 执行:
  ```bash
  cd ~/skills/trading-assistant && python3 daily_report.py morning small
  ```

### 盘后总结 (HKT 17:00 = UTC 09:00)
- 时间：每天 UTC 09:00-10:00
- 执行:
  ```bash
  cd ~/skills/trading-assistant && python3 daily_report.py evening medium
  ```

### 深度分析 (HKT 20:00 = UTC 12:00)
- 时间：每天 UTC 12:00-13:00
- 执行:
  ```bash
  cd ~/skills/trading-assistant && python3 daily_report.py evening large
  ```
```

---

## 📝 报告等级详解

### Small 报告 📝 (10 秒)

**用途**: 忙碌交易者的快速市场快照

**内容**:
- 市场状态概览
- 关键情绪指标
- 预期波动范围
- 重要支撑/阻力位

**适用场景**:
- 早盘开盘前检查
- 晚间快速复盘
- 手机推送通知

**输出示例**:
```
📊 早盘简报 - 2026-03-26

市场状态：开盘
市场情绪：看涨 (65%)
预期波动：+0.5% 至 +1.2%

关键位置:
- SPY 阻力：$582.50
- SPY 支撑：$578.00

祝交易顺利！🚀
```

---

### Medium 报告 📊 (1 分钟)

**用途**: 标准日常分析，提供可操作建议

**内容**:
- 包含 Small 报告全部内容
- 技术指标摘要 (RSI, MACD, BB)
- 自选股买卖信号
- 入场/出场建议
- 风险管理提示

**适用场景**:
- 日常交易决策
- 投资组合复盘
- 策略调整

**输出示例**:
```
📊 盘后总结 - 2026-03-26

市场表现:
- SPY: +0.85% (看涨)
- QQQ: +1.23% (看涨)

技术信号:
🟢 AAPL: 买入 (RSI: 45, MACD: 看涨)
🟡 NVDA: 观望 (RSI: 68, 接近阻力位)
🟢 TSLA: 强烈买入 (突破确认)

自选股汇总:
- 3 个买入信号
- 2 个观望信号
- 0 个卖出信号

明日关注:
- 美联储讲话 14:00 EST
- 财报：MSFT (盘后)
```

---

### Large 报告 📈 (5 分钟)

**用途**: 深度分析，适合严肃交易者

**内容**:
- 包含 Medium 报告全部内容
- 详细技术分析 (10 个指标)
- 持仓表现分析
- 板块轮动分析
- 新闻情绪分析
- 风险评估
- 次日/周展望

**适用场景**:
- 周末深度复盘
- 月度投资组合审查
- 策略优化
- 学习研究

**主要章节**:
```
📊 深度分析 - 2026-03-26

1. 市场概览
   - 主要指数表现
   - 成交量分析
   - 涨跌家数比

2. 技术深度分析
   - 各板块 RSI 分析
   - MACD 背离/收敛
   - 布林带位置
   - 均线排列

3. 持仓分析
   - 个股表现
   - 成本价对比
   - 浮动盈亏
   - 仓位配置审查

4. 板块轮动
   - 强势板块
   - 弱势板块
   - 资金流向

5. 新闻情绪
   - 利好因素
   - 风险因素
   - 财报惊喜

6. 展望与策略
   - 次日预期
   - 关键位置
   - 建议操作
```

---

## 📁 文件位置

### 生成的报告

```
trading-assistant/reports/
├── 2026-03-26_morning_small.md
├── 2026-03-26_evening_medium.md
└── 2026-03-26_evening_large.md
```

### 已发送报告

```
trading-assistant/sent/
├── 2026-03-26_morning_small.md
└── 2026-03-26_evening_medium.md
```

### 学习数据

```
trading-assistant/learning/
├── predictions_2026-03.json
└── accuracy_stats.json
```

---

## 🔧 配置说明

### 环境变量

```bash
# API Keys
TWELVE_DATA_API_KEY=your_key
ALPHA_VANTAGE_API_KEY=your_key

# LLM Provider (用于生成分析)
DASHSCOPE_API_KEY=your_key
QWEN_MODEL=qwen3.5-plus

# 飞书推送
FEISHU_APP_ID=your_app_id
FEISHU_APP_SECRET=your_app_secret
FEISHU_WEBHOOK_URL=https://...

# 交易设置
TRADING_LANG=zh_CN  # 或 en
DEFAULT_RISK_PROFILE=moderate
```

### 自选股配置

编辑 `watchlist.txt`:

```
# 美股
AAPL|Apple Inc.
NVDA|NVIDIA Corporation
TSLA|Tesla Inc.
MSFT|Microsoft Corporation

# A 股
600519|贵州茅台
000858|五粮液

# 加密货币
BTCUSDT|Bitcoin
ETHUSDT|Ethereum
```

---

## 📊 学习系统

### 预测跟踪

系统自动：
1. 保存预测到 `learning/predictions_YYYY-MM.json`
2. 验证预测与实际价格的准确性
3. 计算准确率统计
4. 生成周/月度报告

### 准确性报告

```bash
# 生成 30 天准确性报告
python3 daily_report.py accuracy 30

# 显示学习统计
python3 daily_report.py stats
```

### 持续改进

学习系统分析：
- 信号准确性 (买入/卖出/观望)
- 置信度校准
- 最佳/最差表现股票
- 时间模式
- 板块表现

---

## 🎯 最佳实践

### 晨间流程 (10-15 分钟)

1. **查看 Small 报告** (10 秒)
   - 快速市场状态
   - 关键位置

2. **阅读 Medium 报告** (1 分钟)
   - 交易信号
   - 入场/出场点

3. **调整自选股** (5-10 分钟)
   - 添加/删除股票
   - 更新目标价

### 晚间流程 (15-30 分钟)

1. **查看 Medium 报告** (1 分钟)
   - 当日表现
   - 信号准确性

2. **阅读 Large 报告** (5 分钟，可选)
   - 深度分析
   - 持仓审查

3. **规划明日** (5-10 分钟)
   - 设置提醒
   - 准备自选股

### 周度复盘 (30-60 分钟，周末)

1. **阅读本周 Large 报告**
2. **检查准确性统计**
3. **根据表现调整策略**
4. **更新下周自选股**

---

## ⚠️ 故障排除

### 常见问题

**问题**: 报告无法生成

**解决方案**:
```bash
# 检查 API keys
cat .env | grep API_KEY

# 测试数据连接
python3 -c "from config import get_api_key; print(get_api_key('TWELVE_DATA'))"

# 查看日志
tail -f logs/daily_report.log
```

**问题**: 飞书推送不发送

**解决方案**:
```bash
# 测试飞书连接
python3 -c "from feishu_utils import test_webhook; test_webhook()"

# 验证 webhook URL
cat .env | grep FEISHU_WEBHOOK
```

**问题**: 报告生成缓慢

**解决方案**:
```bash
# 减少自选股数量
# 启用缓存
# 在配置中减少指标数量
```

---

## 📚 相关文档

- [入门指南](../index.zh.md) - 安装和设置
- [技术分析](technical-analysis.zh.md) - 指标详解
- [持仓管理](position-management.zh.md) - 持仓跟踪
- [风险管理](risk-management.zh.md) - 止损和仓位计算
- [API Keys 设置](api-keys.zh.md) - 获取 API 凭证

---

## 🔗 资源链接

- **GitHub**: https://github.com/XuXuClassMate/trading-assistant
- **问题反馈**: https://github.com/XuXuClassMate/trading-assistant/issues
- **PyPI**: https://pypi.org/project/trading-assistant/

---

**最后更新**: 2026-03-26 | **版本**: v1.5.0
