# Food Health Classifier - Backend

## 🎯 Model Folosit
- **nateraw/food** - EfficientNet pre-antrenat pe Food-101
- **101 clase** de mâncăruri preparate
- **NU** recunoaște ingrediente crude (mere, banane, etc.)

## 🚀 Cum rulezi

```powershell
# Activează virtual environment
.\venv\Scripts\activate

# Instalează dependențele
pip install -r requirements.txt

# Rulează serverul
uvicorn app:app --reload --host 0.0.0.0 --port 8000
```

## 🔍 Testare

```powershell
# Vezi toate clasele disponibile
python show_classes.py

# Testează modelul
python test_model.py
```

## 📝 Important!
- Threshold de confidence: **50%**
- Dacă < 50% → returnează "Unknown"
- Pentru lista completă de clase, vezi: `../FOOD_CLASSES.md`

## 🛠️ Fișiere importante
- `routers/predict.py` - endpoint-ul principal
- `utils/nutrition_map.py` - datele nutriționale
- `utils/health_index.py` - calculul scorului de sănătate
- `model/labels_food101.json` - maparea label-urilor
