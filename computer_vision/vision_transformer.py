"""
Vision Transformer (ViT)
========================

This module demonstrates how to use a pretrained Vision Transformer (ViT)
for image classification using Hugging Face's Transformers library.

Source:
https://huggingface.co/docs/transformers/model_doc/vit
"""

import requests
import torch
from PIL import Image
from transformers import ViTForImageClassification, ViTImageProcessor


def vision_transformer_demo() -> None:
    """
    Demonstrates Vision Transformer (ViT) on a sample image.

    Example:
        >>> vision_transformer_demo()  # doctest: +SKIP
        Predicted label: tabby, tabby cat
    """
    url = "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/cat_sample.jpeg"
    image = Image.open(requests.get(url, stream=True, timeout=10).raw)

    processor = ViTImageProcessor.from_pretrained("google/vit-base-patch16-224")
    model = ViTForImageClassification.from_pretrained("google/vit-base-patch16-224")

    inputs = processor(images=image, return_tensors="pt")

    with torch.no_grad():
        outputs = model(**inputs)
        logits = outputs.logits

    predicted_class_idx = logits.argmax(-1).item()
    predicted_label = model.config.id2label[predicted_class_idx]

    print(f"Predicted label: {predicted_label}")


if __name__ == "__main__":
    vision_transformer_demo()
