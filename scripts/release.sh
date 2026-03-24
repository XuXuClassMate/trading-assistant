#!/bin/bash
# Release Script / 发布脚本
# Usage: ./release.sh <version> [message]
# 用法：./release.sh <版本号> [发布说明]

set -e

# Colors / 颜色
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Functions / 函数
print_info() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

print_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Check arguments / 检查参数
if [ -z "$1" ]; then
    print_error "Usage: ./release.sh <version> [message]"
    print_error "用法：./release.sh <版本号> [发布说明]"
    echo ""
    echo "Example / 示例:"
    echo "  ./release.sh 1.0.0"
    echo "  ./release.sh 1.0.0 \"Initial release / 初始版本\""
    exit 1
fi

VERSION=$1
MESSAGE=${2:-"Release v$VERSION"}

# Check if on main branch / 检查是否在 main 分支
CURRENT_BRANCH=$(git rev-parse --abbrev-ref HEAD)
if [ "$CURRENT_BRANCH" != "main" ]; then
    print_warning "Not on main branch. Current: $CURRENT_BRANCH"
    read -p "Continue? / 继续？(y/n): " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        exit 1
    fi
fi

# Check for uncommitted changes / 检查未提交的更改
if [ -n "$(git status --porcelain)" ]; then
    print_warning "You have uncommitted changes / 你有未提交的更改"
    git status
    read -p "Continue? / 继续？(y/n): " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        exit 1
    fi
fi

print_info "Creating release v$VERSION..."
print_info "创建发布版本 v$VERSION..."

# Update CHANGELOG.md if needed / 更新 CHANGELOG.md
if ! grep -q "## \[$VERSION\]" CHANGELOG.md; then
    print_warning "CHANGELOG.md doesn't have entry for v$VERSION"
    print_warning "CHANGELOG.md 中没有 v$VERSION 的记录"
fi

# Create tag / 创建标签
git tag -a "v$VERSION" -m "$MESSAGE"

print_success "Tag v$VERSION created / 标签已创建"

# Push to GitHub / 推送到 GitHub
print_info "Pushing to GitHub / 推送到 GitHub..."
git push origin "v$VERSION"

print_success "Release v$VERSION pushed to GitHub / 发布已推送"

# Create GitHub Release (requires GitHub CLI) / 创建 GitHub Release (需要 GitHub CLI)
if command -v gh &> /dev/null; then
    print_info "Creating GitHub release / 创建 GitHub Release..."
    gh release create "v$VERSION" \
        --title "Release v$VERSION" \
        --notes "$MESSAGE" \
        --generate-notes
    
    print_success "GitHub release created / GitHub Release 已创建"
    print_info "Release URL: https://github.com/XuXuClassMate/trading-assistant/releases/tag/v$VERSION"
else
    print_warning "GitHub CLI not found. Please create release manually:"
    print_warning "未找到 GitHub CLI。请手动创建发布："
    print_info "https://github.com/XuXuClassMate/trading-assistant/releases/new"
    print_info "Tag: v$VERSION"
    print_info "Title: Release v$VERSION"
fi

print_success "Release process completed! / 发布流程完成！"
echo ""
print_info "Next steps / 下一步:"
print_info "1. Update README.md version number / 更新 README.md 版本号"
print_info "2. Update CHANGELOG.md with changes / 更新 CHANGELOG.md"
print_info "3. Announce release to users / 通知用户新版本发布"
