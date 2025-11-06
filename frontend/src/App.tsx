import { useState } from 'react'
import './App.css'
import FileUpload from './components/FileUpload'
import ResultCard from './components/ResultCard'
import type { Prediction } from './types/Prediction'

function App() {
  const [result, setResult] = useState<Prediction | null>(null)
  const [previewUrl, setPreviewUrl] = useState<string | undefined>(undefined)

  return (
    <div className="app-container">
      <header className="app-header">
        <div className="app-emoji">🥗🍕🥑</div>
        <h1 className="app-title">Food Health Classifier</h1>
        <p className="app-subtitle">AI-Powered Food Recognition & Nutrition Analysis</p>
        <p className="app-description">
          Upload a photo of your meal and discover its nutritional value, health score, and make informed food choices!
        </p>
      </header>

      <main className="main-content">
        {!result ? (
          <FileUpload onResult={(r, url) => {
            setResult(r)
            setPreviewUrl(url)
          }} />
        ) : (
          <ResultCard 
            result={result} 
            imageUrl={previewUrl} 
            onTryAnother={() => { 
              setResult(null)
              setPreviewUrl(undefined)
            }} 
          />
        )}
      </main>
    </div>
  )
}

export default App
