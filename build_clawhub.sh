#!/bin/bash
# ClawHub 上传专用打包脚本 v2.0.0
# 创建一个干净的、只包含必要文件的版本

set -e

VERSION="2.0.0"
PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
OUTPUT_FILE="${PROJECT_DIR}/trading-assistant-v${VERSION}-clawhub.tar.gz"
TEMP_DIR=$(mktemp -d)

echo "📦 创建 ClawHub 上传包 v${VERSION}..."
echo "📁 项目目录：${PROJECT_DIR}"
echo "📄 输出文件：${OUTPUT_FILE}"
echo ""

cd "${PROJECT_DIR}"

# 使用 find + cp 复制文件
echo "📋 准备文件..."
find . -maxdepth 1 -type f -o -type d | while read item; do
  # 跳过排除的目录和文件
  case "$item" in
    .|.git|.github|__pycache__|node_modules|.pytest_cache|reports|logs|data|sent|portfolio|cache|site|daily_reports)
      continue
      ;;
    *.pyc|*.pyo|*.so|*.log|*.tar.gz|*.tgz|.env|config.json|feishu_config.json|watchlist.txt|accuracy_log.json|sentiment_report.json)
      continue
      ;;
    *screenshots*.txt|PUSH_COMPLETE.md|GITHUB_RELEASE_INSTRUCTIONS.md|create_upload_tarball.sh)
      continue
      ;;
    GITHUB_ACTIONS_SETUP.md|GITHUB_ACTIONS_MULTI_BUILD.md|BUILD_SUCCESS_v2.0.0.md)
      continue
      ;;
    RE_PUSH_COMPLETE.md|REBUILD_NOTES.md|FINAL_BUILD_NOTES.md|.DS_Store|Thumbs.db)
      continue
      ;;
    build_clawhub.sh)
      continue
      ;;
  esac
  
  if [ -e "$item" ]; then
    cp -r "$item" "${TEMP_DIR}/" 2>/dev/null || true
  fi
done

# 打包临时目录
echo "📦 打包中..."
tar -czf "${OUTPUT_FILE}" -C "${TEMP_DIR}" .

# 清理临时目录
rm -rf "${TEMP_DIR}"

echo "✅ 打包完成！"
echo ""
echo "📊 包信息:"
echo "  文件大小：$(du -h "${OUTPUT_FILE}" | cut -f1)"
echo "  文件数量：$(tar -tzf "${OUTPUT_FILE}" | wc -l)"
echo ""

echo "🔍 验证关键文件:"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

# 验证必需文件
check_file() {
  if tar -tzf "${OUTPUT_FILE}" | grep -q "^${1}$"; then
    echo "✅ $1"
  else
    echo "❌ $1 缺失!"
  fi
}

check_file "SKILL.md"
check_file "i18n.py"
check_file "locales/en.json"
check_file "locales/zh_CN.json"
check_file "README.md"
check_file "cli.py"
check_file "config.py"
check_file "requirements.txt"
check_file "pyproject.toml"
check_file "LICENSE"

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "📋 目录结构预览:"
tar -tzf "${OUTPUT_FILE}" | grep -E "^[^/]+/?$" | head -20
echo ""
echo "🎉 打包完成！文件已准备好上传到 ClawHub"
echo ""
echo "📤 上传文件：${OUTPUT_FILE}"
echo "🔗 ClawHub: https://clawhub.com/skills/trading-assistant"
echo ""
echo "💡 上传命令:"
echo "   clawhub upload ${OUTPUT_FILE}"
