---
hide:
  - navigation
  - toc
---

# 📈 Trading Signals Guide

**Understand how our AI generates trading signals**

---

## 🎯 Signal Generation Process

```mermaid
flowchart TD
    A[📊 Market Data] --> B{Technical Indicators}
    B --> C[RSI Analysis]
    B --> D[MACD Analysis]
    B --> E[Moving Averages]
    
    C --> F{Signal Scoring}
    D --> F
    E --> F
    
    F --> G[Combined Score]
    G --> H{Recommendation}
    
    H -->|Score 3/3| I[🟢 Strong BUY]
    H -->|Score 2/3| J[🟡 BUY]
    H -->|Score 1/3| K[⚪ HOLD]
    H -->|Score 0/3| L[🔴 SELL]
    
    style I fill:#10b981,color:#fff
    style J fill:#34d399,color:#fff
    style K fill:#9ca3af,color:#fff
    style L fill:#ef4444,color:#fff
```

---

## 📊 Indicator Breakdown

### RSI (Relative Strength Index)

```mermaid
xychart-beta
    title "RSI Interpretation"
    x-axis [0, 30, 50, 70, 100]
    y-axis "Signal Strength" 0 --> 10
    bar [1, 7, 5, 7, 1]
    line [1, 7, 5, 7, 1]
```

| RSI Range | Signal | Meaning |
|-----------|--------|---------|
| 0-30 | 🟢 Oversold | Potential BUY |
| 30-50 | 🟡 Weak | Caution |
| 50-70 | 🟡 Strong | Bullish |
| 70-100 | 🔴 Overbought | Potential SELL |

---

### MACD (Moving Average Convergence Divergence)

```mermaid
flowchart LR
    A[MACD Line] --> B{Crossover}
    B -->|Above Signal| C[🟢 Bullish]
    B -->|Below Signal| D[🔴 Bearish]
    
    C --> E[BUY Signal]
    D --> F[SELL Signal]
    
    style C fill:#10b981,color:#fff
    style D fill:#ef4444,color:#fff
```

---

## 💰 Position Sizing Algorithm

```mermaid
flowchart TD
    A[💰 Total Capital] --> B[Risk %]
    B --> C[Risk Amount]
    
    D[Entry Price] --> E[Stop Loss %]
    E --> F[Risk per Share]
    
    C --> G{Position Calc}
    F --> G
    
    G --> H[Shares to Buy]
    H --> I[Position Value]
    
    style A fill:#3b82f6,color:#fff
    style C fill:#10b981,color:#fff
    style H fill:#8b5cf6,color:#fff
```

---

## 🎓 Example Walkthrough

### Scenario: NVDA @ $175

```mermaid
sequenceDiagram
    participant User
    participant TA as Trading Assistant
    participant API as Market Data API
    participant Calc as Calculator
    
    User->>TA: ta sig --symbol NVDA
    TA->>API: Fetch OHLCV data
    API-->>TA: Price data returned
    
    TA->>Calc: Calculate RSI
    Calc-->>TA: RSI = 52.34 (Neutral)
    
    TA->>Calc: Calculate MACD
    Calc-->>TA: MACD = 0.1234 (Bullish)
    
    TA->>Calc: Check Moving Averages
    Calc-->>TA: MA50/MA200 (Bullish)
    
    TA->>TA: Combine signals
    TA-->>User: BUY (Confidence: Medium)
```

---

## 📈 Performance Metrics

```mermaid
xychart-beta
    title "Signal Accuracy (Last 30 Days)"
    x-axis ["Week 1", "Week 2", "Week 3", "Week 4"]
    y-axis "Accuracy %" 0 --> 100
    bar [68, 72, 75, 71]
    line [68, 72, 75, 71]
```

---

## 🔍 Signal Confidence Levels

<div class="grid" markdown>

<div class="feature-card" markdown>
### 🟢 High Confidence (75%+)
- All 3 indicators agree
- Strong trend confirmation
- Volume supports move

**Action**: Execute with full position
</div>

<div class="feature-card" markdown>
### 🟡 Medium Confidence (50-74%)
- 2 of 3 indicators agree
- Moderate trend strength
- Normal volume

**Action**: Execute with reduced position
</div>

<div class="feature-card" markdown>
### ⚪ Low Confidence (<50%)
- Indicators conflict
- Weak or no clear trend
- Low volume

**Action**: Wait for better setup
</div>

</div>

---

## 🎯 Best Practices

```mermaid
mindmap
  root((Trading<br/>Strategy))
    Risk Management
      Position Sizing
      Stop Loss
      Take Profit
    Technical Analysis
      Multiple Indicators
      Time Frames
      Volume
    Market Conditions
      Trending
      Ranging
      Volatility
    Psychology
      Discipline
      Patience
      Emotional Control
```

---

## 📊 Real-World Examples

### Example 1: Strong BUY Signal

```
NVDA - March 20, 2026
┌─────────────────────────────┐
│ RSI:    35.2  [Oversold] 🟢 │
│ MACD:   +0.45 [Bullish]  🟢 │
│ MA:     Above    [Bullish] 🟢 │
├─────────────────────────────┤
│ Score:  3/3                 │
│ Action: BUY                 │
│ Confidence: HIGH (85%)      │
└─────────────────────────────┘

Result: +12.5% in 5 days ✅
```

### Example 2: Caution Signal

```
TSLA - March 18, 2026
┌─────────────────────────────┐
│ RSI:    48.5  [Neutral]  ⚪ │
│ MACD:   -0.12 [Bearish]  🔴 │
│ MA:     Above    [Bullish] 🟢 │
├─────────────────────────────┤
│ Score:  1/3                 │
│ Action: HOLD                │
│ Confidence: LOW (35%)       │
└─────────────────────────────┘

Result: Sideways movement ➡️
```

---

## 🎓 Learn More

- [Getting Started](getting-started.md)
- [Risk Management](risk-management.md)
- [Advanced Strategies](advanced-strategies.md)

---

<div class="feature-card" style="text-align: center;" markdown>
### Ready to Generate Signals?

[Start Trading →](../getting-started.md){ .md-button .md-button--primary }
</div>
