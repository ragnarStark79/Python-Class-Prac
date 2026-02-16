#!/bin/bash

# Student Portfolio Quick Start Script
# This script helps you start the Flask application easily

echo "=========================================="
echo "  Student Portfolio Web Application"
echo "=========================================="
echo ""

# Check if Flask is installed
if ! python3 -c "import flask" 2>/dev/null; then
    echo "📦 Flask not found. Installing dependencies..."
    pip install -r requirements.txt
    echo ""
fi

echo "🚀 Starting Flask server..."
echo ""
echo "📱 Access the application at:"
echo "   → http://localhost:5001"
echo ""
echo "Press Ctrl+C to stop the server"
echo "=========================================="
echo ""

# Start the Flask application
python3 main.py
