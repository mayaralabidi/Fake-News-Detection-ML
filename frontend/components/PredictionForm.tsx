'use client'

import { useState } from 'react'

interface PredictionFormProps {
  onPredict: (text: string, title?: string) => Promise<void>
  loading: boolean
}

export default function PredictionForm({ onPredict, loading }: PredictionFormProps) {
  const [text, setText] = useState('')
  const [title, setTitle] = useState('')

  const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault()
    await onPredict(text, title)
  }

  const handleClear = () => {
    setText('')
    setTitle('')
  }

  return (
    <form onSubmit={handleSubmit} className="space-y-4">
      <div>
        <label htmlFor="title" className="block text-sm font-medium text-gray-200 mb-2">
          Article Title (Optional)
        </label>
        <input
          type="text"
          id="title"
          value={title}
          onChange={(e) => setTitle(e.target.value)}
          placeholder="Enter article title..."
          className="w-full px-4 py-3 bg-slate-800/50 border border-purple-500/30 rounded-lg focus:outline-none focus:border-purple-400 focus:ring-2 focus:ring-purple-500/20 text-white placeholder-gray-400 transition-all"
          disabled={loading}
        />
      </div>

      <div>
        <label htmlFor="text" className="block text-sm font-medium text-gray-200 mb-2">
          Article Content *
        </label>
        <textarea
          id="text"
          value={text}
          onChange={(e) => setText(e.target.value)}
          placeholder="Paste the article text here to analyze..."
          rows={6}
          className="w-full px-4 py-3 bg-slate-800/50 border border-purple-500/30 rounded-lg focus:outline-none focus:border-purple-400 focus:ring-2 focus:ring-purple-500/20 text-white placeholder-gray-400 resize-none transition-all"
          disabled={loading}
          required
        />
      </div>

      <div className="flex gap-3 pt-2">
        <button
          type="submit"
          disabled={loading || !text.trim()}
          className="btn-primary flex-1"
        >
          {loading ? (
            <>
              <span className="inline-block w-4 h-4 border-2 border-white/30 border-t-white rounded-full animate-spin mr-2"></span>
              Analyzing...
            </>
          ) : (
            '🔍 Analyze Article'
          )}
        </button>
        <button
          type="button"
          onClick={handleClear}
          disabled={loading}
          className="btn-secondary"
        >
          Clear
        </button>
      </div>

      <p className="text-xs text-gray-400 mt-4">
        💡 Tip: The model analyzes the text and predicts whether it's real or fake news based on language patterns and features learned from the training data.
      </p>
    </form>
  )
}
