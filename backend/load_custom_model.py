"""
Exemplu: Cum să încarci modelul custom antrenat în predict.py
Copiază acest cod în routers/predict.py după ce ai antrenat modelul
"""
import torch
import timm
import json
from pathlib import Path
from PIL import Image
import torchvision.transforms as transforms

# ========== ÎNCARCĂ MODELUL CUSTOM ==========
def load_custom_model():
    """Încarcă modelul custom antrenat"""
    model_dir = Path("model")
    
    # Încarcă configurația
    with open(model_dir / "config.json", "r") as f:
        config = json.load(f)
    
    # Încarcă labels
    with open(model_dir / "labels_food101.json", "r") as f:
        labels_data = json.load(f)
        id2label = {int(k): v for k, v in labels_data["id2label"].items()}
    
    # Creează modelul
    model = timm.create_model(
        config["model_type"], 
        pretrained=False, 
        num_classes=config["num_classes"]
    )
    
    # Încarcă weights
    model.load_state_dict(torch.load(model_dir / "best_model.pth", map_location="cpu"))
    model.eval()
    
    print(f"✅ Custom model loaded!")
    print(f"   - Architecture: {config['model_type']}")
    print(f"   - Classes: {config['num_classes']}")
    print(f"   - Best accuracy: {config['best_accuracy']:.2f}%")
    
    return model, id2label, config

# ========== PREPROCESSING ==========
def get_transform():
    """Transform pentru preprocessing imagini (identic cu cel din training)"""
    return transforms.Compose([
        transforms.Resize((256, 256)),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
    ])

# ========== PREDICȚIE ==========
def predict_with_custom_model(image_path_or_pil, model, id2label, transform):
    """
    Face predicție cu modelul custom
    
    Args:
        image_path_or_pil: Path la imagine sau PIL Image
        model: Modelul PyTorch
        id2label: Dict cu mapping id -> label
        transform: Transformare pentru preprocessing
    
    Returns:
        dict cu predicții
    """
    # Încarcă imaginea
    if isinstance(image_path_or_pil, str) or isinstance(image_path_or_pil, Path):
        img = Image.open(image_path_or_pil).convert("RGB")
    else:
        img = image_path_or_pil
    
    # Preprocessing
    img_tensor = transform(img).unsqueeze(0)  # Add batch dimension
    
    # Predicție
    with torch.no_grad():
        outputs = model(img_tensor)
        probs = torch.nn.functional.softmax(outputs, dim=1)[0]
        
        # Top 5 predictions
        top5_probs, top5_indices = torch.topk(probs, k=5)
        
        results = []
        for prob, idx in zip(top5_probs, top5_indices):
            label = id2label[idx.item()]
            results.append({
                "label": label,
                "score": round(prob.item(), 4)
            })
    
    return results

# ========== EXEMPLU DE UTILIZARE ==========
if __name__ == "__main__":
    # Încarcă modelul
    model, id2label, config = load_custom_model()
    transform = get_transform()
    
    print("\n🧪 Testing model...")
    print("=" * 70)
    
    # Test pe o imagine (înlocuiește cu path-ul tău)
    test_image = "data/food101_split/test/apple_pie/1005649.jpg"
    
    if Path(test_image).exists():
        results = predict_with_custom_model(test_image, model, id2label, transform)
        
        print(f"\n📸 Predictions for: {test_image}")
        print(f"\n🎯 Top 5 predictions:")
        for i, pred in enumerate(results, 1):
            print(f"   {i}. {pred['label']}: {pred['score']*100:.2f}%")
    else:
        print(f"⚠️  Test image not found: {test_image}")
        print("   Train the model first with 'python train_model.py'")

# ========== COD PENTRU predict.py ==========
"""
COPIAZĂ ACEST COD ÎN routers/predict.py:

# La început (după imports):
import timm
import torchvision.transforms as transforms

# Înlocuiește încărcarea modelului HuggingFace cu:
def load_custom_model():
    model_dir = Path(__file__).resolve().parents[1] / "model"
    
    with open(model_dir / "config.json", "r") as f:
        config = json.load(f)
    
    with open(model_dir / "labels_food101.json", "r") as f:
        labels_data = json.load(f)
        id2label = {int(k): v for k, v in labels_data["id2label"].items()}
    
    model = timm.create_model(
        config["model_type"], 
        pretrained=False, 
        num_classes=config["num_classes"]
    )
    model.load_state_dict(torch.load(model_dir / "best_model.pth", map_location="cpu"))
    model.eval()
    
    return model, id2label

MODEL, ID2LABEL = load_custom_model()

TRANSFORM = transforms.Compose([
    transforms.Resize((256, 256)),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
])

# În endpoint-ul /predict-image:
@router.post("/predict-image")
async def predict_image(file: UploadFile = File(...)):
    img_bytes = await file.read()
    img = Image.open(io.BytesIO(img_bytes)).convert("RGB")
    
    # Preprocessing
    img_tensor = TRANSFORM(img).unsqueeze(0)
    
    # Predicție
    with torch.no_grad():
        outputs = MODEL(img_tensor)
        probs = F.softmax(outputs, dim=1)[0]
        top5 = torch.topk(probs, k=5)
    
    results = []
    for score, idx in zip(top5.values, top5.indices):
        label = ID2LABEL[idx.item()]
        results.append({"label": label, "score": round(score.item(), 4)})
    
    # ... rest of the code (health index, etc.)
"""
