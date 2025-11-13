import { useState } from 'react'
import type { Prediction, Top5Item } from '../types/Prediction'
import HealthBadge from './HealthBadge'
import NutritionChart from './NutritionChart'

interface Props {
  result: Prediction
  imageUrl?: string
  onTryAnother?: () => void
}

export default function ResultCard({ result, imageUrl, onTryAnother }: Props) {
  const [liked, setLiked] = useState<boolean | null>(null) // null = no vote
  const [tooltipVisible, setTooltipVisible] = useState<{ [key: string]: boolean }>({
    confidence: false,
    tryAnother: false,
    like: false,
    dislike: false
  })
  const isUnknown = result.food === 'Unknown'

  const showTooltip = (key: string) => setTooltipVisible(prev => ({ ...prev, [key]: true }))
  const hideTooltip = (key: string) => setTooltipVisible(prev => ({ ...prev, [key]: false }))

  return (
    <div
      className="result-card"
      style={{
        maxWidth: 800,
        margin: '0 auto',
        padding: 24,
        borderRadius: 'var(--radius-lg)',
        boxShadow: 'var(--shadow-lg)',
        animation: 'fadeIn 0.5s ease-out',
        transition: 'transform 0.3s ease, box-shadow 0.3s ease',
        cursor: 'pointer'
      }}
      onMouseEnter={(e) => {
        e.currentTarget.style.transform = 'scale(1.03)'
        e.currentTarget.style.boxShadow = '0 12px 24px rgba(0,0,0,0.15)'
      }}
      onMouseLeave={(e) => {
        e.currentTarget.style.transform = 'scale(1)'
        e.currentTarget.style.boxShadow = 'var(--shadow-lg)'
      }}
    >
      {imageUrl && (
        <div style={{ textAlign: 'center', marginBottom: 24 }}>
          <img
            src={imageUrl}
            alt="analyzed food"
            style={{
              maxWidth: '100%',
              maxHeight: 300,
              borderRadius: 'var(--radius-md)',
              boxShadow: 'var(--shadow-md)',
              objectFit: 'cover'
            }}
          />
        </div>
      )}

      <div style={{ textAlign: 'center', marginBottom: 20 }}>
        <h2
          style={{
            fontSize: '2.5rem',
            margin: '0 0 12px 0',
            color: isUnknown ? 'var(--text-muted)' : 'var(--text-primary)',
            textTransform: 'capitalize'
          }}
        >
          {result.food.replace(/_/g, ' ')}
        </h2>

        <div style={{ display: 'flex', justifyContent: 'center', gap: 16, flexWrap: 'wrap', marginBottom: 16 }}>
          {!isUnknown && (
            <HealthBadge score={result.health_index} color={result.health_color} />
          )}

          {/* Confidence */}
          <div
            style={{
              position: 'relative',
              display: 'inline-flex',
              alignItems: 'center',
              gap: 8,
              padding: '8px 16px',
              background: result.confidence >= 0.7 ? 'rgba(76, 175, 80, 0.1)' : 'rgba(255, 152, 0, 0.1)',
              borderRadius: 'var(--radius-sm)',
              border: `2px solid ${result.confidence >= 0.7 ? 'var(--accent-green)' : 'var(--accent-orange)'}`,
              cursor: 'pointer'
            }}
            onMouseEnter={() => showTooltip('confidence')}
            onMouseLeave={() => hideTooltip('confidence')}
          >
            <span style={{ fontSize: '1.2rem' }}>{result.confidence >= 0.7 ? '✅' : '⚠️'}</span>
            <span style={{ fontWeight: 600, color: 'var(--text-primary)' }}>
              {(result.confidence * 100).toFixed(1)}%
            </span>
            {tooltipVisible.confidence && (
              <div
                style={{
                  position: 'absolute',
                  bottom: '120%',
                  left: '50%',
                  transform: 'translateX(-50%)',
                  padding: '6px 10px',
                  background: 'var(--tooltip-bg)',
                  color: 'var(--tooltip-text)',
                  borderRadius: 4,
                  fontSize: '0.75rem',
                  whiteSpace: 'nowrap',
                  zIndex: 1000,
                  boxShadow: '0 2px 8px rgba(0,0,0,0.3)'
                }}
              >
                Confidence of the prediction
              </div>
            )}
          </div>

          {/* Like / Dislike Microinteraction */}
          {!isUnknown && (
            <div style={{ display: 'flex', gap: 8, alignItems: 'center' }}>
              <div style={{ position: 'relative' }}>
                <button
                  onClick={() => setLiked(true)}
                  onMouseEnter={() => showTooltip('like')}
                  onMouseLeave={() => hideTooltip('like')}
                  style={{
                    fontSize: '1.5rem',
                    background: liked === true ? 'var(--accent-green)' : 'transparent',
                    color: liked === true ? '#fff' : 'var(--text-primary)',
                    border: 'none',
                    cursor: 'pointer',
                    borderRadius: '50%',
                    padding: 8,
                    transition: 'all 0.2s ease'
                  }}
                >
                  👍
                </button>
                {tooltipVisible.like && (
                  <div
                    style={{
                      position: 'absolute',
                      bottom: '120%',
                      left: '50%',
                      transform: 'translateX(-50%)',
                      padding: '6px 10px',
                      background: 'var(--tooltip-bg)',
                      color: 'var(--tooltip-text)',
                      borderRadius: 4,
                      fontSize: '0.75rem',
                      whiteSpace: 'nowrap',
                      zIndex: 1000,
                      boxShadow: '0 2px 8px rgba(0,0,0,0.3)'
                    }}
                  >
                    Like this prediction
                  </div>
                )}
              </div>

              <div style={{ position: 'relative' }}>
                <button
                  onClick={() => setLiked(false)}
                  onMouseEnter={() => showTooltip('dislike')}
                  onMouseLeave={() => hideTooltip('dislike')}
                  style={{
                    fontSize: '1.5rem',
                    background: liked === false ? 'var(--accent-orange)' : 'transparent',
                    color: liked === false ? '#fff' : 'var(--text-primary)',
                    border: 'none',
                    cursor: 'pointer',
                    borderRadius: '50%',
                    padding: 8,
                    transition: 'all 0.2s ease'
                  }}
                >
                  👎
                </button>
                {tooltipVisible.dislike && (
                  <div
                    style={{
                      position: 'absolute',
                      bottom: '120%',
                      left: '50%',
                      transform: 'translateX(-50%)',
                      padding: '6px 10px',
                      background: 'var(--tooltip-bg)',
                      color: 'var(--tooltip-text)',
                      borderRadius: 4,
                      fontSize: '0.75rem',
                      whiteSpace: 'nowrap',
                      zIndex: 1000,
                      boxShadow: '0 2px 8px rgba(0,0,0,0.3)'
                    }}
                  >
                    Dislike this prediction
                  </div>
                )}
              </div>
            </div>
          )}
        </div>

        {/* Try Another Image Button */}
        <div style={{ position: 'relative' }}>
          <button
            onClick={onTryAnother}
            onMouseEnter={() => showTooltip('tryAnother')}
            onMouseLeave={() => hideTooltip('tryAnother')}
            style={{
              padding: '10px 24px',
              fontSize: '1rem',
              borderRadius: 'var(--radius-md)',
              background: 'var(--accent-blue)',
              color: '#fff',
              marginTop: 8,
              cursor: 'pointer',
              border: 'none'
            }}
          >
            🔄 Try Another Image
          </button>
          {tooltipVisible.tryAnother && (
            <div
              style={{
                position: 'absolute',
                bottom: '120%',
                left: '50%',
                transform: 'translateX(-50%)',
                padding: '6px 10px',
                background: 'var(--tooltip-bg)',
                color: 'var(--tooltip-text)',
                borderRadius: 4,
                fontSize: '0.75rem',
                whiteSpace: 'nowrap',
                zIndex: 1000,
                boxShadow: '0 2px 8px rgba(0,0,0,0.3)'
              }}
            >
              Upload a new image to analyze
            </div>
          )}
        </div>
      </div>

      {/* Nutrition Chart */}
      {!isUnknown && result.nutrition && <NutritionChart nutrition={result.nutrition} />}

      {/* Top 5 Predictions */}
      {result.top5 && result.top5.length > 1 && (
        <details style={{ marginTop: 20 }}>
          <summary
            style={{
              cursor: 'pointer',
              padding: 12,
              background: 'var(--bg-accent)',
              borderRadius: 'var(--radius-sm)',
              fontWeight: 600,
              color: 'var(--text-primary)',
              userSelect: 'none'
            }}
          >
            🔍 View Top 5 Predictions
          </summary>
          <div
            style={{
              marginTop: 12,
              padding: 16,
              background: 'var(--bg-secondary)',
              borderRadius: 'var(--radius-sm)'
            }}
          >
            {result.top5.map((item: Top5Item, idx, arr) => (
              <div
                key={idx}
                style={{
                  display: 'flex',
                  justifyContent: 'space-between',
                  padding: '8px 0',
                  borderBottom: idx < arr.length - 1 ? '1px solid #e5e7eb' : 'none'
                }}
              >
                <span
                  style={{
                    fontWeight: idx === 0 ? 600 : 400,
                    color: 'var(--text-primary)',
                    textTransform: 'capitalize'
                  }}
                >
                  {idx + 1}. {item.label.replace(/_/g, ' ')}
                </span>
                <span style={{ color: 'var(--text-secondary)', fontFamily: 'monospace' }}>
                  {(item.score * 100).toFixed(1)}%
                </span>
              </div>
            ))}
          </div>
        </details>
      )}
    </div>
  )
}
