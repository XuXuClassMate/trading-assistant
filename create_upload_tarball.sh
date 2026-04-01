#!/bin/bash
# Create clean tarball for ClawHub upload
# Usage: ./create_upload_tarball.sh

set -e

VERSION="2.0.1"
PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
OUTPUT_FILE="${PROJECT_DIR}/trading-assistant-v${VERSION}-security.tar.gz"

echo "📦 Creating trading-assistant v${VERSION} tarball..."
echo "📁 Project directory: ${PROJECT_DIR}"
echo "📄 Output file: ${OUTPUT_FILE}"

cd "${PROJECT_DIR}"

# Create tarball excluding unnecessary files
tar -czf "${OUTPUT_FILE}" \
  --exclude='*.tar.gz' \
  --exclude='*.tgz' \
  --exclude='node_modules' \
  --exclude='.git' \
  --exclude='__pycache__' \
  --exclude='*.pyc' \
  --exclude='reports/*' \
  --exclude='logs/*' \
  --exclude='data/*' \
  --exclude='sent/*' \
  --exclude='portfolio/*' \
  --exclude='cache/*' \
  --exclude='.env' \
  --exclude='config.json' \
  --exclude='feishu_config.json' \
  --exclude='watchlist.txt' \
  --exclude='accuracy_log.json' \
  --exclude='sentiment_report.json' \
  --exclude='*.log' \
  --exclude='.pytest_cache' \
  --exclude='site/*' \
  --exclude='daily_reports/*' \
  --exclude='screenshots_*.txt' \
  .

echo "✅ Tarball created successfully!"
echo "📦 File size: $(du -h "${OUTPUT_FILE}" | cut -f1)"
echo "📋 Contents preview:"
tar -tzf "${OUTPUT_FILE}" | head -20
echo "..."
echo "📊 Total files: $(tar -tzf "${OUTPUT_FILE}" | wc -l)"

echo ""
echo "🚀 Ready for upload to ClawHub!"
echo "📝 Don't forget to update:"
echo "   - Version: ${VERSION}"
echo "   - Changelog: SECURITY_FIXES_v2.0.1.md"
echo "   - Security summary: SECURITY_FIX_SUMMARY.md"
