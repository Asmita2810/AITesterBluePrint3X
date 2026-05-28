#!/bin/bash
# setup.sh - Initialize REST Assured Python framework

echo "🚀 Setting up REST Assured Python Framework..."

# Create directories
mkdir -p src/config
mkdir -p src/assertions
mkdir -p src/data
mkdir -p src/endpoints
mkdir -p tests
mkdir -p logs
mkdir -p reports

echo "📁 Project structure created"

# Install dependencies
echo "📦 Installing Python dependencies..."
pip install -r requirements.txt

echo "✅ Installation complete!"
echo ""
echo "Next steps:"
echo "1. Configure .env file (if needed)"
echo "2. Run: pytest -v"
echo "3. Check logs in logs/ directory"
echo "4. View report in reports/report.html"
echo ""
