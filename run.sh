#!/bin/bash
# Quick Start Installation and Run Script
# Run this to set up and start both frontend and backend

echo ""
echo "=============================================="
echo "FAKE NEWS DETECTION - Quick Start Setup"
echo "=============================================="
echo ""

# Check Python
echo "Checking Python..."
if ! command -v python &> /dev/null; then
    echo "❌ Python not found. Please install Python 3.8+"
    exit 1
fi
echo "✓ Python found: $(python --version)"
echo ""

# Check Node.js
echo "Checking Node.js..."
if ! command -v npm &> /dev/null; then
    echo "❌ Node.js/npm not found. Please install Node.js 18+"
    exit 1
fi
echo "✓ Node.js found: $(node --version)"
echo "✓ npm found: $(npm --version)"
echo ""

# Install Python dependencies
echo "Installing Python dependencies..."
pip install flask flask-cors pandas numpy scikit-learn nltk
echo "✓ Python dependencies installed"
echo ""

# Install Frontend dependencies
echo "Installing Frontend dependencies..."
cd frontend
npm install
cd ..
echo "✓ Frontend dependencies installed"
echo ""

echo "=============================================="
echo "Setup Complete! Starting servers..."
echo "=============================================="
echo ""

# Start Backend in background
echo "Starting Flask Backend (http://localhost:5000)"
python app.py &
BACKEND_PID=$!
sleep 2

# Start Frontend
echo "Starting Next.js Frontend (http://localhost:3000)"
cd frontend
npm run dev

# Kill backend when frontend stops
kill $BACKEND_PID 2>/dev/null || true
