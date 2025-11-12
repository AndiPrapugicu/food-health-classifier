"""
Organizează Food-101 în format PyTorch (train/test folders)
Structura finală:
    data/food101_split/
    ├── train/
    │   ├── apple_pie/
    │   ├── baby_back_ribs/
    │   └── ...
    └── test/
        ├── apple_pie/
        ├── baby_back_ribs/
        └── ...
"""
import shutil
from pathlib import Path
import json
from tqdm import tqdm

FOOD101_ROOT = Path("data/food-101")
OUTPUT_ROOT = Path("data/food101_split")

def prepare_splits():
    """Organizează imaginile în train/test splits"""
    print("="*70)
    print("📁 PREPARING TRAIN/TEST SPLITS")
    print("="*70)
    
    # Verifică dacă dataset-ul există
    if not FOOD101_ROOT.exists():
        print(f"❌ Error: Food-101 dataset not found at {FOOD101_ROOT.absolute()}")
        print("   Please run 'python download_dataset.py' first!")
        return
    
    # Verifică dacă split-ul există deja
    if OUTPUT_ROOT.exists():
        print(f"⚠️  Output directory already exists: {OUTPUT_ROOT.absolute()}")
        response = input("Do you want to recreate it? (y/n): ")
        if response.lower() != 'y':
            print("Skipping dataset preparation.")
            return
        print("🧹 Cleaning existing directory...")
        shutil.rmtree(OUTPUT_ROOT)
    
    # Citește split-urile oficiale
    meta_path = FOOD101_ROOT / "meta"
    print(f"\n📋 Reading splits from {meta_path}...")
    
    try:
        with open(meta_path / "train.json", "r") as f:
            train_files = json.load(f)
        with open(meta_path / "test.json", "r") as f:
            test_files = json.load(f)
    except FileNotFoundError as e:
        print(f"❌ Error: Could not find meta files: {e}")
        return
    
    # Creează structura de foldere
    train_dir = OUTPUT_ROOT / "train"
    test_dir = OUTPUT_ROOT / "test"
    train_dir.mkdir(parents=True, exist_ok=True)
    test_dir.mkdir(parents=True, exist_ok=True)
    
    images_dir = FOOD101_ROOT / "images"
    
    # Copiază imaginile de training
    print("\n📂 Organizing TRAINING images...")
    total_train = sum(len(files) for files in train_files.values())
    
    with tqdm(total=total_train, desc="Train images", ncols=100) as pbar:
        for class_name, files in train_files.items():
            class_dir = train_dir / class_name
            class_dir.mkdir(exist_ok=True)
            
            for file_path in files:
                src = images_dir / f"{file_path}.jpg"
                dst = class_dir / f"{Path(file_path).name}.jpg"
                
                if src.exists():
                    shutil.copy2(src, dst)
                    pbar.update(1)
                else:
                    print(f"⚠️  Warning: Missing file {src}")
    
    # Copiază imaginile de test
    print("\n📂 Organizing TEST images...")
    total_test = sum(len(files) for files in test_files.values())
    
    with tqdm(total=total_test, desc="Test images", ncols=100) as pbar:
        for class_name, files in test_files.items():
            class_dir = test_dir / class_name
            class_dir.mkdir(exist_ok=True)
            
            for file_path in files:
                src = images_dir / f"{file_path}.jpg"
                dst = class_dir / f"{Path(file_path).name}.jpg"
                
                if src.exists():
                    shutil.copy2(src, dst)
                    pbar.update(1)
                else:
                    print(f"⚠️  Warning: Missing file {src}")
    
    # Salvează lista de clase
    classes = sorted(train_files.keys())
    classes_file = OUTPUT_ROOT / "classes.json"
    with open(classes_file, "w") as f:
        json.dump(classes, f, indent=2)
    
    # Salvează mapping id2label
    id2label = {i: class_name for i, class_name in enumerate(classes)}
    label2id = {class_name: i for i, class_name in enumerate(classes)}
    
    mapping_file = OUTPUT_ROOT / "class_mapping.json"
    with open(mapping_file, "w") as f:
        json.dump({"id2label": id2label, "label2id": label2id}, f, indent=2)
    
    print("\n" + "="*70)
    print("✅ DATASET PREPARATION COMPLETE!")
    print("="*70)
    print(f"Location: {OUTPUT_ROOT.absolute()}")
    print(f"\n📊 Statistics:")
    print(f"   ├─ Classes: {len(classes)}")
    print(f"   ├─ Train images: {total_train}")
    print(f"   ├─ Test images: {total_test}")
    print(f"   ├─ Total images: {total_train + total_test}")
    print(f"   └─ Class mapping saved: {mapping_file}")
    
    print("\n🎯 Next step: Run 'python train_model.py' to start training!")
    
    # Verifică câteva clase random
    print("\n📋 Sample classes:")
    for class_name in classes[:5]:
        train_count = len(list((train_dir / class_name).glob("*.jpg")))
        test_count = len(list((test_dir / class_name).glob("*.jpg")))
        print(f"   ├─ {class_name}: {train_count} train, {test_count} test")
    print(f"   └─ ... (and {len(classes) - 5} more)")

if __name__ == "__main__":
    try:
        prepare_splits()
    except KeyboardInterrupt:
        print("\n\n⚠️  Preparation interrupted by user")
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
