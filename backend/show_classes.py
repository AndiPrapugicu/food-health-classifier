"""
Script pentru a arăta toate clasele Food-101 disponibile
"""
from transformers import AutoModelForImageClassification

print("🍕 Loading Food-101 model...")
model = AutoModelForImageClassification.from_pretrained('nateraw/food')

print(f"\n📊 Total classes: {len(model.config.id2label)}\n")
print("=" * 60)
print("TOATE CLASELE DISPONIBILE ÎN FOOD-101:")
print("=" * 60)

# Sortăm alfabetic pentru ușurință
classes = sorted(model.config.id2label.values())

for i, cls in enumerate(classes, 1):
    print(f"{i:3d}. {cls}")

print("\n" + "=" * 60)
print("💡 NOTĂ: Food-101 conține doar MÂNCĂRURI PREPARATE!")
print("   Nu conține ingrediente simple (mere, roșii, cartofi cruzi, etc.)")
print("=" * 60)
