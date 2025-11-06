import type { Prediction } from '../types/Prediction'
import HealthBadge from './HealthBadge'
import NutritionChart from './NutritionChart'

interface Props {
  result: Prediction
  imageUrl?: string
  onTryAnother?: () => void
}

export default function ResultCard({ result, imageUrl, onTryAnother }: Props) {
  const isUnknown = result.food === 'Unknown'
  
  return (
    <div style={{ 
      maxWidth: 800, 
      margin: '0 auto', 
      padding: 24,
      background: 'var(--bg-secondary)',
      borderRadius: 'var(--radius-lg)',
      boxShadow: 'var(--shadow-lg)',
      animation: 'fadeIn 0.5s ease-out'
    }}>
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
        <h2 style={{ 
          fontSize: '2.5rem',
          margin: '0 0 12px 0',
          color: isUnknown ? 'var(--text-muted)' : 'var(--text-primary)',
          textTransform: 'capitalize'
        }}>
          {result.food.replace(/_/g, ' ')}
        </h2>
        
        <div style={{ 
          display: 'flex', 
          alignItems: 'center', 
          justifyContent: 'center',
          gap: 16,
          flexWrap: 'wrap',
          marginBottom: 16
        }}>
          {!isUnknown && <HealthBadge score={result.health_index} color={result.health_color} />}
          
          <div style={{ 
            display: 'inline-flex',
            alignItems: 'center',
            gap: 8,
            padding: '8px 16px',
            background: result.confidence >= 0.7 ? 'rgba(76, 175, 80, 0.1)' : 'rgba(255, 152, 0, 0.1)',
            borderRadius: 'var(--radius-sm)',
            border: `2px solid ${result.confidence >= 0.7 ? 'var(--accent-green)' : 'var(--accent-orange)'}`,
          }}>
            <span style={{ fontSize: '1.2rem' }}>
              {result.confidence >= 0.7 ? '✅' : '⚠️'}
            </span>
            <span style={{ 
              fontWeight: 600,
              color: 'var(--text-primary)'
            }}>
              {(result.confidence * 100).toFixed(1)}% confident
            </span>
          </div>
        </div>

        <button
          onClick={onTryAnother}
          style={{ 
            padding: '10px 24px',
            fontSize: '1rem',
            borderRadius: 'var(--radius-md)',
            background: 'var(--accent-blue)',
            marginTop: 8
          }}
        >
          🔄 Try Another Image
        </button>
      </div>

      {!isUnknown && result.nutrition && (
        <div style={{ marginTop: 24, marginBottom: 24 }}>
          <h3 style={{ 
            fontSize: '1.3rem',
            color: 'var(--text-primary)',
            marginBottom: 16,
            display: 'flex',
            alignItems: 'center',
            gap: 8
          }}>
            <span>📊</span> Nutritional Information
            <span style={{ 
              fontSize: '0.75rem',
              color: 'var(--text-muted)',
              fontWeight: 400 
            }}>
              (per 100g)
            </span>
          </h3>
          <NutritionChart nutrition={result.nutrition} />
        </div>
      )}

      <div style={{ 
        marginTop: 20,
        padding: 20,
        background: isUnknown ? '#fff4e6' : 'var(--bg-accent)',
        borderRadius: 'var(--radius-md)',
        border: `2px solid ${isUnknown ? 'var(--accent-orange)' : 'rgba(76, 175, 80, 0.3)'}`,
      }}>
        <p style={{ 
          margin: 0,
          fontSize: '1rem',
          color: 'var(--text-secondary)',
          lineHeight: 1.6,
          textAlign: 'center'
        }}>
          {isUnknown ? '🤔' : '💡'} <strong>{result.message}</strong>
        </p>
      </div>

      {result.top5 && result.top5.length > 1 && (
        <details style={{ marginTop: 20 }}>
          <summary style={{ 
            cursor: 'pointer',
            padding: 12,
            background: 'var(--bg-accent)',
            borderRadius: 'var(--radius-sm)',
            fontWeight: 600,
            color: 'var(--text-primary)',
            userSelect: 'none'
          }}>
            🔍 View Top 5 Predictions
          </summary>
          <div style={{ 
            marginTop: 12,
            padding: 16,
            background: '#f9fafb',
            borderRadius: 'var(--radius-sm)'
          }}>
            {result.top5.map((item, idx) => (
              <div 
                key={idx}
                style={{ 
                  display: 'flex',
                  justifyContent: 'space-between',
                  padding: '8px 0',
                  borderBottom: idx < result.top5!.length - 1 ? '1px solid #e5e7eb' : 'none'
                }}
              >
                <span style={{ 
                  fontWeight: idx === 0 ? 600 : 400,
                  color: 'var(--text-primary)',
                  textTransform: 'capitalize'
                }}>
                  {idx + 1}. {item.label.replace(/_/g, ' ')}
                </span>
                <span style={{ 
                  color: 'var(--text-secondary)',
                  fontFamily: 'monospace'
                }}>
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
