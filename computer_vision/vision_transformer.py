"""
Vision Transformer (ViT) Module
================================

Classify images using a pretrained Vision Transformer (ViT)
from Hugging Face Transformers.

Can be used as a demo or imported in other scripts.

Source:
https://huggingface.co/docs/transformers/model_doc/vit
"""

try:
    import requests
    import torch
    from io import BytesIO
    from PIL import Image
    from transformers import ViTForImageClassification, ViTImageProcessor
except ImportError as e:
    raise ImportError(
        "This module requires 'torch', 'transformers', 'PIL', and 'requests'. "
        "Install them with: pip install torch transformers pillow requests"
    ) from e


def classify_image(image: Image.Image) -> str:
    """Classify a PIL image using pretrained ViT."""
    processor = ViTImageProcessor.from_pretrained("google/vit-base-patch16-224")
    model = ViTForImageClassification.from_pretrained("google/vit-base-patch16-224")

    inputs = processor(images=image, return_tensors="pt")

    with torch.no_grad():
        outputs = model(**inputs)
        logits = outputs.logits

    predicted_class_idx = logits.argmax(-1).item()
    return model.config.id2label[predicted_class_idx]


def demo(url: str = None) -> None:
    """
    Run a demo using a sample image or provided URL.

    Args:
        url (str): URL of the image. If None, uses a default cat image.
    """
    if url is None:
        url = "https://images.unsplash.com/photo-1592194996308-7b43878e84a6"  # default example image

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        image = Image.open(BytesIO(response.content))
    except Exception as e:
        print(f"Failed to load image from {url}. Error: {e}")
        return

    label = classify_image(image)
    print(f"Predicted label: {label}")


if __name__ == "__main__":
    demo()
