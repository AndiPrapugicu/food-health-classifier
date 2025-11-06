export default function Loader() {
  return (
    <div style={{ 
      display: 'inline-flex',
      flexDirection: 'column',
      alignItems: 'center',
      gap: 12
    }}>
      <svg width="48" height="48" viewBox="0 0 50 50">
        <circle 
          cx="25" 
          cy="25" 
          r="20" 
          fill="none" 
          stroke="var(--accent-green)" 
          strokeWidth="4" 
          strokeDasharray="31.4 31.4" 
          transform="rotate(-90 25 25)"
          opacity="0.2"
        />
        <circle 
          cx="25" 
          cy="25" 
          r="20" 
          fill="none" 
          stroke="var(--accent-green)" 
          strokeWidth="4" 
          strokeDasharray="62.8" 
          strokeLinecap="round"
          transform="rotate(-90 25 25)"
        >
          <animateTransform 
            attributeName="transform" 
            type="rotate" 
            from="0 25 25" 
            to="360 25 25" 
            dur="1.2s" 
            repeatCount="indefinite" 
          />
          <animate
            attributeName="stroke-dashoffset"
            values="0;-31.4;-62.8"
            dur="1.2s"
            repeatCount="indefinite"
          />
        </circle>
      </svg>
    </div>
  )
}
