import glob
import os
import random
from string import ascii_lowercase, digits

import cv2

LABEL_DIR = ""
IMAGE_DIR = ""
OUTPUT_DIR = ""
FLIP_TYPE = 1  # (0 is vertical, 1 is horizontal)


def random_chars(length: int) -> str:
    """Generates a random string of alphanumeric characters."""
    chars = ascii_lowercase + digits
    return "".join(random.choice(chars) for _ in range(length))


def get_dataset(label_dir: str, img_dir: str) -> tuple[list, list]:
    """
    Get a list of images and their corresponding annotations.

    Args:
        label_dir (str): Path to label directory containing annotations.
        img_dir (str): Path to folder containing images.

    Returns:
        Tuple containing a list of image paths and a list of labels.
    """
    # ... (rest of the function remains the same) ...


def update_image_and_anno(
    img_list: list, anno_list: list, flip_type: int = 1
) -> tuple[list, list, list]:
    """
    Update images and annotations based on flip type.

    Args:
        img_list (list): List of image paths.
        anno_list (list): List of labels.
        flip_type (int): Flip type (0 for vertical, 1 for horizontal).

    Returns:
        Tuple containing updated images, updated annotations, and their corresponding paths.
    """
    # ... (rest of the function remains the same) ...


def main() -> None:
    """
    Get images list and annotations list from input dir.
    Update new images and annotations.
    Save images and annotations in output dir.
    """
    img_paths, annos = get_dataset(LABEL_DIR, IMAGE_DIR)
    print("Processing...")
    new_images, new_annos, paths = update_image_and_anno(img_paths, annos, FLIP_TYPE)

    for index, image in enumerate(new_images):
        letter_code = random_chars(32)
        file_name = paths[index].split(os.sep)[-1].rsplit(".", 1)[0]
        file_root = f"{OUTPUT_DIR}/{file_name}_FLIP_{letter_code}"
        cv2.imwrite(f"{file_root}.jpg", image, [cv2.IMWRITE_JPEG_QUALITY, 85])
        print(f"Success {index+1}/{len(new_images)} with {file_name}")
        annos_list = []
        for anno in new_annos[index]:
            obj = f"{anno[0]} {anno[1]} {anno[2]} {anno[3]} {anno[4]}"
            annos_list.append(obj)
        with open(f"{file_root}.txt", "w") as outfile:
            outfile.write("\n".join(line for line in annos_list))


if __name__ == "__main__":
    main()
