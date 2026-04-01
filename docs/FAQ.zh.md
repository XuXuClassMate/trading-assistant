# ❓ 常见问题解答

---

## 🔑 API 密钥

### 问：在哪里获取 API 密钥？

**答：** 两者都是免费的：

- **Twelve Data**: https://twelvedata.com/pricing（免费 800 次/天）
- **Alpha Vantage**: https://www.alphavantage.co/support/#api-key（免费 25 次/天）

### 问：我需要两个 API 密钥吗？

**答：** 是的，交易助手使用两者以保证冗余和不同数据类型：
- **Twelve Data**: 价格和指标的主要数据源
- **Alpha Vantage**: 备用数据源和新闻数据

---

## 💰 使用

### 问：我可以将这个用于真实交易吗？

**答：** 这是一个**决策支持工具**，不是财务建议。务必：
- 做你自己的研究
- 了解风险
- 咨询理财顾问
- 永远不要交易超过你能承受损失的金额

### 问：我应该多久运行一次分析？

**答：** 取决于你的交易风格：

| 风格 | 频率 |
|------|------|
| 日内交易 | 市场时间内每 15-30 分钟 |
| 波段交易 | 每天 1-2 次 |
| 长期投资 | 每周即可 |

### 问：我的 API 调用被速率限制了！

**答：** 解决方案：
1. 升级到付费计划（Twelve Data 有慷慨的限额）
2. 降低分析频率
3. 尽可能使用缓存数据
4. 在多个 API 密钥之间轮换

---

## 🐛 故障排除

### 问：运行 Docker 时出现权限拒绝

**答：** 使用当前用户运行：
```bash
docker run --rm -it \
  -u $(id -u):$(id -g) \
  -v $(pwd)/.env:/app/.env \
  -v $(pwd)/watchlist.txt:/app/watchlist.txt \
  xuxuclassmate/trading-assistant:latest
```

### 问：找不到命令：`ta`

**答：** 确保使用正确的命令：
```bash
# 正确
ta
ta sig
ta all

# 也可以使用（全名）
trading-assistant
```

### 问：Windows 上的卷挂载问题

**答：** 使用绝对路径：
```bash
docker run --rm -it \
  -v C:/path/to/.env:/app/.env \
  -v C:/path/to/watchlist.txt:/app/watchlist.txt \
  xuxuclassmate/trading-assistant:latest
```

### 问：我的股票没有返回数据

**答：** 检查：
1. 股票代码正确（例如 `AAPL` 不是 `Apple`）
2. 市场开放（美股交易时间：美东时间上午 9:30 - 下午 4:00）
3. API 密钥有效且未被速率限制
4. 股票在你的 `watchlist.txt` 中

---

## 📦 安装

### 问：我应该使用哪种安装方法？

**答：** **Docker** 推荐给大多数用户：
- ✅ 无依赖冲突
- ✅ 适用于任何平台
- ✅ 易于更新
- ✅ 隔离环境

根据你的需求选择：

| 方法 | 最适合 | 时间 |
|------|--------|------|
| Docker | 大多数用户 | 5 分钟 |
| pip | Python 开发者 | 10 分钟 |
| npm | Node.js 开发者 | 10 分钟 |
| 源码 | 贡献者 | 15 分钟 |

### 问：如何更新到最新版本？

**Docker**：
```bash
docker pull xuxuclassmate/trading-assistant:latest
docker stop trading-assistant
docker rm trading-assistant
# 使用相同命令重新运行
```

**pip**：
```bash
pip install --upgrade trading-assistant
```

**npm**：
```bash
npm update -g @xuxuclassmate/trading-assistant
```

---

## 🔒 安全

### 问：我的 API 密钥安全吗？

**答：** 是的：
- ✅ 密钥本地存储在 `.env` 中
- ✅ 从不发送到外部服务器（API 提供商除外）
- ✅ 不提交到 git（`.env` 在 `.gitignore` 中）
- ✅ 开源代码 - 你可以验证

### 问：我可以使用环境变量而不是 `.env` 吗？

**答：** 可以：
```bash
export TWELVE_DATA_API_KEY=your_key
export ALPHA_VANTAGE_API_KEY=your_key
ta
```

---

## 🌐 语言

### 问：如何更改语言？

**答：** 编辑 `.env`：
```env
LANGUAGE=en  # 英语
# 或
LANGUAGE=zh  # 中文
```

### 问：我可以贡献翻译吗？

**答：** 可以！请在 GitHub 上提交包含你语言翻译的 PR。

---

## 📞 支持

### 问：我发现了一个 Bug！

**答：** 请报告：https://github.com/XuXuClassMate/trading-assistant/issues

包括：
- 你试图做什么
- 发生了什么
- 你期望什么
- 错误消息（如果有）
- 你的环境（操作系统、Python 版本等）

### 问：我有一个功能请求！

**答：** 太好了！开启一个讨论：https://github.com/XuXuClassMate/trading-assistant/discussions

### 问：我想贡献！

**答：** 太棒了！查看：
- [贡献指南](https://github.com/XuXuClassMate/trading-assistant/blob/main/CONTRIBUTING.md)
- [适合新手的 Issue](https://github.com/XuXuClassMate/trading-assistant/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22)

---

## 💬 还有问题？

- 📚 [文档](https://xuxuclassmate.github.io/trading-assistant/)
- 💬 [讨论](https://github.com/XuXuClassMate/trading-assistant/discussions)
- 🐛 [Issues](https://github.com/XuXuClassMate/trading-assistant/issues)
- 📧 [联系](https://github.com/XuXuClassMate)

---

<div align="center">

**Made with ❤️ by XuXuClassMate**

[返回主页 →](index.zh.md)

</div>
