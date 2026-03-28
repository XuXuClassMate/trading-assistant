# 🔑 API 密钥设置

## 需要的 API 密钥

交易助手使用两个免费的 API 服务：

### Twelve Data（主要）
- **网址**: https://twelvedata.com/pricing
- **免费额度**: 每天 800 次调用
- **用途**: 价格数据、技术指标

### Alpha Vantage（备用）
- **网址**: https://www.alphavantage.co/support/#api-key
- **免费额度**: 每天 25 次调用
- **用途**: 备用数据、新闻

## 配置方法

在工作目录创建 `.env` 文件：

```bash
TWELVE_DATA_API_KEY=你的_twelve_data_密钥
ALPHA_VANTAGE_API_KEY=你的_alpha_vantage_密钥
```

## 验证密钥

测试 API 密钥是否有效：

```bash
ta verify
```

## 了解更多

- [安装指南](install-overview.md)
- [入门指南](getting-started.md)
