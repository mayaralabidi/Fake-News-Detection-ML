#!/usr/bin/env python3
"""
Test script to verify the Flask API is working correctly.
Run this after starting the Flask server.
"""

import requests
import json
import sys

API_URL = "http://localhost:5000"

def test_health():
    """Test health endpoint"""
    print("\n" + "="*60)
    print("Testing: GET /api/health")
    print("="*60)
    
    try:
        response = requests.get(f"{API_URL}/api/health")
        print(f"Status Code: {response.status_code}")
        print(f"Response: {json.dumps(response.json(), indent=2)}")
        assert response.status_code == 200
        assert response.json()["status"] == "healthy"
        print("✅ PASSED")
        return True
    except Exception as e:
        print(f"❌ FAILED: {str(e)}")
        return False


def test_single_prediction():
    """Test single prediction endpoint"""
    print("\n" + "="*60)
    print("Testing: POST /api/predict")
    print("="*60)
    
    test_texts = [
        {
            "text": "Breaking news: Scientists discover breakthrough in renewable energy technology.",
            "expected": "real"
        },
        {
            "text": "NASA secretly admitted that the Moon landing was faked.",
            "expected": "fake"
        }
    ]
    
    results = []
    for test in test_texts:
        try:
            print(f"\nTesting: {test['text'][:60]}...")
            response = requests.post(
                f"{API_URL}/api/predict",
                json={"text": test["text"]},
                headers={"Content-Type": "application/json"}
            )
            
            print(f"Status Code: {response.status_code}")
            data = response.json()
            print(f"Prediction: {data['prediction']}")
            print(f"Confidence: {data['confidence']:.4f}")
            
            assert response.status_code == 200
            assert "prediction" in data
            assert data["prediction"] in ["real", "fake"]
            assert 0 <= data["confidence"] <= 1
            
            print("✅ PASSED")
            results.append(True)
        except Exception as e:
            print(f"❌ FAILED: {str(e)}")
            results.append(False)
    
    return all(results)


def test_batch_prediction():
    """Test batch prediction endpoint"""
    print("\n" + "="*60)
    print("Testing: POST /api/batch-predict")
    print("="*60)
    
    try:
        texts = [
            "Real news about economic growth",
            "Fake alien invasion story",
            "Government announces new policy"
        ]
        
        response = requests.post(
            f"{API_URL}/api/batch-predict",
            json={"texts": texts},
            headers={"Content-Type": "application/json"}
        )
        
        print(f"Status Code: {response.status_code}")
        data = response.json()
        print(f"Number of predictions: {data['count']}")
        
        for i, pred in enumerate(data['predictions']):
            print(f"  {i+1}. {pred['prediction'].upper()} (confidence: {pred['confidence']:.4f})")
        
        assert response.status_code == 200
        assert data["count"] == len(texts)
        assert len(data["predictions"]) == len(texts)
        
        print("✅ PASSED")
        return True
    except Exception as e:
        print(f"❌ FAILED: {str(e)}")
        return False


def test_error_handling():
    """Test error handling"""
    print("\n" + "="*60)
    print("Testing: Error Handling")
    print("="*60)
    
    tests_passed = 0
    
    # Test empty text
    try:
        print("\nTest 1: Empty text")
        response = requests.post(
            f"{API_URL}/api/predict",
            json={"text": ""},
            headers={"Content-Type": "application/json"}
        )
        assert response.status_code == 400
        print("✅ PASSED - Correctly rejected empty text")
        tests_passed += 1
    except Exception as e:
        print(f"❌ FAILED: {str(e)}")
    
    # Test missing text field
    try:
        print("\nTest 2: Missing text field")
        response = requests.post(
            f"{API_URL}/api/predict",
            json={},
            headers={"Content-Type": "application/json"}
        )
        assert response.status_code == 400
        print("✅ PASSED - Correctly rejected missing field")
        tests_passed += 1
    except Exception as e:
        print(f"❌ FAILED: {str(e)}")
    
    # Test invalid JSON
    try:
        print("\nTest 3: Invalid JSON")
        response = requests.post(
            f"{API_URL}/api/predict",
            data="invalid json",
            headers={"Content-Type": "application/json"}
        )
        assert response.status_code in [400, 500]
        print("✅ PASSED - Correctly rejected invalid JSON")
        tests_passed += 1
    except Exception as e:
        print(f"❌ FAILED: {str(e)}")
    
    return tests_passed == 3


def main():
    """Run all tests"""
    print("\n" + "="*60)
    print("FAKE NEWS DETECTION API - TEST SUITE")
    print("="*60)
    print(f"\nTesting API at: {API_URL}")
    print("Make sure Flask server is running!")
    
    results = {
        "Health Check": test_health(),
        "Single Prediction": test_single_prediction(),
        "Batch Prediction": test_batch_prediction(),
        "Error Handling": test_error_handling(),
    }
    
    print("\n" + "="*60)
    print("TEST SUMMARY")
    print("="*60)
    
    for test_name, passed in results.items():
        status = "✅ PASSED" if passed else "❌ FAILED"
        print(f"{test_name}: {status}")
    
    total = len(results)
    passed = sum(results.values())
    
    print(f"\nTotal: {passed}/{total} test groups passed")
    
    if passed == total:
        print("\n🎉 All tests passed! API is working correctly.")
        return 0
    else:
        print("\n⚠️  Some tests failed. Check the output above.")
        return 1


if __name__ == "__main__":
    try:
        sys.exit(main())
    except requests.exceptions.ConnectionError:
        print("\n" + "="*60)
        print("❌ ERROR: Cannot connect to Flask API")
        print("="*60)
        print(f"\nMake sure Flask server is running at {API_URL}")
        print("Run: python app.py")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Unexpected error: {str(e)}")
        sys.exit(1)
