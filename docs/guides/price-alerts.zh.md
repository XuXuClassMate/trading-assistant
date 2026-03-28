# 🔔 价格提醒

**版本**: v1.5.0  
**最后更新**: 2026-03-25

---

## 📊 概述

价格提醒功能帮助你监控关键价格水平，自动通知止盈止损触发情况。

### 核心特性

- ✅ **多提醒支持** - 同时监控多个价格水平
- ✅ **自动检测** - 实时监控价格变化
- ✅ **灵活配置** - 支持入场/止损/止盈
- ✅ **日志记录** - 记录所有提醒历史

---

## 🎯 提醒类型

### 1. 入场提醒

**用途**: 价格达到理想入场点时提醒

**设置**:
```bash
ta alerts create --symbol BTC --entry 67000
```

**触发条件**:
- 价格 ≥ 入场价 (做多)
- 价格 ≤ 入场价 (做空)

---

### 2. 止损提醒

**用途**: 价格触及止损位时提醒离场

**设置**:
```bash
ta alerts create --symbol BTC --stop 64000
```

**触发条件**:
- 价格 ≤ 止损价 (多头仓位)
- 价格 ≥ 止损价 (空头仓位)

---

### 3. 止盈提醒

**用途**: 价格达到目标位时提醒获利了结

**设置**:
```bash
ta alerts create --symbol BTC --target 72000
```

**触发条件**:
- 价格 ≥ 目标价 (多头仓位)
- 价格 ≤ 目标价 (空头仓位)

---

### 4. 综合提醒

**用途**: 同时设置入场/止损/止盈

**设置**:
```bash
ta alerts create --symbol BTC \
  --entry 67000 \
  --stop 64000 \
  --target 72000
```

---

## 🛠️ 使用方法

### CLI 命令

```bash
# 创建提醒
ta alerts create --symbol BTC --entry 67000

# 创建综合提醒
ta alerts create --symbol BTC --entry 67000 --stop 64000 --target 72000

# 列出所有提醒
ta alerts list

# 删除提醒
ta alerts delete --id 1

# 清除所有提醒
ta alerts clear

# 检查是否触发
ta alerts check
```

### 输出示例

```
🔔 Price Alerts
============================================================
Active Alerts:

ID: 1
  Symbol: BTC
  Entry: $67,000.00
  Stop: $64,000.00 (-4.5%)
  Target: $72,000.00 (+7.5%)
  Current: $67,500.00
  Status: Active (Entry reached ✅)

ID: 2
  Symbol: ETH
  Entry: $3,500.00
  Stop: $3,200.00 (-8.6%)
  Target: $4,000.00 (+14.3%)
  Current: $3,450.00
  Status: Waiting

Summary:
  Total: 2
  Active: 2
  Triggered: 1
============================================================
```

---

## 📊 实际应用

### 提醒策略

#### 突破策略

**场景**: 预期价格突破阻力位

**设置**:
```bash
# 阻力位突破买入
ta alerts create --symbol BTC --entry 72000 --stop 69000 --target 78000
```

**逻辑**:
- 突破 $72,000 入场
- 止损 $69,000 (-4.2%)
- 目标 $78,000 (+8.3%)

#### 回调策略

**场景**: 等待价格回调到支撑位

**设置**:
```bash
# 支撑位回调买入
ta alerts create --symbol BTC --entry 64000 --stop 61000 --target 70000
```

**逻辑**:
- 回调到 $64,000 入场
- 止损 $61,000 (-4.7%)
- 目标 $70,000 (+9.4%)

---

## ⚙️ 配置选项

### 提醒文件

提醒保存在 `alerts.json` 文件中：

```json
{
  "alerts": [
    {
      "id": 1,
      "symbol": "BTC",
      "entry": 67000,
      "stop": 64000,
      "target": 72000,
      "created_at": "2026-03-25T10:00:00Z",
      "status": "active"
    }
  ]
}
```

### 自动检查

**手动检查**:
```bash
ta alerts check
```

**自动检查** (推荐):
```bash
# 每 5 分钟检查一次
while true; do ta alerts check; sleep 300; done
```

---

## ⚠️ 注意事项

### 局限性

1. **非实时** - 需要手动或定时运行检查
2. **本地运行** - 需要保持程序运行
3. **无推送** - 仅在终端显示提醒

### 最佳实践

1. **定期运行** - 设置定时任务检查提醒
2. **合理设置** - 止损止盈比例合理 (1:2 或 1:3)
3. **及时清理** - 移除已触发或过期的提醒
4. **记录总结** - 记录提醒触发情况，优化策略

---

## 🔗 相关文档

- [交易信号](trading-signals.zh.md) - 信号生成
- [仓位管理](position-management.zh.md) - 仓位计算
- [实时监控](realtime-backtest.zh.md) - 市场监控
- [CLI 参考](../CLI.md) - 命令行使用

---

**最后更新**: 2026-03-25 13:00 UTC  
**版本**: v1.5.0  
**建议**: 设置提醒后定期运行 `ta alerts check`
