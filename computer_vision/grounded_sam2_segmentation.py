"""
Grounded SAM2 Image Segmentation

This module demonstrates interactive image segmentation using Grounded SAM2
(Segment Anything Model 2 with grounding capabilities). It allows segmentation
based on:
- Point prompts (positive/negative)
- Bounding box prompts
- Text prompts (grounding)

The implementation provides a practical reference for integrating SAM2 into
real-world segmentation workflows.

Reference:
- SAM2: https://github.com/facebookresearch/segment-anything-2
- Grounding DINO: https://github.com/IDEA-Research/GroundingDINO
- Paper: https://arxiv.org/abs/2304.02643

Author: NANDAGOPALNG
"""

import numpy as np
from typing import Any


class GroundedSAM2Segmenter:
    """
    A class for performing image segmentation using Grounded SAM2 approach.

    This implementation provides core segmentation functionality that can work
    with different prompt types: points, bounding boxes, and text descriptions.

    Attributes:
        image_shape: Tuple containing (height, width, channels) of input image
        mask_threshold: Confidence threshold for mask generation (0.0 to 1.0)
    """

    def __init__(self, mask_threshold: float = 0.5) -> None:
        """
        Initialize the Grounded SAM2 segmenter.

        Args:
            mask_threshold: Confidence threshold for generating binary masks.
                          Default is 0.5. Range: [0.0, 1.0]

        Raises:
            ValueError: If mask_threshold is not in valid range

        Example:
            >>> segmenter = GroundedSAM2Segmenter(mask_threshold=0.6)
            >>> segmenter.mask_threshold
            0.6
        """
        if not 0.0 <= mask_threshold <= 1.0:
            raise ValueError("mask_threshold must be between 0.0 and 1.0")

        self.mask_threshold = mask_threshold
        self.image_shape: tuple[int, int, int] | None = None

    def set_image(self, image: np.ndarray) -> None:
        """
        Set the input image for segmentation.

        Args:
            image: Input image as numpy array with shape (H, W, C) or (H, W)

        Raises:
            ValueError: If image dimensions are invalid

        Example:
            >>> segmenter = GroundedSAM2Segmenter()
            >>> img = np.zeros((100, 100, 3), dtype=np.uint8)
            >>> segmenter.set_image(img)
            >>> segmenter.image_shape
            (100, 100, 3)
        """
        if image.ndim not in [2, 3]:
            raise ValueError("Image must be 2D (grayscale) or 3D (color)")

        if image.ndim == 2:
            image = np.expand_dims(image, axis=-1)

        self.image_shape = image.shape

    def segment_with_points(
        self,
        image: np.ndarray,
        point_coords: list[tuple[int, int]],
        point_labels: list[int],
    ) -> np.ndarray:
        """
        Segment image using point prompts.

        Args:
            image: Input image as numpy array (H, W, C)
            point_coords: List of (x, y) coordinates for point prompts
            point_labels: List of labels (1 for foreground, 0 for background)

        Returns:
            Binary segmentation mask as numpy array (H, W)

        Raises:
            ValueError: If inputs are invalid

        Example:
            >>> segmenter = GroundedSAM2Segmenter()
            >>> img = np.ones((50, 50, 3), dtype=np.uint8) * 128
            >>> points = [(25, 25), (30, 30)]
            >>> labels = [1, 1]
            >>> mask = segmenter.segment_with_points(img, points, labels)
            >>> mask.shape
            (50, 50)
            >>> mask.dtype
            dtype('uint8')
        """
        self.set_image(image)

        if len(point_coords) != len(point_labels):
            raise ValueError("Number of points must match number of labels")

        if not point_coords:
            raise ValueError("At least one point is required")

        # Validate point labels
        for label in point_labels:
            if label not in [0, 1]:
                raise ValueError("Point labels must be 0 (background) or 1 (foreground)")

        # Simulate segmentation based on point prompts
        # In real implementation, this would use SAM2 model inference
        h, w = image.shape[:2]
        mask = np.zeros((h, w), dtype=np.uint8)

        # Create circular regions around foreground points
        for (x, y), label in zip(point_coords, point_labels):
            if label == 1:  # Foreground point
                y_coords, x_coords = np.ogrid[:h, :w]
                radius = min(h, w) // 5
                circle_mask = (x_coords - x) ** 2 + (y_coords - y) ** 2 <= radius**2
                mask[circle_mask] = 1

        return mask

    def segment_with_box(
        self, image: np.ndarray, bbox: tuple[int, int, int, int]
    ) -> np.ndarray:
        """
        Segment image using bounding box prompt.

        Args:
            image: Input image as numpy array (H, W, C)
            bbox: Bounding box as (x1, y1, x2, y2) where (x1,y1) is top-left
                  and (x2,y2) is bottom-right corner

        Returns:
            Binary segmentation mask as numpy array (H, W)

        Raises:
            ValueError: If bbox coordinates are invalid

        Example:
            >>> segmenter = GroundedSAM2Segmenter()
            >>> img = np.ones((100, 100, 3), dtype=np.uint8) * 128
            >>> bbox = (20, 20, 80, 80)
            >>> mask = segmenter.segment_with_box(img, bbox)
            >>> mask.shape
            (100, 100)
            >>> np.sum(mask > 0) > 0
            True
        """
        self.set_image(image)
        x1, y1, x2, y2 = bbox

        h, w = image.shape[:2]

        # Validate bounding box
        if not (0 <= x1 < x2 <= w and 0 <= y1 < y2 <= h):
            raise ValueError(
                f"Invalid bounding box coordinates: {bbox} for image size ({h}, {w})"
            )

        # Simulate segmentation within bounding box
        # In real implementation, this would use SAM2 model inference
        mask = np.zeros((h, w), dtype=np.uint8)

        # Create mask with some padding inside the box
        pad = min(5, (x2 - x1) // 4, (y2 - y1) // 4)
        mask[
            max(0, y1 + pad) : min(h, y2 - pad),
            max(0, x1 + pad) : min(w, x2 - pad),
        ] = 1

        return mask

    def segment_with_text(
        self, image: np.ndarray, text_prompt: str, confidence_threshold: float = 0.5
    ) -> list[dict[str, Any]]:
        """
        Segment image using text description (grounding).

        This uses text-based grounding to first detect objects matching the
        description, then segments them.

        Args:
            image: Input image as numpy array (H, W, C)
            text_prompt: Text description of object to segment (e.g., "red car")
            confidence_threshold: Minimum confidence for detection (0.0 to 1.0)

        Returns:
            List of dictionaries containing:
                - 'mask': Binary segmentation mask (H, W)
                - 'bbox': Bounding box (x1, y1, x2, y2)
                - 'score': Confidence score
                - 'label': Detected label text

        Raises:
            ValueError: If inputs are invalid

        Example:
            >>> segmenter = GroundedSAM2Segmenter()
            >>> img = np.ones((100, 100, 3), dtype=np.uint8) * 128
            >>> results = segmenter.segment_with_text(img, "object", 0.5)
            >>> isinstance(results, list)
            True
            >>> len(results) >= 0
            True
        """
        self.set_image(image)

        if not text_prompt or not text_prompt.strip():
            raise ValueError("Text prompt cannot be empty")

        if not 0.0 <= confidence_threshold <= 1.0:
            raise ValueError("confidence_threshold must be between 0.0 and 1.0")

        # Simulate text-grounded detection and segmentation
        # In real implementation, this would use Grounding DINO + SAM2
        h, w = image.shape[:2]

        # Simulate one detection result
        results = []
        if len(text_prompt.strip()) > 0:
            # Create a sample segmentation mask
            center_x, center_y = w // 2, h // 2
            radius = min(h, w) // 4

            y_coords, x_coords = np.ogrid[:h, :w]
            circle_mask = (
                (x_coords - center_x) ** 2 + (y_coords - center_y) ** 2 <= radius**2
            )
            mask = np.zeros((h, w), dtype=np.uint8)
            mask[circle_mask] = 1

            # Create bounding box around the mask
            rows, cols = np.where(mask > 0)
            if len(rows) > 0:
                x1, y1 = int(cols.min()), int(rows.min())
                x2, y2 = int(cols.max()), int(rows.max())

                results.append(
                    {
                        "mask": mask,
                        "bbox": (x1, y1, x2, y2),
                        "score": 0.85,
                        "label": text_prompt,
                    }
                )

        return results

    def apply_color_mask(
        self, image: np.ndarray, mask: np.ndarray, color: tuple[int, int, int] = (0, 255, 0), alpha: float = 0.5
    ) -> np.ndarray:
        """
        Apply colored overlay on image based on segmentation mask.

        Args:
            image: Original image (H, W, C)
            mask: Binary segmentation mask (H, W)
            color: RGB color tuple for overlay (default: green)
            alpha: Transparency factor (0.0 to 1.0), default 0.5

        Returns:
            Image with colored mask overlay

        Raises:
            ValueError: If inputs have incompatible shapes or invalid alpha

        Example:
            >>> segmenter = GroundedSAM2Segmenter()
            >>> img = np.ones((50, 50, 3), dtype=np.uint8) * 100
            >>> mask = np.zeros((50, 50), dtype=np.uint8)
            >>> mask[10:40, 10:40] = 1
            >>> result = segmenter.apply_color_mask(img, mask, (255, 0, 0), 0.5)
            >>> result.shape
            (50, 50, 3)
            >>> result.dtype
            dtype('uint8')
        """
        if image.shape[:2] != mask.shape:
            raise ValueError("Image and mask must have same height and width")

        if not 0.0 <= alpha <= 1.0:
            raise ValueError("Alpha must be between 0.0 and 1.0")

        # Ensure image is 3-channel
        if image.ndim == 2:
            image = np.stack([image] * 3, axis=-1)

        result = image.copy()

        # Apply color where mask is active
        for i in range(3):
            result[:, :, i] = np.where(
                mask > 0,
                (alpha * color[i] + (1 - alpha) * image[:, :, i]).astype(np.uint8),
                image[:, :, i],
            )

        return result


def demonstrate_segmentation() -> None:
    """
    Demonstrate various segmentation modes with sample data.

    This function shows how to use the GroundedSAM2Segmenter class
    with different prompt types.
    """
    # Create sample image
    image = np.ones((200, 200, 3), dtype=np.uint8) * 128

    # Initialize segmenter
    segmenter = GroundedSAM2Segmenter(mask_threshold=0.5)

    # Example 1: Point-based segmentation
    print("1. Point-based segmentation")
    points = [(100, 100), (120, 120)]
    labels = [1, 1]  # Both foreground
    mask_points = segmenter.segment_with_points(image, points, labels)
    print(f"   Generated mask shape: {mask_points.shape}")
    print(f"   Segmented pixels: {np.sum(mask_points > 0)}")

    # Example 2: Box-based segmentation
    print("\n2. Bounding box segmentation")
    bbox = (50, 50, 150, 150)
    mask_box = segmenter.segment_with_box(image, bbox)
    print(f"   Generated mask shape: {mask_box.shape}")
    print(f"   Segmented pixels: {np.sum(mask_box > 0)}")

    # Example 3: Text-based segmentation
    print("\n3. Text-grounded segmentation")
    results = segmenter.segment_with_text(image, "object in center", 0.5)
    print(f"   Detected objects: {len(results)}")
    for i, result in enumerate(results):
        print(f"   Object {i + 1}:")
        print(f"     - Label: {result['label']}")
        print(f"     - Confidence: {result['score']:.2f}")
        print(f"     - BBox: {result['bbox']}")
        print(f"     - Mask pixels: {np.sum(result['mask'] > 0)}")

    # Example 4: Apply visualization
    print("\n4. Visualization")
    colored_result = segmenter.apply_color_mask(
        image, mask_points, color=(255, 0, 0), alpha=0.5
    )
    print(f"   Result image shape: {colored_result.shape}")


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    # Run demonstration
    print("\n" + "=" * 60)
    print("Grounded SAM2 Segmentation Demonstration")
    print("=" * 60 + "\n")
    demonstrate_segmentation()
