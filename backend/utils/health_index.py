# utils/health_index.py
from typing import Dict, Tuple

def clamp(x: float, lo: float, hi: float) -> float:
    return max(lo, min(hi, x))

def compute_health_index(nutri: Dict[str, float]) -> Tuple[float, str, str]:
    """
    Input: {"calories": int, "protein_g": float, "fat_g": float, "carbs_g": float, "sugar_g": float (optional)}
    Output: (score_0_10, color_hex, message)
    Heuristic simplă, explicabilă, bună pentru demo.
    """
    cal = float(nutri.get("calories", 0))
    prot = float(nutri.get("protein_g", 0))
    fat  = float(nutri.get("fat_g", 0))
    carb = float(nutri.get("carbs_g", 0))
    sugar = float(nutri.get("sugar_g", 0))

    # Punctaj de bază: proteina ajută, grăsimea și zahărul penalizează, caloriile mari penalizează
    base = 5.0 + 0.02*prot - 0.015*fat - 0.01*sugar - 0.004*max(0, cal-250)
    score = clamp(base, 0.0, 10.0)

    if score >= 7.5:
        color = "#2ecc71"; msg = "Great choice! 🥗"
    elif score >= 5.0:
        color = "#f1c40f"; msg = "Decent choice, balance it ⚖️"
    else:
        color = "#e74c3c"; msg = "High calorie/sugar/fat — enjoy in moderation 🍕"

    return round(score, 1), color, msg
