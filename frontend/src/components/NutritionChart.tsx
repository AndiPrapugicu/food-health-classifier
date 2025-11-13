import { useState, useEffect } from 'react'
import type { Nutrition } from '../types/Prediction'

interface Props {
  nutrition: Nutrition | null
}

export default function NutritionChart({ nutrition }: Props) {
  const [animatedValues, setAnimatedValues] = useState<Record<string, number>>({})
  const [hovered, setHovered] = useState(false)
  const [visibleCharts, setVisibleCharts] = useState({
    calories: true,
    protein: true,
    fat: true,
    carbs: true,
    sugar: true
  })

  if (!nutrition) {
    return (
      <div style={{
        textAlign: 'center',
        padding: 32,
        color: 'var(--text-muted)',
        fontSize: '1rem',
        background: 'var(--bg-secondary)',
        borderRadius: 'var(--radius-md)',
        border: '2px dashed #d1d5db'
      }}>
        📊 No nutrition data available for this food yet.
      </div>
    )
  }

  const dailyNeeds: Record<string, number> = {
    protein_g: 70,
    fat_g: 50,
    carbs_g: 275,
    sugar_g: 50
  }

  const items = [
    { key: 'protein_g', label: 'Protein', value: nutrition.protein_g, color: '#3b82f6', unit: 'g' },
    { key: 'fat_g', label: 'Fat', value: nutrition.fat_g, color: '#f97316', unit: 'g' },
    { key: 'carbs_g', label: 'Carbs', value: nutrition.carbs_g, color: '#10b981', unit: 'g' }
  ]

  if (nutrition.sugar_g !== undefined) {
    items.push({ key: 'sugar_g', label: 'Sugar', value: nutrition.sugar_g, color: '#ec4899', unit: 'g' })
  }

  const max = Math.max(...items.map(i => i.value), 1)
  const dominantValue = Math.max(...items.map(i => i.value))

  useEffect(() => {
    const animationTimeout = setTimeout(() => {
      const newValues: Record<string, number> = {}
      items.forEach(i => newValues[i.key] = i.value)
      setAnimatedValues(newValues)
    }, 50)
    return () => clearTimeout(animationTimeout)
  }, [nutrition])

  return (
    <div style={{ position: 'relative' }}>
      {/* Toggle Buttons for Charts */}
      <div style={{ display: 'flex', gap: 8, marginBottom: 16, flexWrap: 'wrap', justifyContent: 'center' }}>
        {Object.keys(visibleCharts).map(key => (
          <button
            key={key}
            onClick={() =>
              setVisibleCharts(prev => ({ ...prev, [key]: !prev[key] }))
            }
            style={{
              padding: '6px 12px',
              borderRadius: 'var(--radius-sm)',
              border: 'none',
              cursor: 'pointer',
              background: visibleCharts[key as keyof typeof visibleCharts] ? 'var(--accent-blue)' : 'var(--bg-secondary)',
              color: visibleCharts[key as keyof typeof visibleCharts] ? '#fff' : 'var(--text-primary)',
              fontSize: '0.85rem',
              transition: 'all 0.2s ease'
            }}
          >
            {key.charAt(0).toUpperCase() + key.slice(1)}
          </button>
        ))}
      </div>

      {/* Calories Card */}
      {visibleCharts.calories && (
        <div style={{
          marginBottom: 20,
          padding: 20,
          background: 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)',
          borderRadius: 'var(--radius-md)',
          color: '#fff',
          textAlign: 'center',
          boxShadow: 'var(--shadow-md)'
        }}>
          <div style={{ fontSize: '0.9rem', opacity: 0.9, marginBottom: 4 }}>Total Calories</div>
          <div style={{ fontSize: '2.5rem', fontWeight: 700 }}>{nutrition.calories}</div>
          <div style={{ fontSize: '0.85rem', opacity: 0.8 }}>kcal per 100g</div>
        </div>
      )}

      {/* Macros / Sugar Chart */}
      <div
        style={{
          display: 'grid',
          gap: 16,
          background: 'var(--bg-secondary)',
          padding: 20,
          borderRadius: 'var(--radius-md)',
          transition: 'background 0.3s'
        }}
        onMouseEnter={() => setHovered(true)}
        onMouseLeave={() => setHovered(false)}
      >
        {items.map(it => {
          if ((it.key === 'sugar_g' && !visibleCharts.sugar) ||
              (it.key === 'protein_g' && !visibleCharts.protein) ||
              (it.key === 'fat_g' && !visibleCharts.fat) ||
              (it.key === 'carbs_g' && !visibleCharts.carbs)) return null
          const percentDaily = ((it.value / (dailyNeeds[it.key] || 1)) * 100).toFixed(0)
          const isDominant = it.value === dominantValue
          return (
            <div key={it.key}>
              <div style={{
                display: 'flex',
                justifyContent: 'space-between',
                marginBottom: 8,
                fontSize: '0.95rem'
              }}>
                <span style={{ fontWeight: 600, color: 'var(--text-primary)' }}>
                  {it.label} {isDominant && '⭐'}
                </span>
                <span style={{ fontWeight: 700, color: it.color }}>
                  {it.value}{it.unit}
                </span>
              </div>
              <div style={{
                height: 12,
                background: '#e5e7eb',
                borderRadius: 10,
                overflow: 'hidden',
                position: 'relative',
                transition: 'background 0.3s ease'
              }}>
                <div style={{
                  width: `${Math.min((animatedValues[it.key] || 0) / max * 100, 100)}%`,
                  height: '100%',
                  background: isDominant
                    ? `linear-gradient(90deg, ${it.color}, #00000033)`
                    : `linear-gradient(90deg, ${it.color}, ${it.color}dd)`,
                  borderRadius: 10,
                  transition: 'width 0.5s ease',
                  boxShadow: `0 0 8px ${it.color}40`
                }} />
              </div>
            </div>
          )
        })}

        {/* Tooltip permanent */}
        {hovered && (
          <div style={{
            position: 'absolute',
            top: -10,
            right: '50%',
            transform: 'translateX(50%)',
            background: '#111827',   // constant
            color: '#f9fafb',        // constant
            borderRadius: 6,
            fontSize: '0.75rem',
            whiteSpace: 'nowrap',
            pointerEvents: 'none',
            zIndex: 10,
            boxShadow: '0 2px 8px rgba(0,0,0,0.2)',
            padding: '8px 12px'
          }}>
            {items.map(it => {
              const percentDaily = ((it.value / (dailyNeeds[it.key] || 1)) * 100).toFixed(0)
              return (
                <div key={it.key} style={{ marginBottom: 2 }}>
                  {it.label}: {it.value}{it.unit} ({percentDaily}% of daily needs)
                </div>
              )
            })}
            <div style={{
              position: 'absolute',
              bottom: -6,
              left: '50%',
              transform: 'translateX(-50%)',
              width: 0,
              height: 0,
              borderLeft: '6px solid transparent',
              borderRight: '6px solid transparent',
              borderTop: '6px solid #111827'
            }} />
          </div>
        )}
      </div>
    </div>
  )
}
