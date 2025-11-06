interface Props {
  score: number | null
  color: string
}

export default function HealthBadge({ score, color }: Props) {
  if (score === null) return null
  
  const getHealthLabel = (score: number) => {
    if (score >= 8) return 'Excellent'
    if (score >= 6) return 'Good'
    if (score >= 4) return 'Fair'
    return 'Poor'
  }

  const getEmoji = (score: number) => {
    if (score >= 8) return '🌟'
    if (score >= 6) return '👍'
    if (score >= 4) return '⚠️'
    return '❌'
  }

  return (
    <div style={{ 
      display: 'inline-flex',
      alignItems: 'center',
      gap: 12,
      padding: '10px 20px',
      background: `linear-gradient(135deg, ${color}15, ${color}05)`,
      borderRadius: 'var(--radius-md)',
      border: `2px solid ${color}`,
      boxShadow: 'var(--shadow-sm)'
    }}>
      <div style={{ 
        width: 40,
        height: 40,
        borderRadius: '50%',
        background: color,
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'center',
        color: 'white',
        fontWeight: 700,
        fontSize: '1.1rem',
        boxShadow: `0 2px 8px ${color}40`
      }}>
        {score}
      </div>
      <div style={{ textAlign: 'left' }}>
        <div style={{ 
          fontSize: '0.75rem',
          color: 'var(--text-muted)',
          fontWeight: 500,
          textTransform: 'uppercase',
          letterSpacing: '0.05em'
        }}>
          Health Score
        </div>
        <div style={{ 
          fontSize: '1.1rem',
          fontWeight: 700,
          color: 'var(--text-primary)',
          display: 'flex',
          alignItems: 'center',
          gap: 6
        }}>
          <span>{getEmoji(score)}</span>
          {getHealthLabel(score)}
        </div>
      </div>
    </div>
  )
}
