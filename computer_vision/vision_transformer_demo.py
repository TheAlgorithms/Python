"""
Vision Transformer (ViT) Image Classification Demo

This module demonstrates how to use a pre-trained Vision Transformer (ViT) model
from Hugging Face for image classification tasks.

Vision Transformers apply the transformer architecture (originally designed for NLP)
to computer vision by splitting images into patches and processing them with
self-attention mechanisms.

Requirements:
    - torch
    - transformers
    - Pillow (PIL)
    - httpx (already in repo dependencies)

Resources:
    - Paper: https://arxiv.org/abs/2010.11929
    - Hugging Face: https://huggingface.co/docs/transformers/model_doc/vit

Example Usage:
    from computer_vision.vision_transformer_demo import classify_image

    # Classify an image from URL
    url = "http://images.cocodataset.org/val2017/000000039769.jpg"
    result = classify_image(url)
    print(f"Predicted: {result['label']} (confidence: {result['score']:.2%})")

    # Classify a local image
    result = classify_image("path/to/image.jpg", top_k=3)
    for pred in result['top_k_predictions']:
        print(f"{pred['label']}: {pred['score']:.2%}")
"""

from __future__ import annotations

import sys
from io import BytesIO
from pathlib import Path
from typing import Any

try:
    import httpx
    import torch
    from PIL import Image
    from transformers import ViTForImageClassification, ViTImageProcessor
except ImportError as e:
    print(f"Error: Missing required dependency: {e.name}")
    print("Install dependencies: pip install torch transformers pillow httpx")
    sys.exit(1)


def load_image(image_source: str | Path, timeout: int = 10) -> Image.Image:
    """
    Load an image from a URL or local file path.

    Args:
        image_source: URL string or Path object to the image
        timeout: Network timeout in seconds (default: 10)

    Returns:
        PIL Image object

    Raises:
    TimeoutError: If request times out
    ConnectionError: If URL is unreachable
        FileNotFoundError: If local file doesn't exist
        IOError: If image cannot be opened

    Examples:
        >>> # Test with non-existent file
        >>> try:
        ...     load_image("nonexistent_file.jpg")
        ... except FileNotFoundError:
        ...     print("File not found")
        File not found
    """
    if isinstance(image_source, (str, Path)) and str(image_source).startswith(
        ("http://", "https://")
    ):
        try:
            with httpx.Client(timeout=timeout) as client:
                response = client.get(str(image_source))
                response.raise_for_status()
                return Image.open(BytesIO(response.content)).convert("RGB")
        except httpx.TimeoutException:
            msg = (
                f"Request timed out after {timeout} seconds. "
                "Try increasing the timeout parameter."
            )
            raise TimeoutError(msg)
        except httpx.HTTPError as e:
            msg = f"Failed to download image from URL: {e}"
            raise ConnectionError(msg) from e
    else:
        # Load from local file
        file_path = Path(image_source)
        if not file_path.exists():
            msg = f"Image file not found: {file_path}"
            raise FileNotFoundError(msg)
        return Image.open(file_path).convert("RGB")


def classify_image(
    image_source: str | Path,
    model_name: str = "google/vit-base-patch16-224",
    top_k: int = 1,
) -> dict[str, Any]:
    """
    Classify an image using a Vision Transformer model.

    Args:
        image_source: URL or local path to the image
        model_name: Hugging Face model identifier (default: google/vit-base-patch16-224)
        top_k: Number of top predictions to return (default: 1)

    Returns:
        Dictionary containing:
            - label: Predicted class label
            - score: Confidence score (0-1)
            - top_k_predictions: List of top-k predictions (if top_k > 1)

    Raises:
        ValueError: If top_k is less than 1
        FileNotFoundError: If image file doesn't exist
        ConnectionError: If unable to download from URL

    Examples:
        >>> # Test parameter validation
        >>> try:
        ...     classify_image("test.jpg", top_k=0)
        ... except ValueError as e:
        ...     print("Invalid top_k")
        Invalid top_k
    """
    if top_k < 1:
        raise ValueError("top_k must be at least 1")
    # Load image
    image = load_image(image_source)

    # Load pre-trained model and processor
    # Using context manager pattern for better resource management
    processor = ViTImageProcessor.from_pretrained(model_name)
    model = ViTForImageClassification.from_pretrained(model_name)

    # Preprocess image
    inputs = processor(images=image, return_tensors="pt")

    # Perform inference
    with torch.no_grad():  # Disable gradient calculation for inference
        outputs = model(**inputs)
        logits = outputs.logits

    # Get predictions
    probabilities = torch.nn.functional.softmax(logits, dim=-1)
    top_k_probs, top_k_indices = torch.topk(probabilities, k=top_k, dim=-1)

    # Format results
    predictions = []
    for prob, idx in zip(top_k_probs[0], top_k_indices[0]):
        predictions.append(
            {"label": model.config.id2label[idx.item()], "score": prob.item()}
        )

    result = {
        "label": predictions[0]["label"],
        "score": predictions[0]["score"],
        "top_k_predictions": predictions if top_k > 1 else None,
    }

    return result


def main() -> None:
    """
    Main function demonstrating Vision Transformer usage.

    Downloads a sample image and performs classification.
    """
    print("Vision Transformer (ViT) Image Classification Demo")
    print("=" * 60)

    # Sample image URL (two cats on a couch from COCO dataset)
    image_url = "http://images.cocodataset.org/val2017/000000039769.jpg"

    print(f"\nLoading image from: {image_url}")

    try:
        # Get top-3 predictions
        result = classify_image(image_url, top_k=3)

        print(f"\n{'Prediction Results':^60}")
        print("-" * 60)
        print(f"Top Prediction: {result['label']}")
        print(f"Confidence: {result['score']:.2%}")

        if result["top_k_predictions"]:
            print(f"\n{'Top 3 Predictions':^60}")
            print("-" * 60)
            for i, pred in enumerate(result["top_k_predictions"], 1):
                print(f"{i}. {pred['label']:<40} {pred['score']:>6.2%}")

        # Example with local image (commented out)
        print("\n" + "=" * 60)
        print("To classify a local image, use:")
        print('  result = classify_image("path/to/your/image.jpg")')
        print("  print(f\"Predicted: {result['label']}\")")

    except TimeoutError as e:
        print(f"\nError: {e}")
        print("Please check your internet connection and try again.")
    except ConnectionError as e:
        print(f"\nError: {e}")
    except Exception as e:
        print(f"\nUnexpected error: {e}")
        raise


if __name__ == "__main__":
    main()
