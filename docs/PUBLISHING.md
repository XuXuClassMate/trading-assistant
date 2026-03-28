# 📦 Publishing Guide / 发布指南

## GitHub Packages / GitHub 包

This project is published as a Python package to GitHub Packages.

本项目作为 Python 包发布到 GitHub Packages。

---

## 🔧 Setup / 配置

### 1. Create PyPI API Token / 创建 PyPI API Token

**For GitHub Packages** (recommended):

1. Go to GitHub Settings → Developer settings → Personal access tokens → Tokens (classic)
2. Generate new token with scopes: `read:packages`, `write:packages`, `repo`
3. Copy the token

**对于 GitHub Packages**（推荐）:

1. 访问 GitHub Settings → Developer settings → Personal access tokens → Tokens (classic)
2. 创建新 token，勾选权限：`read:packages`, `write:packages`, `repo`
3. 复制 token

### 2. Add Secret to Repository / 添加密钥到仓库

1. Go to repository Settings → Secrets and variables → Actions
2. Click "New repository secret"
3. Add:
   - Name: `PYPI_API_TOKEN`
   - Value: [paste your token]

**访问仓库 Settings → Secrets and variables → Actions**
**添加密钥**:
- 名称：`PYPI_API_TOKEN`
- 值：[粘贴你的 token]

---

## 🚀 Publishing a New Version / 发布新版本

### Method 1: Create Release (Automatic) / 方法 1: 创建 Release（自动）

```bash
# 1. Update version in CHANGELOG.md
# 2. Commit changes
git add .
git commit -m "chore: Prepare release v1.1.0"
git push origin main

# 3. Create release
./scripts/release.sh 1.1.0 "New features"

# 4. GitHub Actions will automatically build and publish
#    Visit: https://github.com/XuXuClassMate/trading-assistant/actions
```

**GitHub Actions 会自动**:
1. 构建 Python 包
2. 上传到 GitHub Packages
3. 附加到 GitHub Release

---

### Method 2: Manual Trigger / 方法 2: 手动触发

1. Go to Actions → "Publish to GitHub Packages"
2. Click "Run workflow"
3. Enter version number (e.g., `1.1.0`)
4. Click "Run workflow"

**访问 Actions → "Publish to GitHub Packages"**
**点击 "Run workflow"**
**输入版本号**
**点击运行**

---

## 📥 Installation / 安装

### From GitHub Packages / 从 GitHub Packages 安装

```bash
# Create or edit ~/.pip/pip.conf
# 创建或编辑 ~/.pip/pip.conf

[global]
index-url = https://pypi.pkg.github.com/XuXuClassMate
extra-index-url = https://pypi.org/simple

# Or use command line / 或使用命令行
pip install --index-url https://pypi.pkg.github.com/XuXuClassMate openclaw-trading-assistant
```

### From PyPI (future) / 从 PyPI 安装（未来）

```bash
pip install openclaw-trading-assistant
```

### From Source / 从源码安装

```bash
git clone https://github.com/XuXuClassMate/trading-assistant.git
cd trading-assistant
pip install -e .
```

---

## 📋 Version Management / 版本管理

### Semantic Versioning / 语义化版本

Format: `MAJOR.MINOR.PATCH`

- **MAJOR**: Breaking changes (不兼容的重大更新)
- **MINOR**: New features, backward compatible (向下兼容的新功能)
- **PATCH**: Bug fixes (Bug 修复)

### Examples / 示例

```
v1.0.0 → Initial release (初始版本)
v1.0.1 → Bug fix (Bug 修复)
v1.1.0 → New feature (新功能)
v2.0.0 → Breaking changes (重大更新)
```

---

## 🔍 Verify Publication / 验证发布

### Check GitHub Packages / 检查 GitHub Packages

Visit: https://github.com/XuXuClassMate/trading-assistant/pkgs/python/openclaw-trading-assistant

### Check Release Assets / 检查 Release 资源

Visit: https://github.com/XuXuClassMate/trading-assistant/releases

You should see `.whl` and `.tar.gz` files.

**应该看到 `.whl` 和 `.tar.gz` 文件**

---

## 📝 Checklist for Each Release / 每次发布清单

- [ ] Update CHANGELOG.md with new version
- [ ] Update version in __init__.py
- [ ] Update version in pyproject.toml (or let workflow do it)
- [ ] Commit and push changes
- [ ] Create release tag
- [ ] Verify Actions workflow completed successfully
- [ ] Test installation from GitHub Packages
- [ ] Update documentation if needed

---

## 🐛 Troubleshooting / 故障排除

### Build Fails / 构建失败

```bash
# Test build locally / 本地测试构建
pip install build
python -m build

# Check for errors / 检查错误
ls -lh dist/
```

### Authentication Fails / 认证失败

1. Verify `PYPI_API_TOKEN` secret is set correctly
2. Check token has `write:packages` permission
3. Regenerate token if needed

### Package Not Found / 包未找到

```bash
# Clear pip cache / 清除 pip 缓存
pip cache purge

# Try again / 重试
pip install --index-url https://pypi.pkg.github.com/XuXuClassMate openclaw-trading-assistant
```

---

## 📚 Resources / 资源

- [GitHub Packages Documentation](https://docs.github.com/en/packages)
- [Python Packaging Guide](https://packaging.python.org/)
- [PyPI Documentation](https://pypi.org/help/)
- [Semantic Versioning](https://semver.org/)

---

*Last Updated: 2026-03-24*  
*Version: v1.0.0*
