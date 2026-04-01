# 🔐 PyPI Token 获取指南

## 📍 直接链接

### 1. 访问 Token 管理页面
**https://pypi.org/manage/account/token/**

### 2. 如果没有 PyPI 账户，先注册
**https://pypi.org/account/register/**

---

## 📝 详细步骤

### 步骤 1: 登录 PyPI
1. 打开 https://pypi.org/account/login/
2. 使用以下方式之一登录:
   - 用户名 + 密码
   - **GitHub 登录** (推荐，最快)
   - Google 登录
   - 其他第三方登录

### 步骤 2: 进入 Token 管理
登录后，直接访问:
```
https://pypi.org/manage/account/token/
```

或者手动导航:
1. 点击右上角你的用户名
2. 选择 "**Account settings**"
3. 左侧菜单选择 "**API tokens**"

### 步骤 3: 创建 Token
1. 点击 "**Add API token**" 按钮

2. 填写表单:
   ```
   Token name: trading-assistant
   Scope: ○ Entire account (or specific projects)
   Validity: ● No expiration
   ```

3. 点击 "**Create token**"

### 步骤 4: 复制 Token
⚠️ **重要**: Token 只显示一次!

复制类似这样的字符串:
```
pypi-AgEIcHlwaS5vcmcCJ... (很长的一串)
```

**立即保存**到安全的地方!

---

## 🔗 快速链接汇总

| 用途 | 链接 |
|------|------|
| 创建 Token | https://pypi.org/manage/account/token/ |
| 登录 PyPI | https://pypi.org/account/login/ |
| 注册账户 | https://pypi.org/account/register/ |
| PyPI 首页 | https://pypi.org/ |
| 帮助文档 | https://pypi.org/help/#apitoken |

---

## ⚠️ 注意事项

1. **Token 只显示一次** - 复制后刷新就看不到了
2. **不要提交到 Git** - 添加到 GitHub Secrets
3. **如果泄露** - 立即撤销并重新生成
4. **永久有效** - 除非手动撤销

---

## 📋 获取后

把 token 发给我，我会:
1. 添加到 GitHub Secrets
2. 配置 PyPI 发布工作流
3. 测试发布
4. 用户就可以 `pip install trading-assistant` 了

---

**现在就去**: https://pypi.org/manage/account/token/
