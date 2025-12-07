'use client'

import { Prediction } from './DetectorContainer'

interface PredictionHistoryProps {
  predictions: Prediction[]
  onClear: () => void
}

export default function PredictionHistory({ predictions, onClear }: PredictionHistoryProps) {
  return (
    <div className="glass-morphism p-6 border-purple-500/30 h-full flex flex-col">
      <div className="flex justify-between items-center mb-6">
        <h2 className="text-xl font-bold text-white">Recent Predictions</h2>
        {predictions.length > 0 && (
          <button
            onClick={onClear}
            className="text-xs bg-red-500/20 hover:bg-red-500/30 text-red-300 px-3 py-1 rounded-full transition-colors"
          >
            Clear
          </button>
        )}
      </div>

      {predictions.length === 0 ? (
        <div className="flex-1 flex items-center justify-center text-center">
          <div>
            <p className="text-4xl mb-3">📚</p>
            <p className="text-gray-400 text-sm">
              No predictions yet. <br />
              Analyze an article to get started!
            </p>
          </div>
        </div>
      ) : (
        <div className="space-y-3 overflow-y-auto flex-1">
          {predictions.map((pred) => (
            <div
              key={pred.id}
              className={`p-3 rounded-lg border transition-all hover:bg-white/5 cursor-pointer ${
                pred.prediction === 'real'
                  ? 'bg-green-500/10 border-green-500/30'
                  : 'bg-red-500/10 border-red-500/30'
              }`}
            >
              <div className="flex items-start justify-between gap-2 mb-2">
                <span className={`text-xs font-bold px-2 py-1 rounded-full ${
                  pred.prediction === 'real'
                    ? 'badge-real'
                    : 'badge-fake'
                }`}>
                  {pred.prediction.toUpperCase()}
                </span>
                <span className="text-xs text-gray-400">
                  {pred.timestamp.toLocaleTimeString()}
                </span>
              </div>
              <p className="text-xs text-gray-300 line-clamp-2">
                {pred.text}...
              </p>
              <div className="text-xs text-gray-400 mt-2">
                Confidence: <span className="text-purple-300 font-medium">
                  {Math.round((pred.confidence / 3) * 100)}%
                </span>
              </div>
            </div>
          ))}
        </div>
      )}
    </div>
  )
}
