import type { Prediction } from '../types/Prediction'

const BACKEND_URL = import.meta.env.DEV ? 'http://127.0.0.1:8000' : ''

export async function predictImage(file: File): Promise<Prediction> {
  const fd = new FormData()
  fd.append('file', file)

  const res = await fetch(`${BACKEND_URL}/predict-image`, {
    method: 'POST',
    body: fd,
  })

  if (!res.ok) {
    throw new Error(`Prediction request failed: ${res.status}`)
  }

  const data = await res.json()
  return data as Prediction
}
