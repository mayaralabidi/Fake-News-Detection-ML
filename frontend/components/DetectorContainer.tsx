'use client'

import { useState, useCallback } from 'react'
import axios from 'axios'
import PredictionForm from './PredictionForm'
import PredictionResult from './PredictionResult'
import PredictionHistory from './PredictionHistory'

export interface Prediction {
  id: string
  text: string
  prediction: 'real' | 'fake'
  confidence: number
  timestamp: Date
}

export default function DetectorContainer() {
  const [predictions, setPredictions] = useState<Prediction[]>([])
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState<string | null>(null)
  const [currentPrediction, setCurrentPrediction] = useState<Prediction | null>(null)

  const handlePredict = useCallback(async (text: string, title?: string) => {
    if (!text.trim()) {
      setError('Please enter an article to analyze')
      return
    }

    setLoading(true)
    setError(null)

    try {
      const apiUrl = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:5000'
      const response = await axios.post(`${apiUrl}/api/predict`, {
        text: title ? `${title} ${text}` : text,
      })

      const prediction: Prediction = {
        id: Date.now().toString(),
        text: text.substring(0, 150),
        prediction: response.data.prediction.toLowerCase(),
        confidence: response.data.confidence || 0.85,
        timestamp: new Date(),
      }

      setCurrentPrediction(prediction)
      setPredictions([prediction, ...predictions.slice(0, 9)])
    } catch (err) {
      if (axios.isAxiosError(err)) {
        setError(
          err.response?.data?.error || 'Failed to connect to the prediction service. Make sure the backend is running.'
        )
      } else {
        setError('An error occurred while processing your request')
      }
    } finally {
      setLoading(false)
    }
  }, [predictions])

  const clearHistory = useCallback(() => {
    setPredictions([])
    setCurrentPrediction(null)
    setError(null)
  }, [])

  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-900 via-purple-900 to-slate-900 text-white py-8 px-4">
      <div className="max-w-6xl mx-auto">
        {/* Header */}
        <div className="text-center mb-12">
          <h1 className="text-5xl font-bold mb-4 bg-gradient-to-r from-purple-400 via-pink-400 to-purple-400 bg-clip-text text-transparent">
            🔍 Fake News Detector
          </h1>
          <p className="text-xl text-gray-300">
            AI-powered detection using Machine Learning
          </p>
        </div>

        {/* Main content grid */}
        <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
          {/* Left column - Form and Result */}
          <div className="lg:col-span-2 space-y-6">
            {/* Prediction Form */}
            <div className="glass-morphism p-8 border-purple-500/30 animate-slide-in">
              <PredictionForm 
                onPredict={handlePredict} 
                loading={loading}
              />
            </div>

            {/* Error message */}
            {error && (
              <div className="bg-red-500/10 border border-red-500/30 rounded-lg p-4 text-red-200 animate-slide-in">
                <p className="font-semibold">⚠️ Error</p>
                <p className="text-sm mt-1">{error}</p>
              </div>
            )}

            {/* Current Prediction Result */}
            {currentPrediction && !loading && (
              <div className="animate-slide-in">
                <PredictionResult prediction={currentPrediction} />
              </div>
            )}

            {/* Loading state */}
            {loading && (
              <div className="glass-morphism p-8 border-purple-500/30 flex items-center justify-center min-h-40">
                <div className="text-center">
                  <div className="inline-block">
                    <div className="w-12 h-12 border-4 border-purple-500/30 border-t-purple-400 rounded-full animate-spin"></div>
                  </div>
                  <p className="mt-4 text-gray-300">Analyzing your article...</p>
                </div>
              </div>
            )}
          </div>

          {/* Right column - History */}
          <div className="lg:col-span-1">
            <PredictionHistory 
              predictions={predictions}
              onClear={clearHistory}
            />
          </div>
        </div>

        {/* Footer */}
        <div className="mt-16 text-center text-gray-400 border-t border-purple-500/20 pt-8">
          <p className="text-sm">
            Built with Next.js • Powered by Machine Learning • Accuracy: 99.65%
          </p>
        </div>
      </div>
    </div>
  )
}
