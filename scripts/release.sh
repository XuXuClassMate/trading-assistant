#!/bin/bash
# Release Script
# Usage: ./release.sh <version> [message]

set -e

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

print_info() { echo -e "${BLUE}[INFO]${NC} $1"; }
print_success() { echo -e "${GREEN}[SUCCESS]${NC} $1"; }
print_warning() { echo -e "${YELLOW}[WARNING]${NC} $1"; }
print_error() { echo -e "${RED}[ERROR]${NC} $1"; }

if [ -z "$1" ]; then
    print_error "Usage: ./release.sh <version> [message]"
    echo "Example: ./release.sh 1.0.0 'Initial release'"
    exit 1
fi

VERSION=$1
MESSAGE=${2:-"Release v$VERSION"}

CURRENT_BRANCH=$(git rev-parse --abbrev-ref HEAD)
if [ "$CURRENT_BRANCH" != "main" ]; then
    print_warning "Not on main branch: $CURRENT_BRANCH"
    read -p "Continue? (y/n): " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        exit 1
    fi
fi

if [ -n "$(git status --porcelain)" ]; then
    print_warning "Uncommitted changes detected"
    git status --short
    read -p "Continue? (y/n): " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        exit 1
    fi
fi

print_info "Creating release v$VERSION..."
git tag -a "v$VERSION" -m "$MESSAGE"
print_success "Tag v$VERSION created"

print_info "Pushing to GitHub..."
git push origin "v$VERSION"
print_success "Release v$VERSION pushed"

if command -v gh &> /dev/null; then
    print_info "Creating GitHub release..."
    gh release create "v$VERSION" --title "Release v$VERSION" --notes "$MESSAGE" --generate-notes
    print_success "GitHub release created"
    print_info "URL: https://github.com/XuXuClassMate/trading-assistant/releases/tag/v$VERSION"
else
    print_warning "GitHub CLI not found. Create release manually:"
    print_info "https://github.com/XuXuClassMate/trading-assistant/releases/new"
fi

print_success "Release completed!"
