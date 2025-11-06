export interface Nutrition {
  calories: number;
  protein_g: number;
  fat_g: number;
  carbs_g: number;
  sugar_g?: number;
}

export interface Top5Item {
  label: string;
  score: number;
}

export interface Prediction {
  food: string;
  confidence: number;
  nutrition: Nutrition | null;
  health_index: number | null; // 0..10
  health_color: string; // hex
  message: string;
  top5?: Top5Item[];
}
