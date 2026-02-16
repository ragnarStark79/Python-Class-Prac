#!/bin/bash

# Student Portfolio - Production Mode
# Starts the Flask server on port 80 for custom domain access

echo "=========================================="
echo "  Student Portfolio - Production Mode"
echo "=========================================="
echo ""

# Check if Flask is installed
if ! python3 -c "import flask" 2>/dev/null; then
    echo "📦 Flask not found. Installing dependencies..."
    pip3 install -r requirements.txt
    echo ""
fi

echo "🚀 Starting Flask server on port 80..."
echo ""
echo "📱 Access the application at:"
echo "   → http://portfolio.com"
echo "   → http://172.28.10.63"
echo "   → http://localhost"
echo ""
echo "⚠️  Running on port 80 requires sudo privileges"
echo "Press Ctrl+C to stop the server"
echo "=========================================="
echo ""

# Start the Flask application in production mode (port 80)
python3 main.py --production
