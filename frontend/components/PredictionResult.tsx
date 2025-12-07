'use client'

import { Prediction } from './DetectorContainer'

interface PredictionResultProps {
  prediction: Prediction
}

export default function PredictionResult({ prediction }: PredictionResultProps) {
  const isReal = prediction.prediction === 'real'
  const iconEmoji = isReal ? '✅' : '⚠️'
  const label = isReal ? 'REAL NEWS' : 'FAKE NEWS'
  const badgeClass = isReal ? 'badge-real' : 'badge-fake'
  const bgClass = isReal 
    ? 'from-green-500/10 to-emerald-500/10 border-green-500/30'
    : 'from-red-500/10 to-rose-500/10 border-red-500/30'

  const confidencePercent = Math.round((prediction.confidence / 3) * 100)

  return (
    <div className={`glass-morphism p-8 border bg-gradient-to-br ${bgClass} animate-slide-in`}>
      <div className="space-y-6">
        {/* Result badge */}
        <div className="flex items-center justify-between">
          <div className="flex items-center gap-3">
            <span className="text-4xl">{iconEmoji}</span>
            <div>
              <h3 className="text-2xl font-bold">{label}</h3>
              <p className="text-sm text-gray-300">Prediction Result</p>
            </div>
          </div>
          <span className={badgeClass}>
            {prediction.prediction.toUpperCase()}
          </span>
        </div>

        {/* Confidence bar */}
        <div>
          <div className="flex justify-between items-center mb-2">
            <p className="text-sm font-medium text-gray-200">Model Confidence</p>
            <p className="text-sm font-semibold text-purple-300">
              {confidencePercent}%
            </p>
          </div>
          <div className="w-full bg-slate-700/50 rounded-full h-3 overflow-hidden border border-slate-600/50">
            <div
              className={`h-full transition-all duration-300 ${
                isReal
                  ? 'bg-gradient-to-r from-green-500 to-emerald-400'
                  : 'bg-gradient-to-r from-red-500 to-rose-400'
              }`}
              style={{ width: `${confidencePercent}%` }}
            />
          </div>
        </div>

        {/* Article preview */}
        <div>
          <p className="text-xs font-semibold text-gray-400 mb-2">ARTICLE PREVIEW</p>
          <p className="text-sm text-gray-300 line-clamp-3">
            {prediction.text}...
          </p>
        </div>

        {/* Timestamp */}
        <div className="flex justify-between items-center text-xs text-gray-400 border-t border-slate-700/50 pt-4">
          <span>Analysis at {prediction.timestamp.toLocaleTimeString()}</span>
          <span className="text-purple-400 font-medium">ID: {prediction.id.slice(-4)}</span>
        </div>
      </div>
    </div>
  )
}
