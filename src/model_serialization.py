import pickle
import os
from pathlib import Path


def save_model(model, model_name="fake_news_model.pkl"):
    """
    Save the trained model to a pickle file.
    
    Args:
        model: The trained sklearn pipeline model
        model_name: Name of the pickle file (default: fake_news_model.pkl)
    
    Returns:
        str: Path to the saved model file
    """
    # Create models directory if it doesn't exist
    models_dir = Path("models")
    models_dir.mkdir(exist_ok=True)
    
    model_path = models_dir / model_name
    
    with open(model_path, 'wb') as f:
        pickle.dump(model, f)
    
    print(f"✓ Model saved successfully at: {model_path}")
    return str(model_path)


def load_model(model_path="models/fake_news_model.pkl"):
    """
    Load a trained model from a pickle file.
    
    Args:
        model_path: Path to the pickle file
    
    Returns:
        The loaded model
    """
    if not os.path.exists(model_path):
        raise FileNotFoundError(f"Model file not found at: {model_path}")
    
    with open(model_path, 'rb') as f:
        model = pickle.load(f)
    
    print(f"✓ Model loaded successfully from: {model_path}")
    return model


if __name__ == "__main__":
    print("Model serialization module loaded successfully!")
