# 性能优化指南

优化 API 调用，提升执行效率。

## 概述 🚀

Trading Assistant 使用多个外部 API 获取数据。为避免速率限制并提升性能，系统内置了：

- **API 缓存** - 减少重复调用
- **速率限制** - 避免超限
- **批量处理** - 优化大数据集

## API 限制 📊

### Twelve Data

| 套餐 | 限制 | 适用场景 |
|------|------|---------|
| **免费** | 800 次/天 | 个人使用 |
| **基础** | 12,000 次/天 | 高频监控 |
| **专业** | 无限制 | 商业应用 |

**建议**: 免费账户每 60 秒调用一次。

### Alpha Vantage

| 套餐 | 限制 | 说明 |
|------|------|------|
| **免费** | 25 次/天 | 基础功能 |
| **付费** | 75 次/分钟 | 高级功能 |

**建议**: 免费账户谨慎使用，优先使用 Twelve Data。

### CoinGecko

| 套餐 | 限制 | 说明 |
|------|------|------|
| **免费** | 10-50 次/分钟 | 加密货币数据 |
| **Demo** | 30 次/分钟 | 注册获取 |

## 缓存系统 💾

### 工作原理

```
请求数据 → 检查缓存 → 缓存命中 → 返回数据
              ↓
         缓存未命中
              ↓
         调用 API → 保存缓存 → 返回数据
```

### 缓存配置

**位置**: `~/.trading_assistant/cache/api_cache.json`

**TTL**: 5 分钟（300 秒）

**最大条目**: 1000 条

### 缓存管理

```bash
# 查看缓存统计
python3 -c "from optimizer import api_cache; print(api_cache.stats())"

# 清除缓存
python3 -c "from optimizer import api_cache; api_cache.clear()"
```

### 代码示例

```python
from optimizer import api_cache

# 获取缓存
cached = api_cache.get('price', {'symbol': 'AAPL'})
if cached:
    print("缓存命中!")
    data = cached
else:
    # 调用 API
    data = fetch_price_from_api('AAPL')
    # 保存缓存
    api_cache.set('price', {'symbol': 'AAPL'}, data)
```

## 速率限制 ⏱️

### 配置位置

`optimizer.py` 中定义：

```python
# Twelve Data: 800 次/天
twelve_data_limiter = RateLimiter(calls_per_day=800, calls_per_minute=60)

# Alpha Vantage: 25 次/天
alpha_vantage_limiter = RateLimiter(calls_per_day=25, calls_per_minute=5)
```

### 使用示例

```python
from optimizer import twelve_data_limiter

# 检查是否可以调用
can_call, msg = twelve_data_limiter.can_call()

if can_call:
    # 记录调用
    twelve_data_limiter.record_call()
    # 调用 API
    data = fetch_data()
else:
    print(f"等待：{msg}")
```

### 查看使用统计

```python
from optimizer import twelve_data_limiter

stats = twelve_data_limiter.stats()
print(f"今日调用：{stats['calls_today']}/800")
print(f"剩余：{stats['remaining_today']}")
```

## 批量处理 📦

### 数据分块

```python
from optimizer import DataBatcher

batcher = DataBatcher(batch_size=100)

# 分块列表
symbols = ['AAPL', 'GOOGL', 'TSLA'] * 50  # 150 个标的
chunks = batcher.chunk_list(symbols)

print(f"分为 {len(chunks)} 批，每批最多 100 个")
```

### 批量处理

```python
from optimizer import DataBatcher
import time

batcher = DataBatcher(batch_size=50)

def process_batch(batch):
    """处理一批数据"""
    results = []
    for symbol in batch:
        data = fetch_price(symbol)
        results.append(data)
    return results

# 批量处理
symbols = ['AAPL', 'GOOGL', 'TSLA'] * 100
for i, batch in enumerate(batcher.batch_process(symbols, process_batch, delay_seconds=1)):
    print(f"批次 {i+1} 完成，{len(batch)} 条数据")
    time.sleep(1)  # 批次间延迟
```

## 性能监控 📈

### 查看统计

```bash
python3 optimizer.py
```

**输出示例**:
```
==================================================
📊 性能优化统计
==================================================

💾 缓存:
   总条目：156
   有效：142
   过期：14
   大小：45.2 KB

📈 Twelve Data API:
   今日调用：234/800
   剩余：566
   最近 1 分钟：3/60

📉 Alpha Vantage API:
   今日调用：12/25
   剩余：13
   最近 1 分钟：1/5
==================================================
```

### 缓存命中率

```python
from optimizer import api_cache

stats = api_cache.stats()
hit_rate = (stats['valid'] / stats['total'] * 100) if stats['total'] > 0 else 0
print(f"缓存命中率：{hit_rate:.1f}%")
```

**目标**: > 60% 命中率

## 优化建议 💡

### 1. 合理设置监控间隔

```bash
# ❌ 过于频繁（会超限）
ta monitor --watchlist BTC ETH --interval 10 --run

# ✅ 合理间隔
ta monitor --watchlist BTC ETH --interval 60 --run
```

### 2. 使用缓存

```python
# ❌ 每次都调用 API
for symbol in symbols:
    price = fetch_price(symbol)

# ✅ 使用缓存
for symbol in symbols:
    price = get_cached_price(symbol) or fetch_price(symbol)
```

### 3. 批量获取数据

```python
# ❌ 逐个获取
for symbol in symbols:
    data = fetch_price(symbol)

# ✅ 批量获取（如果 API 支持）
data = fetch_prices_batch(symbols)
```

### 4. 避免重复计算

```python
# ❌ 重复计算
for i in range(100):
    result = calculate_sma(data, 20)

# ✅ 缓存结果
sma_20 = calculate_sma(data, 20)
for i in range(100):
    result = sma_20
```

## 故障排查 🔧

### 问题：API 调用失败

**检查速率限制**:
```python
from optimizer import twelve_data_limiter
print(twelve_data_limiter.stats())
```

**解决方案**:
- 等待配额重置
- 升级到付费套餐
- 增加缓存 TTL

### 问题：缓存过大

**检查缓存大小**:
```python
from optimizer import api_cache
print(api_cache.stats())
```

**解决方案**:
```python
from optimizer import api_cache
api_cache.clear()
```

### 问题：性能下降

**检查缓存命中率**:
```python
from optimizer import api_cache
stats = api_cache.stats()
print(f"命中率：{stats['valid']/stats['total']*100:.1f}%")
```

**解决方案**:
- 增加缓存 TTL
- 优化查询参数
- 减少不必要的 API 调用

## 高级配置 ⚙️

### 自定义缓存 TTL

编辑 `optimizer.py`:

```python
# 默认 5 分钟
api_cache = APICache(ttl_seconds=300)

# 改为 10 分钟
api_cache = APICache(ttl_seconds=600)
```

### 自定义速率限制

```python
# Twelve Data 付费账户
twelve_data_limiter = RateLimiter(calls_per_day=12000, calls_per_minute=120)
```

### 禁用缓存（调试用）

```bash
export TRADING_ASSISTANT_CACHE=false
```

---

## 下一步

- 📚 查看 [实时监控指南](realtime-backtest.md) 了解监控功能
- 📊 查看 [持仓成本分析](cost-analysis.md) 学习成本分析
- 🔧 查看 [CLI 参考](CLI.md) 了解所有命令
