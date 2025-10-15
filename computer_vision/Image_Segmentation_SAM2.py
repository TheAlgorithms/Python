"""
Text-Driven Image Segmentation with Grounded SAM2

This module demonstrates image segmentation using Meta's Segment Anything Model 2
combined with text prompts for automatic object detection and segmentation.
"""

import os

import cv2
import matplotlib.pyplot as plt
import numpy as np
import torch
from PIL import Image

# Set up device configuration
os.environ["PYTORCH_ENABLE_MPS_FALLBACK"] = "1"


def setup_device():
    """Configure and return the available computation device"""
    if torch.cuda.is_available():
        device = torch.device("cuda")
        # Use bfloat16 for faster inference on supported GPUs
        torch.autocast("cuda", dtype=torch.bfloat16).__enter__()
        # Enable tf32 for Ampere GPUs
        if torch.cuda.get_device_properties(0).major >= 8:
            torch.backends.cuda.matmul.allow_tf32 = True
            torch.backends.cudnn.allow_tf32 = True
    elif torch.backends.mps.is_available():
        device = torch.device("mps")
        print("MPS device detected - preliminary support may have limitations")
    else:
        device = torch.device("cpu")

    print(f"Using device: {device}")
    return device


# Visualization functions
np.random.seed(3)


def show_mask(mask, ax, random_color=False, borders=True):
    """
    Display segmentation mask on matplotlib axis

    Args:
        mask: Binary mask array
        ax: Matplotlib axis
        random_color: Whether to use random colors
        borders: Whether to draw mask borders
    """
    if random_color:
        color = np.concatenate([np.random.random(3), np.array([0.6])], axis=0)
    else:
        color = np.array([30 / 255, 144 / 255, 255 / 255, 0.6])

    h, w = mask.shape[-2:]
    mask = mask.astype(np.uint8)
    mask_image = mask.reshape(h, w, 1) * color.reshape(1, 1, -1)

    if borders:
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        contours = [
            cv2.approxPolyDP(contour, epsilon=0.01, closed=True) for contour in contours
        ]
        mask_image = cv2.drawContours(
            mask_image, contours, -1, (1, 1, 1, 0.5), thickness=2
        )

    ax.imshow(mask_image)


def show_points(coords, labels, ax, marker_size=375):
    """
    Display point prompts on image

    Args:
        coords: Point coordinates [[x, y], ...]
        labels: Point labels (1=positive, 0=negative)
        ax: Matplotlib axis
        marker_size: Size of point markers
    """
    pos_points = coords[labels == 1]
    neg_points = coords[labels == 0]

    ax.scatter(
        pos_points[:, 0],
        pos_points[:, 1],
        color="green",
        marker="*",
        s=marker_size,
        edgecolor="white",
        linewidth=1.25,
    )
    ax.scatter(
        neg_points[:, 0],
        neg_points[:, 1],
        color="red",
        marker="*",
        s=marker_size,
        edgecolor="white",
        linewidth=1.25,
    )


def show_box(box, ax):
    """
    Display bounding box on image

    Args:
        box: Bounding box [x_min, y_min, x_max, y_max]
        ax: Matplotlib axis
    """
    x0, y0 = box[0], box[1]
    w, h = box[2] - box[0], box[3] - box[1]
    ax.add_patch(
        plt.Rectangle((x0, y0), w, h, edgecolor="green", facecolor=(0, 0, 0, 0), lw=2)
    )


def show_masks(
    image,
    masks,
    scores,
    point_coords=None,
    box_coords=None,
    input_labels=None,
    borders=True,
):
    """
    Display segmentation masks with optional prompts

    Args:
        image: Input image
        masks: Segmentation masks
        scores: Confidence scores for masks
        point_coords: Point coordinates
        box_coords: Bounding box coordinates
        input_labels: Point labels
        borders: Whether to draw mask borders
    """
    for i, (mask, score) in enumerate(zip(masks, scores)):
        plt.figure(figsize=(10, 10))
        plt.imshow(image)
        show_mask(mask, plt.gca(), borders=borders)

        if point_coords is not None:
            assert input_labels is not None
            show_points(point_coords, input_labels, plt.gca())

        if box_coords is not None:
            show_box(box_coords, plt.gca())

        if len(scores) > 1:
            plt.title(f"Mask {i + 1}, Score: {score:.3f}", fontsize=18)

        plt.axis("off")
        plt.show()


def load_and_setup_model(model_cfg, checkpoint_path, device):
    """
    Load SAM2 model and create predictor

    Args:
        model_cfg: Model configuration path
        checkpoint_path: Path to model checkpoint
        device: Computation device

    Returns:
        SAM2 predictor instance
    """
    from sam2.build_sam import build_sam2
    from sam2.sam2_image_predictor import SAM2ImagePredictor

    sam2_model = build_sam2(model_cfg, checkpoint_path, device=device)
    predictor = SAM2ImagePredictor(sam2_model)
    return predictor


def demonstrate_point_prompt(predictor, image):
    """Demonstrate segmentation using single point prompt"""
    print("=== Single Point Prompt ===")

    # Single point on the truck
    input_point = np.array([[500, 375]])
    input_label = np.array([1])

    # Display input points
    plt.figure(figsize=(10, 10))
    plt.imshow(image)
    show_points(input_point, input_label, plt.gca())
    plt.axis("on")
    plt.title("Input Point Prompt")
    plt.show()

    # Predict masks
    masks, scores, logits = predictor.predict(
        point_coords=input_point,
        point_labels=input_label,
        multimask_output=True,
    )

    # Sort by score
    sorted_ind = np.argsort(scores)[::-1]
    masks = masks[sorted_ind]
    scores = scores[sorted_ind]
    logits = logits[sorted_ind]

    show_masks(
        image,
        masks,
        scores,
        point_coords=input_point,
        input_labels=input_label,
        borders=True,
    )

    return masks, scores, logits


def demonstrate_multiple_points(
    predictor, image, previous_masks, previous_scores, previous_logits
):
    """Demonstrate segmentation using multiple point prompts"""
    print("=== Multiple Points Prompt ===")

    # Multiple points to specify the object better
    input_point = np.array([[500, 375], [1125, 625]])
    input_label = np.array([1, 1])

    # Use best mask from previous prediction
    mask_input = (
        previous_logits[np.argmax(previous_scores), :, :]
        if previous_logits is not None
        else None
    )

    masks, scores, _ = predictor.predict(
        point_coords=input_point,
        point_labels=input_label,
        mask_input=mask_input[None, :, :] if mask_input is not None else None,
        multimask_output=False,
    )

    show_masks(image, masks, scores, point_coords=input_point, input_labels=input_label)

    return masks, scores


def demonstrate_box_prompt(predictor, image):
    """Demonstrate segmentation using bounding box prompt"""
    print("=== Bounding Box Prompt ===")

    input_box = np.array([425, 600, 700, 875])  # x_min, y_min, x_max, y_max

    masks, scores, _ = predictor.predict(
        point_coords=None,
        point_labels=None,
        box=input_box[None, :],
        multimask_output=False,
    )

    show_masks(image, masks, scores, box_coords=input_box)

    return masks, scores


def demonstrate_combined_prompts(predictor, image):
    """Demonstrate combining box and point prompts"""
    print("=== Combined Box and Points ===")

    input_box = np.array([425, 600, 700, 875])
    input_point = np.array([[575, 750]])  # Negative point inside the box
    input_label = np.array([0])

    masks, scores, _ = predictor.predict(
        point_coords=input_point,
        point_labels=input_label,
        box=input_box,
        multimask_output=False,
    )

    show_masks(
        image,
        masks,
        scores,
        box_coords=input_box,
        point_coords=input_point,
        input_labels=input_label,
    )

    return masks, scores


def demonstrate_batched_prompts(predictor, image):
    """Demonstrate batched prompt processing"""
    print("=== Batched Prompts ===")

    # Multiple bounding boxes (simulating object detector output)
    input_boxes = np.array(
        [
            [75, 275, 1725, 850],  # Large area
            [425, 600, 700, 875],  # Wheel area
            [1375, 550, 1650, 800],  # Another wheel
            [1240, 675, 1400, 750],  # Small detail
        ]
    )

    masks, scores, _ = predictor.predict(
        point_coords=None,
        point_labels=None,
        box=input_boxes,
        multimask_output=False,
    )

    # Display all masks together
    plt.figure(figsize=(10, 10))
    plt.imshow(image)
    for i, mask in enumerate(masks):
        show_mask(mask.squeeze(0), plt.gca(), random_color=True)
    for box in input_boxes:
        show_box(box, plt.gca())
    plt.axis("off")
    plt.title("Batched Prompts - Multiple Objects")
    plt.show()

    return masks, scores


def demonstrate_batched_images(predictor):
    """Demonstrate processing multiple images with batched prompts"""
    print("=== Batched Images ===")

    # Load multiple images
    image1 = Image.open("images/truck.jpg")
    image1 = np.array(image1.convert("RGB"))
    image1_boxes = np.array(
        [
            [75, 275, 1725, 850],
            [425, 600, 700, 875],
            [1375, 550, 1650, 800],
        ]
    )

    image2 = Image.open("images/groceries.jpg")
    image2 = np.array(image2.convert("RGB"))
    image2_boxes = np.array(
        [
            [450, 170, 520, 350],
            [350, 190, 450, 350],
            [500, 170, 580, 350],
        ]
    )

    img_batch = [image1, image2]
    boxes_batch = [image1_boxes, image2_boxes]

    # Process batch
    predictor.set_image_batch(img_batch)
    masks_batch, scores_batch, _ = predictor.predict_batch(
        None, None, box_batch=boxes_batch, multimask_output=False
    )

    # Display results
    for i, (image, boxes, masks) in enumerate(zip(img_batch, boxes_batch, masks_batch)):
        plt.figure(figsize=(10, 10))
        plt.imshow(image)
        for mask in masks:
            show_mask(mask.squeeze(0), plt.gca(), random_color=True)
        for box in boxes:
            show_box(box, plt.gca())
        plt.axis("off")
        plt.title(f"Image {i + 1} - Batched Processing")
        plt.show()


def main():
    """Main function demonstrating SAM2 image segmentation capabilities"""

    # Setup device
    device = setup_device()

    # Load model
    sam2_checkpoint = "../checkpoints/sam2.1_hiera_large.pt"
    model_cfg = "configs/sam2.1/sam2.1_hiera_l.yaml"

    print("Loading SAM2 model...")
    predictor = load_and_setup_model(model_cfg, sam2_checkpoint, device)

    # Load and display sample image
    print("Loading sample image...")
    image = Image.open("images/truck.jpg")
    image = np.array(image.convert("RGB"))

    plt.figure(figsize=(10, 10))
    plt.imshow(image)
    plt.axis("on")
    plt.title("Original Image")
    plt.show()

    # Set image for predictor
    predictor.set_image(image)

    # Run demonstrations
    masks, scores, logits = demonstrate_point_prompt(predictor, image)
    demonstrate_multiple_points(predictor, image, masks, scores, logits)
    demonstrate_box_prompt(predictor, image)
    demonstrate_combined_prompts(predictor, image)
    demonstrate_batched_prompts(predictor, image)
    demonstrate_batched_images(predictor)

    print("All demonstrations completed successfully!")


if __name__ == "__main__":
    main()
