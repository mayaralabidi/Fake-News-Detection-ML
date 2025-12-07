#!/usr/bin/env python3
"""
Quick test to verify both backend and frontend are configured correctly
"""

import subprocess
import time
import os
import requests
import sys

print("\n" + "="*60)
print("FAKE NEWS DETECTION - System Check")
print("="*60)

# Test 1: Check model file
print("\n1. Checking ML Model...")
if os.path.exists("models/fake_news_model.pkl"):
    print("   ✓ Model file found")
else:
    print("   ✗ Model file missing!")

# Test 2: Check backend imports
print("\n2. Checking Backend Dependencies...")
try:
    from predict import FakeNewsPredictor
    print("   ✓ predict.py working")
except Exception as e:
    print(f"   ✗ predict.py error: {e}")

# Test 3: Check if Flask is running
print("\n3. Checking Flask API...")
try:
    response = requests.get("http://localhost:5000/api/health", timeout=2)
    if response.status_code == 200:
        print("   ✓ Flask API is running and responding")
    else:
        print(f"   ✗ Flask returned status {response.status_code}")
except requests.exceptions.ConnectionError:
    print("   ⚠ Flask API not running yet (start with: python app.py)")
except Exception as e:
    print(f"   ✗ Flask error: {e}")

# Test 4: Check frontend files
print("\n4. Checking Frontend Files...")
frontend_files = [
    "frontend/app/layout.tsx",
    "frontend/app/page.tsx",
    "frontend/components/DetectorContainer.tsx",
    "frontend/components/PredictionForm.tsx",
    "frontend/components/PredictionResult.tsx",
    "frontend/components/PredictionHistory.tsx",
    "frontend/package.json",
    "frontend/tsconfig.json"
]

missing = []
for f in frontend_files:
    if os.path.exists(f):
        pass
    else:
        missing.append(f)

if not missing:
    print("   ✓ All frontend files present")
else:
    print(f"   ✗ Missing {len(missing)} files")
    for f in missing:
        print(f"      - {f}")

# Test 5: Summary
print("\n" + "="*60)
print("SETUP INSTRUCTIONS:")
print("="*60)
print("\nTerminal 1 - Start Backend:")
print("  python app.py")
print("\nTerminal 2 - Start Frontend:")
print("  cd frontend")
print("  npm install  (if not done)")
print("  npm run dev")
print("\nThen open browser:")
print("  http://localhost:3000")
print("\n" + "="*60)
