# 🍎 Cum să adăugăm recunoaștere pentru ingrediente separate

## Problema
Food-101 NU conține ingrediente simple (mere, banane, roșii crude, etc.)

---

## ✅ SOLUȚIA 1: Model Dual (Recomandat pentru tine)

### Concept
Folosești **2 modele** în paralel:
1. **Model Food-101** - pentru mâncăruri preparate (ce ai acum)
2. **Model ImageNet** - pentru ingrediente (mere, banane, etc.)

### Flow Logic
```
User uploadează imagine
    ↓
Rulezi AMBELE modele în paralel
    ↓
Food-101 → confidence 80% → "pizza"
ImageNet → confidence 30% → "apple"
    ↓
Returnezi rezultatul cu confidence mai mare
```

### Implementare (Pseudo-cod)
```python
# În predict.py
from transformers import AutoImageProcessor, AutoModelForImageClassification

# Model 1: Food-101 (already loaded)
food_model = AutoModelForImageClassification.from_pretrained('nateraw/food')

# Model 2: ImageNet pentru ingrediente
ingredient_model = AutoModelForImageClassification.from_pretrained('google/vit-base-patch16-224')

@router.post("/predict-image")
async def predict_image(file: UploadFile):
    # ... load image ...
    
    # Rulează AMBELE modele
    food_result = predict_with_food_model(img)
    ingredient_result = predict_with_ingredient_model(img)
    
    # Alege cel mai bun
    if food_result['confidence'] > 0.50:
        return food_result  # Pizza, burger, etc.
    elif ingredient_result['confidence'] > 0.70:
        return ingredient_result  # Apple, banana, etc.
    else:
        return {"food": "Unknown"}
```

### Avantaje
- ✅ Simplu de implementat
- ✅ Acoperă AMBELE cazuri (mâncăruri + ingrediente)
- ✅ NU necesită training propriu

### Dezavantaje
- ⚠️ Folosește 2x mai multă memorie RAM
- ⚠️ Mai lent (2 predicții per imagine)

---

## ✅ SOLUȚIA 2: CLIP de la OpenAI (Mai versatil)

### Concept
CLIP poate recunoaște ORICE - nu e limitat la clase fixe!

### Implementare
```python
from transformers import CLIPProcessor, CLIPModel

model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")

# Poți adăuga ORICE clase custom!
labels = [
    "pizza", "burger", "apple", "banana", 
    "carrot", "tomato", "bread", "cheese", "etc."
]

inputs = processor(text=labels, images=image, return_tensors="pt", padding=True)
outputs = model(**inputs)
probs = outputs.logits_per_image.softmax(dim=1)
```

### Avantaje
- ✅ Foarte versatil - recunoaște ORICE
- ✅ Un singur model
- ✅ Poți adăuga clase noi fără training

### Dezavantaje
- ⚠️ Mai puțin precis decât modele specializate
- ⚠️ Mai mare (necesită mai multă RAM)

---

## ✅ SOLUȚIA 3: Fine-Tuning Custom (Profesional dar complex)

### Concept
Antrenezi propriul model pe un dataset combinat:
- Food-101 (mâncăruri)
- + ImageNet (ingrediente)
- + Date custom tale

### Pași
1. Colectezi dataset (1000+ imagini per clasă)
2. Antrenezi un clasificator (EfficientNet, ResNet, etc.)
3. Salvezi modelul
4. Îl folosești în backend

### Avantaje
- ✅ Cea mai mare precizie
- ✅ Control total
- ✅ Poate învăța mâncăruri românești (sarmale, mici, etc.)

### Dezavantaje
- ❌ Necesită timp (zile de training)
- ❌ Necesită GPU puternic
- ❌ Necesită cunoștințe ML

---

## 🎯 RECOMANDAREA MEA pentru tine

### Opțiunea 1: Model Dual (Food-101 + ImageNet)

**De ce:**
- Simplu de implementat (10-15 min)
- Funcționează instant
- NU necesită GPU sau training

**Cod gata de implementat:**

```python
# backend/routers/predict.py

# La început, încarcă AMBELE modele
FOOD_MODEL = AutoModelForImageClassification.from_pretrained('nateraw/food')
INGREDIENT_MODEL = AutoModelForImageClassification.from_pretrained('google/vit-base-patch16-224')

food_processor = AutoImageProcessor.from_pretrained('nateraw/food')
ingredient_processor = AutoImageProcessor.from_pretrained('google/vit-base-patch16-224')

# În endpoint
@router.post("/predict-image")
async def predict_image(file: UploadFile):
    img = ...  # load image
    
    # 1. Try Food-101
    food_inputs = food_processor(images=img, return_tensors="pt")
    with torch.no_grad():
        food_outputs = FOOD_MODEL(**food_inputs)
        food_probs = F.softmax(food_outputs.logits, dim=1)[0]
        food_top = torch.max(food_probs)
        food_idx = torch.argmax(food_probs)
        food_label = FOOD_MODEL.config.id2label[food_idx.item()]
    
    # 2. Try ImageNet (ingredients)
    ingredient_inputs = ingredient_processor(images=img, return_tensors="pt")
    with torch.no_grad():
        ingredient_outputs = INGREDIENT_MODEL(**ingredient_inputs)
        ingredient_probs = F.softmax(ingredient_outputs.logits, dim=1)[0]
        ingredient_top = torch.max(ingredient_probs)
        ingredient_idx = torch.argmax(ingredient_probs)
        ingredient_label = INGREDIENT_MODEL.config.id2label[ingredient_idx.item()]
    
    # 3. Decide care e mai bun
    if food_top > 0.50:  # Food-101 e sigur
        return build_response(food_label, food_top)
    elif ingredient_top > 0.70:  # ImageNet e sigur
        return build_response(ingredient_label, ingredient_top)
    else:
        return {"food": "Unknown"}
```

---

## 📝 Task List (când vrei să implementezi)

1. ✅ Adaugă `google/vit-base-patch16-224` în requirements.txt
2. ✅ Încarcă al doilea model în `predict.py`
3. ✅ Modifică logica de predicție (dual model)
4. ✅ Adaugă mapare pentru ingredient labels
5. ✅ Testează cu: măr, banană, roșie, cartof

---

**NU TREBUIE SĂ IMPLEMENTEZI ACUM** - doar când vrei! 😊
