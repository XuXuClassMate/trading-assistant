# 🔑 npm Token 获取指南

## 步骤 1: 注册 npm 账号

1. 访问 https://www.npmjs.com/signup
2. 填写用户名、邮箱、密码
3. 验证邮箱

## 步骤 2: 登录 npm

```bash
npm login
```

输入用户名、密码、邮箱

## 步骤 3: 创建 Access Token

1. 访问 https://www.npmjs.com/settings/YOUR_USERNAME/tokens
2. 点击 "Generate New Token"
3. 选择 "Automation" 类型 (推荐)
4. 复制生成的 token (以 `npm_` 开头)

## 步骤 4: 添加到 GitHub Secrets

1. 访问 https://github.com/XuXuClassMate/trading-assistant/settings/secrets/actions
2. 点击 "New repository secret"
3. 添加:
   - Name: `NPM_TOKEN`
   - Value: `npm_xxxxxxxxxxxxxxxxxxxx`
4. 点击 "Add secret"

## 步骤 5: 验证 Token

```bash
# 测试 token 是否有效
npm whoami
```

## 注意事项

- ✅ Token 是敏感信息，不要分享到公开场合
- ✅ 使用 Automation token (只读权限)
- ✅ 如果 token 泄露，立即撤销并重新生成
- ✅ Token 永不过期 (除非手动撤销)

## 手动发布 (可选)

如果不想用 GitHub Actions，可以手动发布:

```bash
cd /home/node/.openclaw/workspace/skills/trading-assistant

# 登录
npm login

# 发布
npm publish --access public

# 验证
npm view @xuxuclassmate/openclaw-trading-assistant
```
