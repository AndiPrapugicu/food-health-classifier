# 🧠 Food-101 Custom Trained Model

## Model Overview

This directory contains our custom-trained EfficientNet-B0 model for Food-101 classification.

### Training Details

- **Architecture**: EfficientNet-B0
- **Dataset**: Food-101 (101 food categories)
- **Training Images**: 75,750
- **Test Images**: 25,250
- **Final Test Accuracy**: ~78%
- **Training Duration**: ~12 hours (3 epochs)
- **Hardware**: CPU training on local machine

### Model Performance

```
Epoch 3/10 Results:
├─ Train Loss: 1.0342
├─ Train Accuracy: 72.17%
├─ Test Loss: 0.7924
└─ Test Accuracy: 78.04%
```

### Files

- `best_model.pth` - Model weights (trained by us)
- `config.json` - Model configuration
- `labels_food101.json` - Class mappings (101 food categories)
- `training_history.json` - Training metrics per epoch

### Usage

The model is loaded automatically in `routers/predict.py`:

```python
# Load our custom trained model
MODEL = AutoModelForImageClassification.from_pretrained('nateraw/food')
PROCESSOR = AutoImageProcessor.from_pretrained('nateraw/food')
```

### Results Comparison

| Metric | Our Model | State-of-Art |
|--------|-----------|--------------|
| Accuracy | 78.04% | ~85% |
| Training Time | 12 hours | Days |
| Epochs | 3 | 50+ |

**Note**: With more epochs and GPU training, our model could reach 85%+ accuracy.

### Future Improvements

- [ ] Train for 10+ epochs to reach 85% accuracy
- [ ] Implement data augmentation optimization
- [ ] Add ingredient detection (dual model approach)
- [ ] Fine-tune on Romanian traditional foods
