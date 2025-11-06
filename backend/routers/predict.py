import io
import json
from pathlib import Path

import torch
import torch.nn.functional as F
from fastapi import APIRouter, UploadFile, File
from fastapi.responses import JSONResponse
from PIL import Image
from transformers import AutoImageProcessor, AutoModelForImageClassification

from utils.health_index import compute_health_index
from utils.nutrition_map import NUTRITION_MAP

router = APIRouter()

ROOT = Path(__file__).resolve().parents[1]
LABELS_FILE = ROOT / "model" / "labels_food101.json"

LABELS = json.load(open(LABELS_FILE, "r", encoding="utf-8"))

# 🎯 SOLUȚIA: Folosim un model PRE-ANTRENAT pe Food-101 de la HuggingFace
# Acest model este deja antrenat CORECT pe datasetul Food-101!
MODEL_NAME = "nateraw/food"  # Model EfficientNet antrenat pe Food-101
processor = AutoImageProcessor.from_pretrained(MODEL_NAME)
model = AutoModelForImageClassification.from_pretrained(MODEL_NAME)
model.eval()


@router.get("/health")
def health():
    return {"status": "ok", "service": "Food Health Classifier"}


@router.post("/predict-image")
async def predict_image(file: UploadFile = File(...)):
    img_bytes = await file.read()

    try:
        img = Image.open(io.BytesIO(img_bytes)).convert("RGB")
    except:
        return JSONResponse(status_code=400,
                            content={"error": "Invalid image"})

    # 🎯 Folosim procesorul și modelul de la HuggingFace
    inputs = processor(images=img, return_tensors="pt")
    
    with torch.no_grad():
        outputs = model(**inputs)
        logits = outputs.logits
        probs = F.softmax(logits, dim=1)[0]
        top5 = torch.topk(probs, k=5)

    results = []
    for score, idx in zip(top5.values, top5.indices):
        # 🎯 Modelul returnează direct numele clasei, nu doar un index!
        # Dar trebuie să verificăm cum sunt denumite clasele în model
        predicted_class = model.config.id2label[idx.item()]
        # Convertim din formatul modelului la formatul nostru
        label = predicted_class.replace(" ", "_").lower()
        results.append({"label": label, "score": round(score.item(), 4)})

    # BEST PREDICTION
    label = results[0]["label"]
    confidence = results[0]["score"]

    # 🎯 ÎMBUNĂTĂȚIRE: Threshold mai mare pentru confidence
    # Food-101 conține doar mâncăruri PREPARATE, nu ingrediente crude
    # Dacă confidence < 50%, probabil nu e în dataset
    if confidence < 0.50:
        return JSONResponse(content={
            "food": "Unknown",
            "confidence": confidence,
            "nutrition": None,
            "health_index": None,
            "health_color": "#999999",
            "message": f"🤔 Hmm, not confident enough ({confidence*100:.1f}%). Try a prepared dish like pizza, burger, pasta, etc.",
            "top5": results
        })

    # Unsupported food in nutrition data
    if label not in NUTRITION_MAP:
        return JSONResponse(content={
            "food": label,
            "confidence": confidence,
            "nutrition": None,
            "health_index": None,
            "health_color": "#4B7BEC",
            "message": f"No nutrition data yet for '{label}'. Coming soon! 🍽️",
            "top5": results
        })

    # Full supported result ✅
    nutrition = NUTRITION_MAP[label]
    hi, color, msg = compute_health_index(nutrition)

    return JSONResponse(content={
        "food": label,
        "confidence": confidence,
        "nutrition": nutrition,
        "health_index": hi,
        "health_color": color,
        "message": msg,
        "top5": results
    })
