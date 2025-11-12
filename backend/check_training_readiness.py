"""
Verifică dacă sistemul e pregătit pentru training
"""
import sys
from pathlib import Path

def check_requirements():
    """Verifică dacă toate library-urile necesare sunt instalate"""
    print("🔍 Checking Python packages...")
    
    required_packages = {
        'torch': 'PyTorch',
        'torchvision': 'TorchVision',
        'timm': 'TIMM',
        'PIL': 'Pillow',
        'tqdm': 'tqdm'
    }
    
    missing = []
    for package, name in required_packages.items():
        try:
            __import__(package)
            print(f"  ✅ {name}")
        except ImportError:
            print(f"  ❌ {name} - NOT INSTALLED")
            missing.append(name)
    
    if missing:
        print(f"\n⚠️  Missing packages: {', '.join(missing)}")
        print("   Install with: pip install torch torchvision timm pillow tqdm")
        return False
    
    return True

def check_gpu():
    """Verifică disponibilitatea GPU"""
    print("\n🖥️  Checking GPU availability...")
    
    try:
        import torch
        if torch.cuda.is_available():
            print(f"  ✅ GPU available: {torch.cuda.get_device_name(0)}")
            print(f"     - CUDA version: {torch.version.cuda}")
            print(f"     - GPU memory: {torch.cuda.get_device_properties(0).total_memory / 1e9:.1f} GB")
            return True
        else:
            print("  ⚠️  No GPU detected - training will use CPU (slower)")
            print("     Consider using Google Colab for free GPU access")
            return False
    except Exception as e:
        print(f"  ❌ Error checking GPU: {e}")
        return False

def check_disk_space():
    """Verifică spațiul disponibil pe disk"""
    print("\n💾 Checking disk space...")
    
    try:
        import shutil
        stat = shutil.disk_usage(".")
        free_gb = stat.free / 1e9
        
        print(f"  Free space: {free_gb:.1f} GB")
        
        if free_gb < 10:
            print("  ⚠️  Low disk space! Need at least 10GB for dataset and model")
            return False
        else:
            print("  ✅ Sufficient disk space")
            return True
    except Exception as e:
        print(f"  ⚠️  Could not check disk space: {e}")
        return True  # Don't fail if we can't check

def check_dataset():
    """Verifică dacă dataset-ul există"""
    print("\n📂 Checking dataset...")
    
    data_dir = Path("data/food-101")
    split_dir = Path("data/food101_split")
    
    if not data_dir.exists():
        print(f"  ❌ Raw dataset not found at {data_dir.absolute()}")
        print("     Run: python download_dataset.py")
        return False
    
    print(f"  ✅ Raw dataset found")
    
    if not split_dir.exists():
        print(f"  ⚠️  Prepared dataset not found at {split_dir.absolute()}")
        print("     Run: python prepare_dataset.py")
        return False
    
    print(f"  ✅ Prepared dataset found")
    
    # Check if splits are complete
    train_dir = split_dir / "train"
    test_dir = split_dir / "test"
    
    if train_dir.exists() and test_dir.exists():
        train_classes = len(list(train_dir.iterdir()))
        test_classes = len(list(test_dir.iterdir()))
        
        print(f"     - Train classes: {train_classes}")
        print(f"     - Test classes: {test_classes}")
        
        if train_classes != 101 or test_classes != 101:
            print("  ⚠️  Incomplete dataset! Should have 101 classes")
            return False
    
    return True

def estimate_training_time():
    """Estimează timpul de training"""
    print("\n⏱️  Estimated training time:")
    
    try:
        import torch
        if torch.cuda.is_available():
            gpu_name = torch.cuda.get_device_name(0)
            if 'RTX 40' in gpu_name or 'RTX 4' in gpu_name:
                print("  With your GPU (RTX 40-series): ~1-2 hours (10 epochs)")
            elif 'RTX 30' in gpu_name or 'RTX 3' in gpu_name:
                print("  With your GPU (RTX 30-series): ~3-4 hours (10 epochs)")
            elif 'RTX 20' in gpu_name or 'RTX 2' in gpu_name or 'GTX 16' in gpu_name:
                print("  With your GPU (RTX 20/GTX 16-series): ~5-7 hours (10 epochs)")
            else:
                print("  With your GPU: ~5-8 hours (10 epochs)")
        else:
            print("  With CPU: ~8-12 hours (10 epochs)")
            print("  💡 Tip: Use Google Colab for free GPU access!")
    except:
        print("  Could not estimate training time")

def main():
    print("="*70)
    print("🎓 FOOD-101 TRAINING READINESS CHECK")
    print("="*70)
    
    all_good = True
    
    # Check requirements
    if not check_requirements():
        all_good = False
    
    # Check GPU
    check_gpu()  # Not critical
    
    # Check disk space
    if not check_disk_space():
        all_good = False
    
    # Check dataset
    if not check_dataset():
        all_good = False
    
    # Estimate time
    estimate_training_time()
    
    # Final verdict
    print("\n" + "="*70)
    if all_good:
        print("✅ READY TO TRAIN!")
        print("="*70)
        print("\n🚀 Start training with:")
        print("   python train_model.py")
        print("\n📚 For more info, see:")
        print("   TRAINING_GUIDE.md")
    else:
        print("❌ NOT READY YET")
        print("="*70)
        print("\n📝 TODO:")
        if not Path("data/food-101").exists():
            print("   1. python download_dataset.py")
        if not Path("data/food101_split").exists():
            print("   2. python prepare_dataset.py")
        print("   3. Make sure all packages are installed")
        print("\n📚 See TRAINING_GUIDE.md for detailed instructions")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠️  Interrupted by user")
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
