import type { Nutrition } from '../types/Prediction'

interface Props {
  nutrition: Nutrition | null
}

export default function NutritionChart({ nutrition }: Props) {
  if (!nutrition) {
    return (
      <div style={{ 
        textAlign: 'center',
        padding: 32,
        color: 'var(--text-muted)',
        fontSize: '1rem',
        background: '#f9fafb',
        borderRadius: 'var(--radius-md)',
        border: '2px dashed #d1d5db'
      }}>
        📊 No nutrition data available for this food yet.
      </div>
    )
  }

  const items = [
    { key: 'protein_g', label: 'Protein', value: nutrition.protein_g, color: '#3b82f6', unit: 'g' },
    { key: 'fat_g', label: 'Fat', value: nutrition.fat_g, color: '#f97316', unit: 'g' },
    { key: 'carbs_g', label: 'Carbs', value: nutrition.carbs_g, color: '#10b981', unit: 'g' },
  ]

  if (nutrition.sugar_g !== undefined) {
    items.push({ 
      key: 'sugar_g', 
      label: 'Sugar', 
      value: nutrition.sugar_g, 
      color: '#ec4899', 
      unit: 'g' 
    })
  }

  const max = Math.max(...items.map((i) => i.value), 1)

  return (
    <div>
      {/* Calories Card */}
      <div style={{ 
        marginBottom: 20,
        padding: 20,
        background: 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)',
        borderRadius: 'var(--radius-md)',
        color: 'white',
        textAlign: 'center',
        boxShadow: 'var(--shadow-md)'
      }}>
        <div style={{ fontSize: '0.9rem', opacity: 0.9, marginBottom: 4 }}>
          Total Calories
        </div>
        <div style={{ fontSize: '2.5rem', fontWeight: 700 }}>
          {nutrition.calories}
        </div>
        <div style={{ fontSize: '0.85rem', opacity: 0.8 }}>
          kcal per 100g
        </div>
      </div>

      {/* Macros Chart */}
      <div style={{ 
        display: 'grid', 
        gap: 16,
        background: '#f9fafb',
        padding: 20,
        borderRadius: 'var(--radius-md)'
      }}>
        {items.map((it) => (
          <div key={it.key}>
            <div style={{ 
              display: 'flex',
              justifyContent: 'space-between',
              marginBottom: 8,
              fontSize: '0.95rem'
            }}>
              <span style={{ 
                fontWeight: 600,
                color: 'var(--text-primary)'
              }}>
                {it.label}
              </span>
              <span style={{ 
                fontWeight: 700,
                color: it.color
              }}>
                {it.value}{it.unit}
              </span>
            </div>
            <div style={{ 
              height: 10,
              background: '#e5e7eb',
              borderRadius: 10,
              overflow: 'hidden',
              position: 'relative'
            }}>
              <div style={{ 
                width: `${Math.min((it.value / max) * 100, 100)}%`,
                height: '100%',
                background: `linear-gradient(90deg, ${it.color}, ${it.color}dd)`,
                borderRadius: 10,
                transition: 'width 0.5s ease',
                boxShadow: `0 0 8px ${it.color}40`
              }} />
            </div>
          </div>
        ))}
      </div>
    </div>
  )
}
