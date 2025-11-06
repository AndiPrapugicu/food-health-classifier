export type PredictionNutrition = {
  calories: number;
  protein_g: number;
  fat_g: number;
  carbs_g: number;
  health_index: number;
};

export type PredictionResult = {
  food: string;
  confidence: number;
  nutrition: PredictionNutrition;
  message: string;
};

/**
 * Send an image file to the backend predict endpoint and return the parsed JSON.
 *
 * Usage:
 *   const result = await predictImage(file);
 */
export async function predictImage(file: File): Promise<PredictionResult> {
  const form = new FormData();
  form.append("file", file);

  const res = await fetch("http://localhost:8000/predict-image", {
    method: "POST",
    body: form,
  });

  if (!res.ok) {
    const text = await res.text();
    throw new Error(`Prediction request failed: ${res.status} ${text}`);
  }

  const json = await res.json();
  return json as PredictionResult;
}
