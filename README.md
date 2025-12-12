WELCOME TO OUR FIRST MACHINE LEARNING PROJECT  ヾ(＠⌒ー⌒＠)ノ

## Fake News Detection ML

Authors:
- Mayara Labidi
- Roua Khribiche

## Overview

- Fake News Detection ML is a machine learning system that classifies news articles as fake or real. It integrates:
- Data preprocessing and feature extraction
- Custom ML pipelines with Scikit-learn
- REST API for predictions
- React.js frontend with prediction history
- Deployment-ready configuration for Vercel, Railway, or Heroku
- The system is designed for easy experimentation, training, and deployment.

## Features

- Train and save ML models
- Predict news via API or CLI
- Web frontend for user interaction
- EDA and experiment notebooks included
- Deployment-ready configuration

## 🎉 What's Been Created

### 1. **Frontend (Next.js + React + TypeScript)**

- ✅ Modern, responsive UI with Tailwind CSS
- ✅ Real-time article input and prediction display
- ✅ Prediction history sidebar with 10-item tracking
- ✅ Glass morphism design with smooth animations
- ✅ Full TypeScript type safety
- ✅ Mobile-responsive layout

**Files:**

- `frontend/app/page.tsx` - Main page
- `frontend/components/DetectorContainer.tsx` - State management
- `frontend/components/PredictionForm.tsx` - Input form
- `frontend/components/PredictionResult.tsx` - Result display
- `frontend/components/PredictionHistory.tsx` - History tracking
- `frontend/globals.css` - Tailwind styles
- `frontend/tailwind.config.ts` - Configuration

### 2. **Backend API (Flask)**

- ✅ REST API with 3 endpoints
- ✅ Single and batch prediction support
- ✅ CORS enabled for frontend
- ✅ Comprehensive error handling
- ✅ Logging and monitoring
- ✅ Production-ready with Gunicorn support

**Files:**

- `app.py` - Flask API server
- `predict.py` - Prediction class
- `train_model.py` - Model training script

### 3. **Machine Learning Model**

- ✅ LinearSVC classifier
- ✅ 99.65% accuracy
- ✅ Trained on 21,417 articles
- ✅ Fast inference (<100ms)
- ✅ Serialized as pickle file

**Files:**

- `models/fake_news_model.pkl` - Trained model

### 4. **Documentation (5 Guides)**

- ✅ `QUICKSTART.md` - 5-minute setup guide
- ✅ `PRODUCTION_README.md` - Complete documentation
- ✅ `DEPLOYMENT.md` - Deployment instructions (6 platforms)
- ✅ `ARCHITECTURE.md` - Tech stack and system design
- ✅ This file - Project summary

## 🚀 Quick Start (2 Terminal Tabs)

### Terminal 1: Backend

```bash
python app.py
```

### Terminal 2: Frontend

```bash
cd frontend
npm install
npm run dev
```

### Visit

```
http://localhost:3000
```

## 📊 Tech Stack Summary

### Frontend

- **Framework**: Next.js 14 (React 18)
- **Language**: TypeScript
- **Styling**: Tailwind CSS
- **HTTP**: Axios
- **Bundler**: Next.js built-in

### Backend

- **Framework**: Flask
- **Language**: Python 3.8+
- **ML**: Scikit-learn
- **NLP**: NLTK
- **CORS**: Flask-CORS

### Model

- **Algorithm**: Linear SVC
- **Features**: TF-IDF + Bigrams
- **Accuracy**: 99.65%
- **Size**: ~50-100 MB

## 📁 Project Structure

```
Fake-News-Detection-ML/
├── frontend/                      # Next.js app
│   ├── app/
│   │   ├── layout.tsx
│   │   └── page.tsx
│   ├── components/               # React components
│   ├── globals.css               # Tailwind styles
│   ├── package.json
│   ├── next.config.js
│   └── tsconfig.json
├── app.py                        # Flask API
├── predict.py                    # Prediction logic
├── train_model.py               # Training script
├── models/
│   └── fake_news_model.pkl      # ML model
└── requirements.txt             # Python deps
```

## 📈 Performance

| Metric          | Value       |
| --------------- | ----------- |
| Frontend Bundle | ~85KB       |
| Model Loading   | 2-3 seconds |
| Prediction Time | 50-150ms    |
| Model Accuracy  | 99.65%      |
| API Response    | <200ms      |

### Model Performance

| Metric    | Value  |
| --------- | ------ |
| Accuracy  | 99.65% |
| Precision | 99.4%  |
| Recall    | 99.9%  |
| F1 Score  | 99.6%  |
