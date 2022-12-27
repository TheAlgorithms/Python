import glob
import os
import random
from string import ascii_lowercase, digits

import cv2
import numpy as np


# Params
IMAGE_DIR = "1"
OUTPUT_DIR = "out"
NOISE_TYPE = "salt-and-pepper" # ("salt-and-pepper" or "gaussian")
ALPHA = 0.1 # ("salt-and-pepper" amount or "gaussian" variance)


def main() -> None:
	"""
	Get images list from input dir.
	Update new images.
	Save images in output dir.
	"""
	img_paths = get_dataset(IMAGE_DIR)
	print("Processing...")
	new_images, paths = update_images(img_paths, NOISE_TYPE, ALPHA)

	for index, image in enumerate(new_images):
		# Get random string code: '7b7ad245cdff75241935e4dd860f3bad'
		letter_code = random_chars(32)
		file_name = paths[index].split(os.sep)[-1].rsplit(".", 1)[0]
		file_root = f"{OUTPUT_DIR}/{file_name}_NOISY_{letter_code}"
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


def update_images(
	img_list: list, noise_type: str, alpha: float
) -> tuple[list, list]:
	"""
	- img_list <type: list>: list of all images
	- noise_type <type: str>: noise type ("salt-and-pepper" or "gaussian")
	- alpha <type: float>: "salt-and-pepper" amount or "gaussian" variance
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
		row, col, ch = img.shape
		if noise_type == "gaussian":
			mean = 0
			var = alpha
			sigma = var ** 0.5
			gaussian_noise = np.random.normal(mean, sigma, (row, col, ch)) * 128
			gaussian_noise = gaussian_noise.reshape(row, col, ch)
			noisy_img = img + gaussian_noise
			noisy_img[noisy_img > 255] = 255
			noisy_img[noisy_img < 0] = 0
		elif noise_type == "salt-and-pepper":
			amount = alpha
			noisy_img = np.copy(img)
			for i in range(img.shape[0]):
				for j in range(img.shape[1]):
					r = random.random()
					if r < amount / 2:
						noisy_img[i][j] = 0
					elif r > 1 - amount / 2:
						noisy_img[i][j] = 255
		new_imgs_list.append(noisy_img)
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
	print("DONE ✅")
