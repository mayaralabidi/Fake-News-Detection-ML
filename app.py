from flask import Flask, request, jsonify
from flask_cors import CORS
import sys
import os
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from predict import FakeNewsPredictor
from src.logger import logging

app = Flask(__name__)

# Configure CORS with explicit origins
# For deployment, allow CORS on API endpoints. Use a permissive policy here
# to ensure browser preflight requests receive proper headers. For stricter
# security, replace "*" with a specific origin or a validated origin echo.
CORS(app, resources={r"/api/*": {"origins": "*"}}, supports_credentials=False)


@app.after_request
def add_cors_headers(response):
    # Ensure CORS headers exist on every API response (helps with OPTIONS preflight)
    response.headers.setdefault('Access-Control-Allow-Origin', '*')
    response.headers.setdefault('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
    response.headers.setdefault('Access-Control-Allow-Headers', 'Content-Type, Authorization')
    return response

# Initialize the predictor
try:
    predictor = FakeNewsPredictor()
    logging.info("✓ Flask API initialized successfully")
except Exception as e:
    logging.error(f"Failed to initialize predictor: {str(e)}")
    raise


@app.route('/api/health', methods=['GET'])
def health():
    """Health check endpoint"""
    return jsonify({'status': 'healthy', 'message': 'API is running'})


@app.route('/api/predict', methods=['POST'])
def predict():
    """
    Predict if the provided text is real or fake news.
    
    Expected JSON:
    {
        "text": "article text here"
    }
    """
    try:
        data = request.get_json()
        
        if not data or 'text' not in data:
            return jsonify({'error': 'Missing "text" in request body'}), 400
        
        text = data['text'].strip()
        
        if not text:
            return jsonify({'error': 'Text cannot be empty'}), 400
        
        # Make prediction
        result = predictor.predict(text)
        
        response = {
            'prediction': result['prediction'],
            'is_real': result['is_real'],
            'confidence': result['confidence'],
            'text_preview': result['text']
        }
        
        logging.info(f"Prediction made: {result['prediction']}")
        return jsonify(response), 200
        
    except Exception as e:
        logging.error(f"Error during prediction: {str(e)}")
        return jsonify({'error': 'Internal server error'}), 500


@app.route('/api/batch-predict', methods=['POST'])
def batch_predict():
    """
    Predict on multiple texts at once.
    
    Expected JSON:
    {
        "texts": ["text1", "text2", ...]
    }
    """
    try:
        data = request.get_json()
        
        if not data or 'texts' not in data:
            return jsonify({'error': 'Missing "texts" in request body'}), 400
        
        texts = data['texts']
        
        if not isinstance(texts, list):
            return jsonify({'error': '"texts" must be a list'}), 400
        
        if len(texts) > 100:
            return jsonify({'error': 'Maximum 100 texts per request'}), 400
        
        # Make predictions
        results = predictor.predict_batch(texts)
        
        response = {
            'predictions': [
                {
                    'prediction': r['prediction'],
                    'is_real': r['is_real'],
                    'confidence': r['confidence']
                }
                for r in results
            ],
            'count': len(results)
        }
        
        logging.info(f"Batch prediction made for {len(results)} texts")
        return jsonify(response), 200
        
    except Exception as e:
        logging.error(f"Error during batch prediction: {str(e)}")
        return jsonify({'error': 'Internal server error'}), 500


@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Endpoint not found'}), 404


@app.errorhandler(500)
def internal_error(error):
    logging.error(f"Internal server error: {str(error)}")
    return jsonify({'error': 'Internal server error'}), 500


if __name__ == '__main__':
    print("\n" + "="*60)
    print("FAKE NEWS DETECTION API - Starting")
    print("="*60)
    print("🚀 API Server running at http://localhost:5000")
    print("\nAvailable endpoints:")
    print("  GET  /api/health          - Health check")
    print("  POST /api/predict         - Single prediction")
    print("  POST /api/batch-predict   - Batch predictions")
    print("\n" + "="*60)
    
    # Get port from environment variable (for cloud deployment) or default to 5000
    port = int(os.getenv("PORT", 5000))
    
    app.run(
        host='0.0.0.0',
        port=port,
        debug=False,
        use_reloader=False
    )
