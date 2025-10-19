"""
Test script for color augmentation module with dynamic image input
"""

import cv2
import numpy as np
import os
import sys
import glob
from color_augmentation import ColorAugmentation


def get_image_interactively():
    """
    Get image through multiple methods interactively.
    
    Returns:
        numpy.ndarray: Loaded image or None
    """
    print("\n" + "="*60)
    print("SELECT IMAGE INPUT METHOD")
    print("="*60)
    print("1. Browse and select image file")
    print("2. Enter image path manually")
    print("3. Use webcam capture")
    print("4. Select from current directory")
    print("5. Drag and drop (paste path)")
    
    choice = input("\nEnter your choice (1-5): ").strip()
    
    if choice == '1':
        return browse_for_image()
    elif choice == '2':
        return load_from_manual_path()
    elif choice == '3':
        return capture_from_webcam()
    elif choice == '4':
        return select_from_directory()
    elif choice == '5':
        return load_from_drag_drop()
    else:
        print("Invalid choice!")
        return None


def browse_for_image():
    """Use tkinter file dialog to browse for image."""
    try:
        import tkinter as tk
        from tkinter import filedialog
        
        root = tk.Tk()
        root.withdraw()  # Hide main window
        
        file_path = filedialog.askopenfilename(
            title="Select an image",
            filetypes=[
                ("Image files", "*.jpg *.jpeg *.png *.bmp *.tiff *.webp"),
                ("All files", "*.*")
            ]
        )
        
        if file_path:
            print(f"Selected: {file_path}")
            img = cv2.imread(file_path)
            if img is not None:
                return img
            else:
                print("Error: Could not load the selected image")
        else:
            print("No file selected")
            
    except ImportError:
        print("Error: tkinter not available. Try another method.")
    
    return None


def load_from_manual_path():
    """Load image from manually entered path."""
    path = input("\nEnter image path: ").strip()
    
    # Remove quotes if user copied path with quotes
    path = path.strip('"').strip("'")
    
    if os.path.exists(path):
        img = cv2.imread(path)
        if img is not None:
            print(f"✓ Successfully loaded: {path}")
            return img
        else:
            print(f"✗ Error: Could not load image from {path}")
    else:
        print(f"✗ Error: File not found at {path}")
    
    return None


def capture_from_webcam():
    """Capture image from webcam."""
    print("\nOpening webcam...")
    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        print("Error: Could not open webcam")
        return None
    
    print("Webcam opened! Press SPACE to capture, ESC to cancel")
    
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Could not read frame")
            break
        
        cv2.putText(frame, "Press SPACE to capture, ESC to cancel", 
                   (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
        cv2.imshow('Webcam - Capture Image', frame)
        
        key = cv2.waitKey(1) & 0xFF
        if key == 32:  # SPACE
            print("✓ Image captured!")
            cap.release()
            cv2.destroyAllWindows()
            return frame
        elif key == 27:  # ESC
            print("Cancelled")
            break
    
    cap.release()
    cv2.destroyAllWindows()
    return None


def select_from_directory():
    """List and select images from current directory."""
    print("\nSearching for images in current directory...")
    
    # Find all image files
    image_extensions = ['*.jpg', '*.jpeg', '*.png', '*.bmp', '*.tiff', '*.webp']
    image_files = []
    
    for ext in image_extensions:
        image_files.extend(glob.glob(ext))
        image_files.extend(glob.glob(ext.upper()))
    
    if not image_files:
        print("No images found in current directory")
        return None
    
    print(f"\nFound {len(image_files)} image(s):")
    for i, file in enumerate(image_files, 1):
        file_size = os.path.getsize(file) / 1024  # KB
        print(f"  {i}. {file} ({file_size:.1f} KB)")
    
    try:
        choice = int(input(f"\nSelect image (1-{len(image_files)}): "))
        if 1 <= choice <= len(image_files):
            selected_file = image_files[choice - 1]
            img = cv2.imread(selected_file)
            if img is not None:
                print(f"✓ Loaded: {selected_file}")
                return img
            else:
                print(f"✗ Error loading: {selected_file}")
        else:
            print("Invalid selection")
    except ValueError:
        print("Invalid input")
    
    return None


def load_from_drag_drop():
    """Load image from drag-and-dropped path."""
    print("\nDrag and drop your image file here and press Enter:")
    print("(or paste the full path)")
    path = input().strip()
    
    # Remove quotes and extra whitespace
    path = path.strip('"').strip("'").strip()
    
    # Handle file:// protocol
    if path.startswith('file://'):
        path = path[7:]
    
    if os.path.exists(path):
        img = cv2.imread(path)
        if img is not None:
            print(f"✓ Successfully loaded: {path}")
            return img
        else:
            print(f"✗ Error: Could not load image from {path}")
    else:
        print(f"✗ Error: File not found at {path}")
    
    return None


def create_augmentation_grid(augmentations, cols=3, cell_size=(200, 200)):
    """
    Create a grid of all augmented images with labels.
    
    Args:
        augmentations: Dictionary of {name: image}
        cols: Number of columns in grid
        cell_size: Size of each cell (width, height)
        
    Returns:
        Composite grid image
    """
    images = list(augmentations.items())
    rows = (len(images) + cols - 1) // cols
    
    cell_width, cell_height = cell_size
    text_height = 40
    total_cell_height = cell_height + text_height
    
    # Create blank canvas
    grid_width = cols * cell_width
    grid_height = rows * total_cell_height
    grid = np.ones((grid_height, grid_width, 3), dtype=np.uint8) * 255
    
    for idx, (name, img) in enumerate(images):
        row = idx // cols
        col = idx % cols
        
        # Resize image to fit cell
        resized = cv2.resize(img, (cell_width, cell_height))
        
        # Calculate position
        y_start = row * total_cell_height
        x_start = col * cell_width
        
        # Place image
        grid[y_start:y_start + cell_height, x_start:x_start + cell_width] = resized
        
        # Add text label below image
        text_y = y_start + cell_height + 30
        text_x = x_start + 10
        
        # Format name (replace underscores with spaces, title case)
        label = name.replace('_', ' ').title()
        
        cv2.putText(grid, label, (text_x, text_y),
                   cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1, cv2.LINE_AA)
    
    return grid


def test_color_augmentation(img, output_dir='augmented_outputs'):
    """
    Test all color augmentation functions on an image.
    
    Args:
        img: Input image (numpy array)
        output_dir: Directory to save augmented images
    """
    if img is None:
        print("Error: No image provided")
        return
    
    # Create output directory
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    print(f"\n✓ Image loaded successfully!")
    print(f"  Shape: {img.shape}")
    print(f"  Size: {img.shape[1]}x{img.shape[0]} pixels")
    
    augmenter = ColorAugmentation()
    
    # Dictionary of augmentations - 5 DISTINCT augmentations
    augmentations = {
        'Original': img,
        'High Brightness': augmenter.brightness_adjustment(img, factor=1.8),
        'High Contrast': augmenter.contrast_adjustment(img, factor=2.0),
        'Grayscale': augmenter.grayscale_conversion(img),
        'Warm Temperature': augmenter.temperature_tint(img, temperature=0.8, tint=0),
        'Histogram Equalization': augmenter.histogram_equalization(img, clip_limit=3.0),
    }
    
    # Save augmented images
    print(f"\n📁 Saving augmented images to '{output_dir}'...")
    for name, aug_img in augmentations.items():
        output_path = os.path.join(output_dir, f'{name}.jpg')
        cv2.imwrite(output_path, aug_img)
        print(f"  ✓ {name}.jpg")
    
    print(f"\n✅ Created {len(augmentations)} augmented images!")
    print(f"📂 Check the '{output_dir}' folder")
    
    # Create composite image with all augmentations
    create_composite = input("\nCreate composite image grid? (y/n): ").strip().lower()
    if create_composite == 'y':
        composite = create_augmentation_grid(augmentations)
        
        # Save composite
        composite_path = os.path.join(output_dir, 'all_augmentations_grid.jpg')
        cv2.imwrite(composite_path, composite)
        print(f"\n✓ Composite grid saved: {composite_path}")
        
        # Display composite
        cv2.imshow('All Color Augmentations - Press any key to close', composite)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


def main():
    """Main function."""
    print("="*60)
    print("COLOR AUGMENTATION TEST TOOL")
    print("="*60)
    
    while True:
        img = get_image_interactively()
        
        if img is not None:
            test_color_augmentation(img)
            
            # Ask if user wants to test another image
            again = input("\nTest another image? (y/n): ").strip().lower()
            if again != 'y':
                break
        else:
            retry = input("\nFailed to load image. Try again? (y/n): ").strip().lower()
            if retry != 'y':
                break
    
    print("\n" + "="*60)
    print("Thank you for using Color Augmentation Test Tool!")
    print("="*60)


if __name__ == "__main__":
    main()