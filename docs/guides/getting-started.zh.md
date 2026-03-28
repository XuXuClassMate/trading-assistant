# 🚀 入门指南

**时间**: 15 分钟  
**级别**: 初学者

---

## ✅ 先决条件

- 已安装交易助手（[安装指南](install-overview.md)）
- 已配置 API 密钥（[API 设置](api-keys.md)）

---

## 📝 步骤 1：验证安装

```bash
ta --version
```

预期输出：
```
OpenClaw Trading Assistant CLI v1.3.2
```

---

## 📝 步骤 2：配置 API 密钥

在工作目录中创建 `.env` 文件：

```bash
# 创建 .env 文件
cat > .env << EOF
TWELVE_DATA_API_KEY=your_key_here
ALPHA_VANTAGE_API_KEY=your_key_here
LANGUAGE=zh
EOF
```

[→ 详细 API 设置](api-keys.md)

---

## 📝 步骤 3：设置观察列表

创建包含要监控股票的 `watchlist.txt`：

```bash
cat > watchlist.txt << EOF
NVDA
AAPL
MSFT
GOOGL
TSLA
EOF
```

[→ 自选列表配置](watchlist-setup.zh.md)

---

## 📝 步骤 4：运行第一次分析

### 交互模式

```bash
ta
```

你将看到：
```
============================================================
  OpenClaw Trading Assistant CLI
  Version: 1.3.2
============================================================

ta> 
```

输入命令：
```
ta> help
ta> sig
ta> exit
```

### 直接命令

```bash
# 分析观察列表中的所有股票
ta all
```

---

## 📊 理解输出

### 交易信号示例

```
📈 正在生成信号...

NVDA:
  RSI: 52.34 [中性]
  MACD: 0.1234 [看涨]
  移动平均线：[看涨]
  综合：看涨 (评分：3)
  推荐：买入 (置信度：中等)

✅ 完成！
```

**含义**：
- **RSI**: 动量指标（30-70 为中性）
- **MACD**: 趋势指标（正值 = 看涨）
- **移动平均线**: 价格趋势方向
- **综合**: 整体信号
- **推荐**: 操作建议

---

## 🎯 常见工作流

### 每日市场检查

```bash
# 快速信号
ta sig

# 特定股票的详细分析
ta sig --symbol NVDA

# 所有分析（支撑阻力 + 信号 + 仓位）
ta all
```

### 仓位规划

```bash
# 计算交易仓位
ta pos --symbol NVDA --price 175 --capital 10000 --risk 2

# 输出显示：
# - 购买股数
# - 仓位价值
# - 风险金额
# - 止损水平
```

### 价格提醒

```bash
# 列出现有提醒
ta alerts list

# 创建新提醒
ta alerts create --symbol NVDA --entry 175 --stop 170 --target 185

# 检查是否触发提醒
ta alerts check
```

---

## 📚 了解更多

### CLI 命令

| 命令 | 描述 |
|------|------|
| `ta` | 交互模式 |
| `ta sig` | 交易信号 |
| `ta sr` | 支撑/阻力 |
| `ta pos` | 仓位计算器 |
| `ta alerts` | 价格提醒 |
| `ta all` | 完整分析 |

[→ 完整 CLI 参考](../CLI.md)

### 高级主题

- [技术指标](advanced-indicators.md)
- [风险管理](risk-management.md)
- [提醒策略](price-alerts.md)

---

## ❓ 故障排除

### "API 密钥无效"

检查 `.env` 文件：
```bash
cat .env
```

确保密钥正确（无多余空格）。

### "观察列表中没有股票"

创建 watchlist.txt：
```bash
echo "NVDA" > watchlist.txt
echo "AAPL" >> watchlist.txt
```

### "找不到命令：ta"

确保安装完成：
```bash
# pip
pip show openclaw-trading-assistant

# npm
npm list -g @xuxuclassmate/openclaw-trading-assistant
```

---

## 🎉 准备好了！

现在你可以：
- ✅ 生成交易信号
- ✅ 分析支撑/阻力位
- ✅ 计算仓位大小
- ✅ 设置价格提醒

**下一步**: [交易信号指南](trading-signals.md)
