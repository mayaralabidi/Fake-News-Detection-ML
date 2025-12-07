import sys
import os

# Add src to path for imports
sys.path.insert(0, os.path.dirname(__file__))

from src.model_serialization import load_model
from src.logger import logging


class FakeNewsPredictor:
    """
    Wrapper class for making predictions on news articles.
    """
    
    def __init__(self, model_path="models/fake_news_model.pkl"):
        """
        Initialize the predictor with a trained model.
        
        Args:
            model_path: Path to the saved model pickle file
        """
        try:
            self.model = load_model(model_path)
            logging.info("✓ Predictor initialized successfully")
        except FileNotFoundError as e:
            logging.error(f"Model not found: {e}")
            raise
    
    def predict(self, text):
        """
        Predict if the given text is real or fake news.
        
        Args:
            text: String containing the news article
        
        Returns:
            dict: Prediction result with label and confidence info
        """
        try:
            prediction = self.model.predict([text])[0]
            
            # Get decision function score for confidence
            try:
                decision_score = self.model.decision_function([text])[0]
                confidence = abs(decision_score)
            except:
                confidence = None
            
            result = {
                'text': text[:100] + "..." if len(text) > 100 else text,
                'prediction': prediction,
                'is_real': prediction == 'real',
                'confidence': confidence
            }
            
            logging.info(f"Prediction made: {prediction}")
            return result
            
        except Exception as e:
            logging.error(f"Error during prediction: {str(e)}")
            raise
    
    def predict_batch(self, texts):
        """
        Make predictions on multiple texts.
        
        Args:
            texts: List of text strings
        
        Returns:
            list: List of prediction results
        """
        results = []
        for text in texts:
            results.append(self.predict(text))
        return results


if __name__ == "__main__":
    # Example usage
    try:
        predictor = FakeNewsPredictor()
        
        sample_texts = [
            "Authorities in Nigeria are increasing efforts to tackle investment scams, especially those involving crypto platforms.",
            "NASA secretly admitted that the Moon landing was faked and astronauts never left Earth.",
            "The government successfully passed a new education reform bill today, aiming to improve access to schools."
        ]
        
        print("\n" + "="*70)
        print("FAKE NEWS DETECTION PREDICTIONS")
        print("="*70)
        
        for i, text in enumerate(sample_texts, 1):
            result = predictor.predict(text)
            label = "✓ REAL" if result['is_real'] else "✗ FAKE"
            print(f"\n{i}. {label}")
            print(f"   Text: {result['text']}")
            if result['confidence']:
                print(f"   Confidence: {result['confidence']:.4f}")
        
        print("\n" + "="*70)
        
    except Exception as e:
        print(f"Error: {e}")
