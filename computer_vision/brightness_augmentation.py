import glob
import os
import random
from string import ascii_lowercase, digits

import cv2
import numpy as np

# Params
IMAGE_DIR = ""
OUTPUT_DIR = ""
BRIGHTNESS_PERCENT = 50  # (between 0 and 100)


def main() -> None:
    """
    Get images list from input dir.
    Update new images.
    Save images in output dir.
    """
    img_paths = get_dataset(IMAGE_DIR)
    print("Processing...")
    new_images, paths = update_images(img_paths, BRIGHTNESS_PERCENT)

    for index, image in enumerate(new_images):
        # Get random string code: '7b7ad245cdff75241935e4dd860f3bad'
        letter_code = random_chars(32)
        file_name = paths[index].split(os.sep)[-1].rsplit(".", 1)[0]
        file_root = f"{OUTPUT_DIR}/{file_name}_NEW_{letter_code}"
        cv2.imwrite(f"{file_root}.jpg", image, [cv2.IMWRITE_JPEG_QUALITY, 100])
        print(f"Success {index+1}/{len(new_images)} with {file_name}")


def get_dataset(img_dir: str) -> list:
    """
    - img_dir <type: str>: Path to folder contain images
    Return <type: list>: List of images path
    """
    img_paths = []
    for img_file_path in glob.glob(os.path.join(img_dir, "*")):
        img_paths.append(img_file_path)
    return img_paths


def update_images(img_list: list, brightness_percent: float) -> tuple[list, list]:
    """
    - img_list <type: list>: list of all images
    - brightness_percent <type: float>: maximum brightness change
    Return:
            - new_imgs_list <type: narray>: images after change
            - path_list <type: list>: list the name of image files
    """
    path_list = []
    new_imgs_list = []
    for idx in range(len(img_list)):
        path = img_list[idx]
        path_list.append(path)
        img = cv2.imread(path)
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        value = int(random.random() * brightness_percent / 100 * 255)
        if random.random() < 0.5:
            hsv[:, :, 2] = np.where(
                (255 - hsv[:, :, 2]) < value, 255, hsv[:, :, 2] + value
            )
        else:
            hsv[:, :, 2] = np.where(hsv[:, :, 2] < value, 0, hsv[:, :, 2] - value)
        hsv[hsv > 255] = 255
        hsv[hsv < 0] = 0
        img = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
        new_imgs_list.append(img)
    return new_imgs_list, path_list


def random_chars(number_char: int = 32) -> str:
    """
    Automatic generate random 32 characters.
    Get random string code: '7b7ad245cdff75241935e4dd860f3bad'
    >>> len(random_chars(32))
    32
    """
    assert number_char > 1, "The number of character should greater than 1"
    letter_code = ascii_lowercase + digits
    return "".join(random.choice(letter_code) for _ in range(number_char))


if __name__ == "__main__":
    main()
