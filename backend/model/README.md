This folder should contain the exported PyTorch model (`model.pt`) and a `class_map.json`.

Workflow:
- Train MobileNetV2 on Food-101 (outside of this repo or in a training notebook).
- Export a CPU-friendly TorchScript or state_dict to `model.pt`.
- Update backend/routers/predict.py to load `model.pt` and perform real inference.

For now this file documents where to place the exported model.
