#!/bin/bash

# Personal Website - Kaidi Zhang
# Quick Start Script

echo "🌟 Starting Kaidi Zhang's Personal Website"
echo "=================================="

# Check if uv is installed
if ! command -v uv &> /dev/null; then
    echo "❌ uv is not installed. Installing now..."
    curl -LsSf https://astral.sh/uv/install.sh | sh
    source $HOME/.local/bin/env
    echo "✅ uv installed successfully"
fi

# Sync dependencies if needed
echo "📦 Syncing dependencies..."
uv sync

# Start the development server
echo "🚀 Starting development server..."
echo "📍 Website will be available at: http://localhost:5000"
echo "🔧 Press Ctrl+C to stop the server"
echo ""

uv run python run.py dev
