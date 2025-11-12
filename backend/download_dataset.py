"""
Descarcă și pregătește Food-101 dataset pentru training
Dataset oficial: https://data.vision.ee.ethz.ch/cvl/datasets_extra/food-101/
"""
import os
import urllib.request
import tarfile
from pathlib import Path

DATASET_URL = "http://data.vision.ee.ethz.ch/cvl/food-101.tar.gz"
DOWNLOAD_PATH = Path("data/food-101.tar.gz")
EXTRACT_PATH = Path("data/")

def download_food101():
    """Descarcă Food-101 dataset (5GB)"""
    print("="*70)
    print("📥 DOWNLOADING FOOD-101 DATASET")
    print("="*70)
    print(f"Source: {DATASET_URL}")
    print(f"Size: ~5 GB")
    print(f"Destination: {EXTRACT_PATH.absolute()}")
    print("⏳ This will take 10-30 minutes depending on your internet speed...")
    print()
    
    # Creează directorul data dacă nu există
    DOWNLOAD_PATH.parent.mkdir(parents=True, exist_ok=True)
    
    # Verifică dacă dataset-ul există deja
    if (EXTRACT_PATH / "food-101").exists():
        print("✅ Dataset already exists at:", EXTRACT_PATH / "food-101")
        response = input("Do you want to re-download? (y/n): ")
        if response.lower() != 'y':
            print("Skipping download.")
            return
    
    # Download with progress bar
    def progress(block_num, block_size, total_size):
        downloaded = block_num * block_size
        percent = min(downloaded / total_size * 100, 100)
        downloaded_gb = downloaded / 1e9
        total_gb = total_size / 1e9
        bar_length = 50
        filled = int(bar_length * percent / 100)
        bar = '█' * filled + '░' * (bar_length - filled)
        print(f"\r  [{bar}] {percent:.1f}% ({downloaded_gb:.2f}GB / {total_gb:.2f}GB)", end="")
    
    try:
        urllib.request.urlretrieve(DATASET_URL, DOWNLOAD_PATH, reporthook=progress)
        print("\n✅ Download complete!")
    except Exception as e:
        print(f"\n❌ Download failed: {e}")
        return
    
    # Extract
    print("\n📦 Extracting dataset...")
    try:
        with tarfile.open(DOWNLOAD_PATH, "r:gz") as tar:
            tar.extractall(EXTRACT_PATH)
        print("✅ Extraction complete!")
    except Exception as e:
        print(f"❌ Extraction failed: {e}")
        return
    
    # Cleanup
    print("🧹 Cleaning up...")
    DOWNLOAD_PATH.unlink()
    
    print("\n" + "="*70)
    print("✅ DATASET READY!")
    print("="*70)
    print(f"Location: {(EXTRACT_PATH / 'food-101').absolute()}")
    
    # Show structure
    train_dir = EXTRACT_PATH / "food-101" / "images"
    if train_dir.exists():
        num_classes = len(list(train_dir.iterdir()))
        print(f"\n📊 Dataset Statistics:")
        print(f"   ├─ Classes: {num_classes}")
        print(f"   ├─ Total images: ~101,000")
        print(f"   ├─ Train images: ~75,750 (750 per class)")
        print(f"   └─ Test images: ~25,250 (250 per class)")
        print("\n🎯 Next step: Run 'python prepare_dataset.py' to organize the data")
    else:
        print("⚠️  Warning: Could not find images directory")

if __name__ == "__main__":
    try:
        download_food101()
    except KeyboardInterrupt:
        print("\n\n⚠️  Download interrupted by user")
    except Exception as e:
        print(f"\n❌ Error: {e}")
