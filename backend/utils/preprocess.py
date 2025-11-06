"""Image preprocessing helpers.

Provides a simple, well-scoped helper that converts raw image bytes into a
PyTorch tensor shaped (1, C, H, W) suitable for MobileNetV2 inference.

This function raises ImportError if torch/torchvision/Pillow are not
available so callers can fall back to a dummy path.
"""

from typing import Any


def preprocess_image_bytes(image_bytes: bytes) -> Any:
    """Decode bytes -> RGB PIL image -> normalized torch.Tensor (1,C,224,224).

    Uses torchvision transforms: Resize(256) -> CenterCrop(224) -> ToTensor -> Normalize
    matching standard ImageNet preprocessing for MobileNetV2.

    Returns:
        torch.Tensor with shape (1, C, H, W)

    Raises:
        ImportError: when required libraries are not installed.
        Exception: for other decoding/transform errors.
    """
    try:
        from PIL import Image
    except Exception as e:
        raise ImportError("Pillow is required for image preprocessing") from e

    try:
        import torch
        from torchvision import transforms
    except Exception as e:
        raise ImportError("torch and torchvision are required for preprocessing") from e

    try:
        img = Image.open(__import__('io').BytesIO(image_bytes)).convert("RGB")

        transform = transforms.Compose([
            transforms.Resize(256),
            transforms.CenterCrop(224),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
        ])

        tensor = transform(img).unsqueeze(0)  # 1,C,H,W
        return tensor
    except Exception:
        # Let caller decide how to handle transform failures
        raise
