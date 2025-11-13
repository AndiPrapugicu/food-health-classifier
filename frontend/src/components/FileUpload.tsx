import React, { useState, useRef, useEffect } from 'react'
import type { Prediction } from '../types/Prediction'
import { predictImage } from '../api/predict'
import Loader from './Loader'

interface Props {
  onResult: (res: Prediction, previewUrl?: string) => void
}

export default function FileUpload({ onResult }: Props) {
  const [preview, setPreview] = useState<string | null>(null)
  const [loading, setLoading] = useState(false)
  const [dragActive, setDragActive] = useState(false)
  const [successGlow, setSuccessGlow] = useState(false)
  const inputRef = useRef<HTMLInputElement | null>(null)

  function handleFile(file?: File) {
    if (!file) return
    const url = URL.createObjectURL(file)
    setPreview(url)
    setLoading(true)
    predictImage(file)
      .then((res) => {
        onResult(res, url)
        setSuccessGlow(true)
        setTimeout(() => setSuccessGlow(false), 700)
      })
      .catch((err) => alert(String(err)))
      .finally(() => setLoading(false))
  }

  function handleDrag(e: React.DragEvent) {
    e.preventDefault()
    e.stopPropagation()
    if (e.type === 'dragenter' || e.type === 'dragover') setDragActive(true)
    if (e.type === 'dragleave') setDragActive(false)
  }

  function handleDrop(e: React.DragEvent) {
    e.preventDefault()
    e.stopPropagation()
    setDragActive(false)
    if (e.dataTransfer.files && e.dataTransfer.files[0]) {
      handleFile(e.dataTransfer.files[0])
    }
  }

  const handleClick = () => {
    if (!preview) inputRef.current?.click()
  }

  return (
    <div style={{ maxWidth: 720, margin: '0 auto', padding: 16 }}>
      <div
        onDragEnter={handleDrag}
        onDragLeave={handleDrag}
        onDragOver={handleDrag}
        onDrop={handleDrop}
        onClick={handleClick}
        className={`file-upload ${successGlow ? 'success-glow' : ''}`}
        style={{
          border: dragActive ? '3px dashed var(--accent-green)' : '3px dashed #d1d5db',
          padding: 40,
          borderRadius: 'var(--radius-lg)',
          textAlign: 'center',
          background: dragActive ? 'rgba(76, 175, 80, 0.08)' : 'var(--bg-secondary)',
          transition: 'all 0.3s ease',
          boxShadow: dragActive ? '0 10px 25px rgba(76,175,80,0.25)' : 'var(--shadow-md)',
          cursor: 'pointer',
          userSelect: 'none'
        }}
      >
        {preview ? (
          <div>
            <img
              src={preview}
              alt="preview"
              style={{
                maxWidth: '100%',
                maxHeight: 320,
                borderRadius: 'var(--radius-md)',
                boxShadow: 'var(--shadow-md)'
              }}
            />
            {!loading && (
              <button
                onClick={(e) => {
                  e.stopPropagation()
                  setPreview(null)
                }}
                style={{
                  marginTop: 16,
                  background: 'var(--text-muted)',
                  fontSize: '0.9rem',
                  padding: '8px 16px',
                  borderRadius: 'var(--radius-md)',
                  cursor: 'pointer'
                }}
              >
                Clear & Choose Another
              </button>
            )}
          </div>
        ) : (
          <div style={{ padding: '2rem 1rem' }}>
            <div style={{ fontSize: '4rem', marginBottom: '1rem' }}>📸</div>
            <p style={{ fontSize: '1.3rem', fontWeight: 600, color: 'var(--text-primary)', marginBottom: 8 }}>
              {dragActive
                ? 'Drop your image here!'
                : 'Drag & drop your food image or click to browse'}
            </p>
            <button
              onClick={(e) => {
                e.stopPropagation()
                inputRef.current?.click()
              }}
              style={{
                padding: '12px 32px',
                fontSize: '1.1rem',
                borderRadius: 'var(--radius-md)',
                cursor: 'pointer',
                transition: 'all 0.2s ease',
                border: 'none',
                background: 'var(--accent-blue)',
                color: '#fff'
              }}
            >
              📁 Browse Files
            </button>
            <p style={{ marginTop: 16, fontSize: '0.85rem', color: 'var(--text-muted)' }}>
              Supports: JPG, PNG, WEBP • Max 10MB
            </p>
          </div>
        )}

        <input
          ref={inputRef}
          type="file"
          accept="image/*"
          style={{ display: 'none' }}
          onChange={(e) => {
            const f = e.target.files && e.target.files[0]
            if (f) handleFile(f)
          }}
        />

        {loading && (
          <div style={{ marginTop: 20 }}>
            <Loader />
            <p style={{ color: 'var(--text-secondary)', marginTop: 12 }}>🔍 Analyzing your food...</p>
          </div>
        )}
      </div>

      <div style={{ marginTop: 24, padding: 16, background: 'var(--bg-accent)', borderRadius: 'var(--radius-md)', border: '1px solid rgba(76, 175, 80, 0.2)' }}>
        <p style={{ margin: 0, fontSize: '0.9rem', color: 'var(--text-secondary)', lineHeight: 1.6 }}>
          💡 <strong>Tip:</strong> Upload clear photos of prepared dishes like pizza, burgers, pasta, sushi, etc.
        </p>
      </div>

      <style>{`
        .success-glow {
          animation: glowBounce 0.6s ease-in-out;
        }
        @keyframes glowBounce {
          0% { transform: scale(1); box-shadow: 0 0 0 rgba(76,175,80,0); }
          50% { transform: scale(1.03); box-shadow: 0 0 20px rgba(76,175,80,0.6); }
          100% { transform: scale(1); box-shadow: 0 0 0 rgba(76,175,80,0); }
        }
      `}</style>
    </div>
  )
}
