"""Test script pentru a verifica modelul HuggingFace"""
print("🔍 Testăm modelul de la HuggingFace...")

try:
    from transformers import AutoImageProcessor, AutoModelForImageClassification
    
    print("✅ Import reușit!")
    
    MODEL_NAME = "nateraw/food"
    print(f"📦 Încărcăm modelul: {MODEL_NAME}")
    
    processor = AutoImageProcessor.from_pretrained(MODEL_NAME)
    model = AutoModelForImageClassification.from_pretrained(MODEL_NAME)
    
    print(f"✅ Model încărcat cu succes!")
    print(f"📊 Număr de clase: {len(model.config.id2label)}")
    
    # Căutăm pizza
    pizza_found = False
    for idx, label in model.config.id2label.items():
        if "pizza" in label.lower():
            print(f"🍕 Pizza găsită la index {idx}: {label}")
            pizza_found = True
    
    if not pizza_found:
        print("❌ Pizza nu a fost găsită în clase!")
        print("Primele 20 clase sunt:")
        for i in range(min(20, len(model.config.id2label))):
            print(f"  {i}: {model.config.id2label[i]}")
    
except Exception as e:
    print(f"❌ Eroare: {e}")
    import traceback
    traceback.print_exc()
