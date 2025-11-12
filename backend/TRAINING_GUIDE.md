# 🎓 Training Your Own Food-101 Model

## 📋 Overview

This guide will help you train your own Food-101 classification model from scratch using PyTorch and EfficientNet-B0.

---

## ⚡ Quick Start (3 Steps)

```powershell
# Step 1: Download Food-101 dataset (~5GB, 10-30 min)
python download_dataset.py

# Step 2: Prepare train/test splits (~5-10 min)
python prepare_dataset.py

# Step 3: Train the model (3-8 hours depending on GPU)
python train_model.py
```

---

## 📊 System Requirements

### Minimum (CPU training)
- **RAM**: 8GB
- **Storage**: 10GB free space
- **Time**: ~8-12 hours training

### Recommended (GPU training)
- **RAM**: 16GB
- **GPU**: NVIDIA GPU with 6GB+ VRAM (GTX 1060, RTX 2060, or better)
- **Storage**: 10GB free space
- **Time**: ~3-5 hours training

---

## 🔍 Detailed Steps

### Step 1: Download Dataset

```powershell
cd backend
python download_dataset.py
```

**What it does:**
- Downloads Food-101 dataset from official source (~5GB)
- Extracts to `data/food-101/`
- Contains 101,000 images (101 food classes, 1000 images each)

**Expected output:**
```
📥 DOWNLOADING FOOD-101 DATASET
[██████████████████████████] 100% (5.00GB / 5.00GB)
✅ Download complete!
📦 Extracting dataset...
✅ DATASET READY!
```

### Step 2: Prepare Dataset

```powershell
python prepare_dataset.py
```

**What it does:**
- Organizes images into PyTorch-compatible structure
- Creates train/test splits (75,750 train / 25,250 test)
- Saves class mappings in JSON format

**Expected output:**
```
📁 PREPARING TRAIN/TEST SPLITS
Train images: 100%|████████████| 75750/75750
Test images:  100%|████████████| 25250/25250
✅ DATASET PREPARATION COMPLETE!
```

**Folder structure after:**
```
data/
└── food101_split/
    ├── train/
    │   ├── apple_pie/
    │   ├── baby_back_ribs/
    │   └── ... (101 classes)
    ├── test/
    │   ├── apple_pie/
    │   ├── baby_back_ribs/
    │   └── ... (101 classes)
    ├── classes.json
    └── class_mapping.json
```

### Step 3: Train Model

```powershell
python train_model.py
```

**What it does:**
- Trains EfficientNet-B0 from scratch
- Uses data augmentation (flips, rotations, color jitter)
- Saves best model based on test accuracy
- Creates checkpoints every 5 epochs

**Expected output (per epoch):**
```
==================================================
Epoch 1/10
==================================================
Training: 100%|████████| 2367/2367 [23:45<00:00]
Testing:  100%|████████| 789/789 [03:12<00:00]

📊 Epoch 1 Summary:
   ├─ Train Loss: 3.2145 | Train Acc: 28.54%
   ├─ Test Loss:  2.8734 | Test Acc:  35.67%
   ├─ Learning Rate: 0.001000
   └─ Time: 1618.3s

✅ New best model saved! Test Acc: 35.67%
```

**Training time estimates:**
- **CPU (Intel i5/i7)**: ~8-12 hours
- **GPU (GTX 1060)**: ~5-7 hours
- **GPU (RTX 3060)**: ~3-4 hours
- **GPU (RTX 4090)**: ~1-2 hours

**Files created:**
```
model/
├── best_model.pth              # Best model weights
├── config.json                 # Model configuration
├── training_history.json       # Loss/accuracy per epoch
├── labels_food101.json         # Class mappings
└── checkpoint_epoch_5.pth      # Checkpoint (every 5 epochs)
```

---

## 🎯 Expected Accuracy

| Epochs | Expected Test Accuracy |
|--------|------------------------|
| 5      | ~60-70%               |
| 10     | ~75-80%               |
| 20     | ~80-85%               |
| 30+    | ~85-88%               |

**Note:** Food-101 is challenging! State-of-the-art models reach ~85-90% accuracy.

---

## 🔧 Configuration Options

Edit `train_model.py` to customize:

```python
BATCH_SIZE = 32      # Reduce to 16 if out of memory
NUM_EPOCHS = 10      # Increase for better accuracy
LEARNING_RATE = 0.001  # Default works well
NUM_WORKERS = 4      # Set to 0 if having issues
```

---

## 📦 Using Your Trained Model

After training, update `routers/predict.py` to use your model:

```python
# See load_custom_model.py for complete example

import timm
import torchvision.transforms as transforms

# Load custom model
def load_custom_model():
    with open("model/config.json", "r") as f:
        config = json.load(f)
    
    with open("model/labels_food101.json", "r") as f:
        labels_data = json.load(f)
        id2label = {int(k): v for k, v in labels_data["id2label"].items()}
    
    model = timm.create_model(
        config["model_type"], 
        pretrained=False, 
        num_classes=config["num_classes"]
    )
    model.load_state_dict(torch.load("model/best_model.pth", map_location="cpu"))
    model.eval()
    
    return model, id2label

MODEL, ID2LABEL = load_custom_model()
```

---

## ⚠️ Troubleshooting

### Out of Memory (OOM)
```python
# Reduce batch size in train_model.py
BATCH_SIZE = 16  # or even 8
```

### Slow training on CPU
- This is normal! Food-101 is large
- Consider using Google Colab (free GPU)
- Or reduce NUM_EPOCHS for faster testing

### "Dataset not found" error
```powershell
# Make sure you ran step 1 and 2 first
python download_dataset.py
python prepare_dataset.py
```

### CUDA out of memory
```python
# In train_model.py, reduce batch size:
BATCH_SIZE = 16  # or 8
```

---

## 🚀 Advanced: Training on GPU

### Check if GPU is available:
```powershell
python -c "import torch; print(f'CUDA available: {torch.cuda.is_available()}'); print(f'GPU: {torch.cuda.get_device_name(0) if torch.cuda.is_available() else 'None'}')"
```

### Install CUDA version of PyTorch (if needed):
```powershell
# For CUDA 11.8
pip install torch torchvision --index-url https://download.pytorch.org/whl/cu118

# For CUDA 12.1
pip install torch torchvision --index-url https://download.pytorch.org/whl/cu121
```

---

## 📈 Monitoring Training

Training creates `model/training_history.json` with:
- Train/test loss per epoch
- Train/test accuracy per epoch
- Learning rate schedule

You can plot this data to visualize training progress!

---

## 🎓 What You're Learning

By training this model, you're learning:
- ✅ Deep learning with PyTorch
- ✅ Transfer learning with EfficientNet
- ✅ Data augmentation techniques
- ✅ Model evaluation and validation
- ✅ Hyperparameter tuning

---

## 📚 Additional Resources

- [Food-101 Dataset Paper](https://data.vision.ee.ethz.ch/cvl/datasets_extra/food-101/)
- [EfficientNet Paper](https://arxiv.org/abs/1905.11946)
- [PyTorch Documentation](https://pytorch.org/docs/)
- [TIMM Library](https://github.com/rwightman/pytorch-image-models)

---

## 🎯 Next Steps

After training:
1. ✅ Test your model: `python load_custom_model.py`
2. ✅ Update `predict.py` to use your model
3. ✅ Run the backend: `uvicorn app:app --reload`
4. ✅ Test with frontend!

Good luck with your training! 🚀
