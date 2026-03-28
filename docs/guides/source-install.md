# 🔧 Source Installation Guide

**Difficulty**: ⭐⭐⭐ Advanced  
**Time**: 15 minutes

---

## ✅ Prerequisites

- Python 3.11+ ([Get Python](https://www.python.org/downloads/))
- Git ([Get Git](https://git-scm.com/))
- pip (Python package manager)
- API Keys (Twelve Data, Alpha Vantage)

---

## 🚀 Quick Start

### 1. Clone Repository

```bash
git clone https://github.com/XuXuClassMate/trading-assistant.git
cd trading-assistant
```

### 2. Create Virtual Environment (Recommended)

```bash
# Create virtual environment
python3 -m venv venv

# Activate (Linux/macOS)
source venv/bin/activate

# Activate (Windows)
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Install in Development Mode

```bash
pip install -e .
```

### 5. Verify Installation

```bash
ta --version
# Output: OpenClaw Trading Assistant CLI v1.3.0
```

---

## ⚙️ Configuration

### 1. Copy Configuration Templates

```bash
cp .env.example .env
cp watchlist.txt.example watchlist.txt
```

### 2. Edit Configuration

```bash
# Edit .env with your API keys
nano .env
```

**Required API Keys**:
```env
TWELVE_DATA_API_KEY=your_key_here
ALPHA_VANTAGE_API_KEY=your_key_here
LANGUAGE=en  # or 'zh' for Chinese
```

---

## 🎯 Usage

### Interactive Mode

```bash
ta
```

### Direct Commands

```bash
# Trading signals
ta sig

# Support/Resistance
ta sr

# Position calculator
ta pos --symbol NVDA --price 175 --capital 10000

# All analysis
ta all
```

---

## 🧪 Development

### Run Tests

```bash
# Install test dependencies
pip install -r requirements-dev.txt

# Run tests
pytest
```

### Run Linter

```bash
# Install linting tools
pip install flake8 black

# Check code style
flake8 .

# Format code
black .
```

### Make Changes

1. Create feature branch:
   ```bash
   git checkout -b feature/my-feature
   ```

2. Make changes and test

3. Commit changes:
   ```bash
   git add .
   git commit -m "feat: Add my feature"
   ```

4. Push and create PR:
   ```bash
   git push origin feature/my-feature
   ```

---

## 📁 Project Structure

```
trading-assistant/
├── cli.py                    # CLI entry point
├── config.py                 # Configuration management
├── i18n.py                   # Internationalization
├── position_calculator.py    # Position sizing
├── stop_loss_alerts.py       # Alert management
├── technical_analysis.py     # Technical indicators
├── pyproject.toml            # Project metadata
├── requirements.txt          # Dependencies
├── .env.example              # Environment template
├── watchlist.txt.example     # Watchlist template
├── docs/                     # Documentation
│   ├── index.md
│   ├── CLI.md
│   └── guides/
│       ├── docker-install.md
│       ├── pip-install.md
│       ├── npm-install.md
│       └── source-install.md
└── .github/workflows/        # CI/CD workflows
    ├── docker-publish.yml
    ├── pypi-publish.yml
    ├── publish-npm.yml
    └── publish-gh.yml
```

---

## 🔄 Update from Source

```bash
# Pull latest changes
git pull origin main

# Update dependencies
pip install -r requirements.txt --upgrade

# Reinstall in development mode
pip install -e .

# Verify version
ta --version
```

---

## 🗑️ Uninstall

```bash
# Uninstall package
pip uninstall openclaw-trading-assistant

# Remove virtual environment (if created)
rm -rf venv

# Remove cloned repository
cd ..
rm -rf trading-assistant
```

---

## ❓ Troubleshooting

### Dependency Conflicts

```bash
# Upgrade pip
pip install --upgrade pip

# Clear pip cache
pip cache purge

# Reinstall dependencies
pip install -r requirements.txt --force-reinstall
```

### Import Errors

```bash
# Make sure you're in the project directory
cd trading-assistant

# Make sure virtual environment is activated
source venv/bin/activate  # Linux/macOS

# Reinstall in development mode
pip install -e .
```

### Python Version Issues

```bash
# Check Python version
python3 --version

# If < 3.11, upgrade Python
# macOS: brew install python@3.11
# Ubuntu: sudo apt install python3.11
# Windows: Download from python.org
```

---

## 📚 Next Steps

- [CLI Documentation](../CLI.md) - Learn all commands
- [Contributing Guide](../CONTRIBUTING.md) - How to contribute
- [API Documentation](api-reference.md) - Code-level documentation

---

## 🔗 Related Links

- [GitHub Repository](https://github.com/XuXuClassMate/trading-assistant)
- [Issue Tracker](https://github.com/XuXuClassMate/trading-assistant/issues)
- [Python Documentation](https://docs.python.org/)
