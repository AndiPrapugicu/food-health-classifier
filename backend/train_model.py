"""
Antrenează un model EfficientNet-B0 pe Food-101 dataset
Rezultat: model antrenat salvat în model/best_model.pth
"""
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader
from torchvision import datasets, transforms
import timm
from pathlib import Path
import json
from tqdm import tqdm
import time

# ========== CONFIGURAȚIE ==========
DATA_ROOT = Path("data/food101_split")
SAVE_DIR = Path("model")
SAVE_DIR.mkdir(exist_ok=True)

BATCH_SIZE = 32  # Reduce la 16 dacă ai probleme cu memoria
NUM_EPOCHS = 10  # Poți face mai multe pentru acuratețe mai mare (20-30 epochs ideal)
LEARNING_RATE = 0.001
NUM_WORKERS = 4  # Paralel data loading (reduce la 0 dacă ai probleme)

DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")

def main():
    print("="*70)
    print("🧠 FOOD-101 MODEL TRAINING")
    print("="*70)
    print(f"Device: {DEVICE}")
    print(f"Batch size: {BATCH_SIZE}")
    print(f"Epochs: {NUM_EPOCHS}")
    print(f"Learning rate: {LEARNING_RATE}")
    print()
    
    # Verifică dacă dataset-ul există
    if not DATA_ROOT.exists():
        print(f"❌ Error: Dataset not found at {DATA_ROOT.absolute()}")
        print("   Please run 'python prepare_dataset.py' first!")
        return
    
    # ========== TRANSFORMĂRI IMAGINI ==========
    print("🖼️  Setting up image transformations...")
    
    # Transformări pentru TRAINING (cu augmentări)
    train_transform = transforms.Compose([
        transforms.Resize((256, 256)),
        transforms.RandomCrop(224),
        transforms.RandomHorizontalFlip(),
        transforms.RandomRotation(10),
        transforms.ColorJitter(brightness=0.2, contrast=0.2, saturation=0.2),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
    ])
    
    # Transformări pentru TEST (fără augmentări)
    test_transform = transforms.Compose([
        transforms.Resize((256, 256)),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
    ])
    
    # ========== ÎNCARCĂ DATASET ==========
    print("📂 Loading datasets...")
    try:
        train_dataset = datasets.ImageFolder(DATA_ROOT / "train", transform=train_transform)
        test_dataset = datasets.ImageFolder(DATA_ROOT / "test", transform=test_transform)
    except Exception as e:
        print(f"❌ Error loading dataset: {e}")
        return
    
    train_loader = DataLoader(
        train_dataset, 
        batch_size=BATCH_SIZE, 
        shuffle=True, 
        num_workers=NUM_WORKERS,
        pin_memory=True if DEVICE.type == 'cuda' else False
    )
    test_loader = DataLoader(
        test_dataset, 
        batch_size=BATCH_SIZE, 
        shuffle=False, 
        num_workers=NUM_WORKERS,
        pin_memory=True if DEVICE.type == 'cuda' else False
    )
    
    num_classes = len(train_dataset.classes)
    print(f"✅ Dataset loaded:")
    print(f"   ├─ Train images: {len(train_dataset)}")
    print(f"   ├─ Test images: {len(test_dataset)}")
    print(f"   ├─ Classes: {num_classes}")
    print(f"   └─ Batches per epoch: {len(train_loader)}")
    print()
    
    # ========== CREEAZĂ MODEL ==========
    print("🧠 Creating model...")
    try:
        model = timm.create_model('efficientnet_b0', pretrained=True, num_classes=num_classes)
        model = model.to(DEVICE)
    except Exception as e:
        print(f"❌ Error creating model: {e}")
        return
    
    total_params = sum(p.numel() for p in model.parameters())
    trainable_params = sum(p.numel() for p in model.parameters() if p.requires_grad)
    print(f"✅ Model: EfficientNet-B0")
    print(f"   ├─ Total parameters: {total_params:,}")
    print(f"   └─ Trainable parameters: {trainable_params:,}")
    print()
    
    # Loss function și optimizer
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=LEARNING_RATE)
    scheduler = optim.lr_scheduler.ReduceLROnPlateau(optimizer, mode='max', factor=0.5, patience=2)
    
    # ========== TRAINING LOOP ==========
    best_accuracy = 0.0
    training_history = {
        "train_loss": [],
        "train_acc": [],
        "test_loss": [],
        "test_acc": [],
        "learning_rates": []
    }
    
    print("🚀 Starting training...")
    print("="*70)
    start_time = time.time()
    
    for epoch in range(NUM_EPOCHS):
        epoch_start = time.time()
        print(f"\n{'='*70}")
        print(f"Epoch {epoch+1}/{NUM_EPOCHS}")
        print(f"{'='*70}")
        
        # ===== TRAINING PHASE =====
        model.train()
        train_loss = 0.0
        train_correct = 0
        train_total = 0
        
        train_bar = tqdm(train_loader, desc="Training", ncols=100, leave=False)
        for images, labels in train_bar:
            images, labels = images.to(DEVICE), labels.to(DEVICE)
            
            # Forward pass
            outputs = model(images)
            loss = criterion(outputs, labels)
            
            # Backward pass
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
            
            # Statistics
            train_loss += loss.item()
            _, predicted = torch.max(outputs, 1)
            train_total += labels.size(0)
            train_correct += (predicted == labels).sum().item()
            
            # Update progress bar
            train_bar.set_postfix({
                'loss': f'{loss.item():.4f}',
                'acc': f'{100 * train_correct / train_total:.2f}%'
            })
        
        train_accuracy = 100 * train_correct / train_total
        avg_train_loss = train_loss / len(train_loader)
        
        # ===== TESTING PHASE =====
        model.eval()
        test_loss = 0.0
        test_correct = 0
        test_total = 0
        
        test_bar = tqdm(test_loader, desc="Testing", ncols=100, leave=False)
        with torch.no_grad():
            for images, labels in test_bar:
                images, labels = images.to(DEVICE), labels.to(DEVICE)
                
                outputs = model(images)
                loss = criterion(outputs, labels)
                
                test_loss += loss.item()
                _, predicted = torch.max(outputs, 1)
                test_total += labels.size(0)
                test_correct += (predicted == labels).sum().item()
                
                test_bar.set_postfix({
                    'loss': f'{loss.item():.4f}',
                    'acc': f'{100 * test_correct / test_total:.2f}%'
                })
        
        test_accuracy = 100 * test_correct / test_total
        avg_test_loss = test_loss / len(test_loader)
        
        # Update learning rate scheduler
        scheduler.step(test_accuracy)
        current_lr = optimizer.param_groups[0]['lr']
        
        # Save history
        training_history["train_loss"].append(avg_train_loss)
        training_history["train_acc"].append(train_accuracy)
        training_history["test_loss"].append(avg_test_loss)
        training_history["test_acc"].append(test_accuracy)
        training_history["learning_rates"].append(current_lr)
        
        epoch_time = time.time() - epoch_start
        
        # Print epoch summary
        print(f"\n📊 Epoch {epoch+1} Summary:")
        print(f"   ├─ Train Loss: {avg_train_loss:.4f} | Train Acc: {train_accuracy:.2f}%")
        print(f"   ├─ Test Loss:  {avg_test_loss:.4f} | Test Acc:  {test_accuracy:.2f}%")
        print(f"   ├─ Learning Rate: {current_lr:.6f}")
        print(f"   └─ Time: {epoch_time:.1f}s")
        
        # Save best model
        if test_accuracy > best_accuracy:
            best_accuracy = test_accuracy
            model_path = SAVE_DIR / "best_model.pth"
            torch.save(model.state_dict(), model_path)
            print(f"\n✅ New best model saved! Test Acc: {best_accuracy:.2f}%")
        
        # Save checkpoint every 5 epochs
        if (epoch + 1) % 5 == 0:
            checkpoint_path = SAVE_DIR / f"checkpoint_epoch_{epoch+1}.pth"
            torch.save({
                'epoch': epoch + 1,
                'model_state_dict': model.state_dict(),
                'optimizer_state_dict': optimizer.state_dict(),
                'train_acc': train_accuracy,
                'test_acc': test_accuracy,
            }, checkpoint_path)
            print(f"💾 Checkpoint saved: {checkpoint_path}")
    
    # ========== TRAINING COMPLETE ==========
    total_time = time.time() - start_time
    print("\n" + "="*70)
    print("✅ TRAINING COMPLETE!")
    print("="*70)
    print(f"Total time: {total_time/60:.1f} minutes")
    print(f"Best test accuracy: {best_accuracy:.2f}%")
    print(f"Final model saved at: {(SAVE_DIR / 'best_model.pth').absolute()}")
    
    # Save configuration
    config = {
        "model_type": "efficientnet_b0",
        "num_classes": num_classes,
        "input_size": [224, 224],
        "num_epochs": NUM_EPOCHS,
        "batch_size": BATCH_SIZE,
        "learning_rate": LEARNING_RATE,
        "best_accuracy": best_accuracy,
        "total_training_time": total_time,
        "class_names": train_dataset.classes
    }
    
    config_path = SAVE_DIR / "config.json"
    with open(config_path, "w") as f:
        json.dump(config, f, indent=2)
    print(f"Config saved at: {config_path.absolute()}")
    
    # Save training history
    history_path = SAVE_DIR / "training_history.json"
    with open(history_path, "w") as f:
        json.dump(training_history, f, indent=2)
    print(f"Training history saved at: {history_path.absolute()}")
    
    # Save class mapping for inference
    id2label = {i: class_name for i, class_name in enumerate(train_dataset.classes)}
    label2id = {class_name: i for i, class_name in enumerate(train_dataset.classes)}
    
    labels_path = SAVE_DIR / "labels_food101.json"
    with open(labels_path, "w") as f:
        json.dump({"id2label": id2label, "label2id": label2id}, f, indent=2)
    print(f"Labels saved at: {labels_path.absolute()}")
    
    print("\n🎯 Next step: Update predict.py to use your trained model!")
    print("   See: load_custom_model.py for example code")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠️  Training interrupted by user")
    except Exception as e:
        print(f"\n❌ Error during training: {e}")
        import traceback
        traceback.print_exc()
