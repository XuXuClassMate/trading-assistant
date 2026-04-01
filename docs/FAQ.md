# ❓ FAQ - Frequently Asked Questions

---

## 🔑 API Keys

### Q: Where do I get API keys?

**A:** Both are free:

- **Twelve Data**: https://twelvedata.com/pricing (800 calls/day free)
- **Alpha Vantage**: https://www.alphavantage.co/support/#api-key (25 calls/day free)

### Q: Do I need both API keys?

**A:** Yes, the assistant uses both for redundancy and different data types:
- **Twelve Data**: Primary source for price data and technical indicators
- **Alpha Vantage**: Backup source and news data

---

## 💰 Usage

### Q: Can I use this for real trading?

**A:** This is a **decision support tool**, not financial advice. Always:
- Do your own research
- Understand the risks
- Consult with a financial advisor
- Never trade more than you can afford to lose

### Q: How often should I run analysis?

**A:** Depends on your trading style:

| Style | Frequency |
|-------|-----------|
| Day Trading | Every 15-30 min during market hours |
| Swing Trading | 1-2 times daily |
| Long-term | Weekly is sufficient |

### Q: My API calls are rate limited!

**A:** Solutions:
1. Upgrade to paid tier (Twelve Data has generous limits)
2. Reduce analysis frequency
3. Use cached data when possible
4. Rotate between multiple API keys

---

## 🐛 Troubleshooting

### Q: Permission Denied when running Docker

**A:** Run with current user:
```bash
docker run --rm -it \
  -u $(id -u):$(id -g) \
  -v $(pwd)/.env:/app/.env \
  -v $(pwd)/watchlist.txt:/app/watchlist.txt \
  xuxuclassmate/trading-assistant:latest
```

### Q: Command not found: `ta`

**A:** Make sure you're using the correct command:
```bash
# Correct
ta
ta sig
ta all

# Also works (full name)
trading-assistant
```

### Q: Volume mount issues on Windows

**A:** Use absolute paths:
```bash
docker run --rm -it \
  -v C:/path/to/.env:/app/.env \
  -v C:/path/to/watchlist.txt:/app/watchlist.txt \
  xuxuclassmate/trading-assistant:latest
```

### Q: No data returned for my stock

**A:** Check:
1. Stock symbol is correct (e.g., `AAPL` not `Apple`)
2. Market is open (US stocks trade 9:30 AM - 4:00 PM ET)
3. API keys are valid and not rate limited
4. Stock is in your `watchlist.txt`

---

## 📦 Installation

### Q: Which installation method should I use?

**A:** **Docker** is recommended for most users:
- ✅ No dependency conflicts
- ✅ Works on any platform
- ✅ Easy to update
- ✅ Isolated environment

Choose based on your needs:

| Method | Best For | Time |
|--------|----------|------|
| Docker | Most users | 5 min |
| pip | Python developers | 10 min |
| npm | Node.js developers | 10 min |
| Source | Contributors | 15 min |

### Q: How do I update to the latest version?

**Docker**:
```bash
docker pull xuxuclassmate/trading-assistant:latest
docker stop trading-assistant
docker rm trading-assistant
# Re-run with same command
```

**pip**:
```bash
pip install --upgrade trading-assistant
```

**npm**:
```bash
npm update -g @xuxuclassmate/trading-assistant
```

---

## 🔒 Security

### Q: Is my API key safe?

**A:** Yes:
- ✅ Keys stored locally in `.env`
- ✅ Never sent to external servers (except API providers)
- ✅ Not committed to git (`.env` is in `.gitignore`)
- ✅ Open source code - you can verify

### Q: Can I use environment variables instead of `.env`?

**A:** Yes:
```bash
export TWELVE_DATA_API_KEY=your_key
export ALPHA_VANTAGE_API_KEY=your_key
ta
```

---

## 🌐 Language

### Q: How do I change the language?

**A:** Edit `.env`:
```env
LANGUAGE=en  # English
# or
LANGUAGE=zh  # Chinese
```

### Q: Can I contribute translations?

**A:** Yes! Please submit a PR on GitHub with translations for your language.

---

## 📞 Support

### Q: I found a bug!

**A:** Please report it: https://github.com/XuXuClassMate/trading-assistant/issues

Include:
- What you were trying to do
- What happened
- What you expected
- Error messages (if any)
- Your environment (OS, Python version, etc.)

### Q: I have a feature request!

**A:** Great! Open a discussion: https://github.com/XuXuClassMate/trading-assistant/discussions

### Q: I want to contribute!

**A:** Awesome! Check out:
- [Contributing Guide](https://github.com/XuXuClassMate/trading-assistant/blob/main/CONTRIBUTING.md)
- [Good First Issues](https://github.com/XuXuClassMate/trading-assistant/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22)

---

## 💬 Still Have Questions?

- 📚 [Documentation](https://xuxuclassmate.github.io/trading-assistant/)
- 💬 [Discussions](https://github.com/XuXuClassMate/trading-assistant/discussions)
- 🐛 [Issues](https://github.com/XuXuClassMate/trading-assistant/issues)
- 📧 [Contact](https://github.com/XuXuClassMate)

---

<div align="center">

**Made with ❤️ by XuXuClassMate**

[Back to Home →](index.md)

</div>
