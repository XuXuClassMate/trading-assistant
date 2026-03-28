# 🔑 API Keys Setup

## Required API Keys

The Trading Assistant uses two free API services:

### Twelve Data (Primary)
- **URL**: https://twelvedata.com/pricing
- **Free Tier**: 800 calls/day
- **Used for**: Price data, technical indicators

### Alpha Vantage (Backup)
- **URL**: https://www.alphavantage.co/support/#api-key
- **Free Tier**: 25 calls/day
- **Used for**: Backup data, news

## Configuration

Create a `.env` file in your working directory:

```bash
TWELVE_DATA_API_KEY=your_twelve_data_key
ALPHA_VANTAGE_API_KEY=your_alpha_vantage_key
```

## Verification

Test your API keys:

```bash
ta verify
```

## Learn More

- [Installation Guide](install-overview.md)
- [Getting Started](getting-started.md)
