import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline
from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score, classification_report
import sys
import os

# Add src to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.logger import logging
from src.model_serialization import save_model


def train_fake_news_model():
    """
    Train the fake news detection model and save it.
    
    Returns:
        tuple: (trained_pipeline, accuracy_score)
    """
    try:
        logging.info("Starting model training...")
        
        # Load data
        logging.info("Loading dataset...")
        real = pd.read_csv('notebook/data/True.csv')
        fake = pd.read_csv('notebook/data/Fake.csv')
        
        # Add labels
        real['label'] = 'real'
        fake['label'] = 'fake'
        
        # Combine datasets
        data = pd.concat([real, fake], ignore_index=True)
        data = data.sample(frac=1, random_state=42).reset_index(drop=True)
        
        logging.info(f"Dataset loaded: {len(data)} samples")
        
        # Prepare features and labels
        data['combined_text'] = data['title'] + " " + data['text']
        X = data['combined_text']
        y = data['label']
        
        # Split data
        logging.info("Splitting data into train and test sets...")
        X_train, X_test, y_train, y_test = train_test_split(
            X, y,
            test_size=0.2,
            random_state=23,
            stratify=y
        )
        
        logging.info(f"Training set: {len(X_train)}, Test set: {len(X_test)}")
        
        # Build and train pipeline
        logging.info("Building and training the pipeline...")
        pipeline = Pipeline([
            ('preprocessor', TfidfVectorizer(
                ngram_range=(1, 2),
                max_df=0.8,
                min_df=5
            )),
            ('classifier', LinearSVC(random_state=23, max_iter=2000))
        ])
        
        pipeline.fit(X_train, y_train)
        logging.info("✓ Pipeline trained successfully")
        
        # Evaluate model
        logging.info("Evaluating model...")
        y_pred = pipeline.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        
        logging.info(f"Model Accuracy: {accuracy:.4f}")
        logging.info(f"\nClassification Report:\n{classification_report(y_test, y_pred)}")
        
        # Save model
        logging.info("Saving trained model...")
        model_path = save_model(pipeline, "fake_news_model.pkl")
        logging.info(f"✓ Model saved at: {model_path}")
        
        return pipeline, accuracy
        
    except Exception as e:
        logging.error(f"Error during model training: {str(e)}")
        raise


if __name__ == "__main__":
    model, accuracy = train_fake_news_model()
    print(f"\n{'='*50}")
    print(f"Training Complete!")
    print(f"Model Accuracy: {accuracy:.4f}")
    print(f"{'='*50}")
