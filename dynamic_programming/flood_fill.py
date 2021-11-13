from array import *

def get_pixel(image, x_co_ordinate, y_co_ordinate):
	return image[x_co_ordinate][y_co_ordinate]

def put_pixel(image, x_co_ordinate, y_co_ordinate, color):
	image[x_co_ordinate][y_co_ordinate] = color

def print_image_array(image):
	for r in image:
		for c in r:
			print(c,end = "  ")
		print()

def flood_fill(image, x_co_ordinate, y_co_ordinate, new_color, old_color):
	if(x_co_ordinate >= 0 and y_co_ordinate >= 0 and get_pixel(image, x_co_ordinate, y_co_ordinate) == old_color):
		put_pixel(image, x_co_ordinate, y_co_ordinate, new_color)
		flood_fill(image, x_co_ordinate + 1, y_co_ordinate, new_color, old_color)
		flood_fill(image, x_co_ordinate - 1, y_co_ordinate, new_color, old_color)
		flood_fill(image, x_co_ordinate, y_co_ordinate + 1, new_color, old_color)
		flood_fill(image, x_co_ordinate, y_co_ordinate - 1, new_color, old_color)
		flood_fill(image, x_co_ordinate + 1, y_co_ordinate - 1, new_color, old_color)
		flood_fill(image, x_co_ordinate - 1, y_co_ordinate + 1, new_color, old_color)
		flood_fill(image, x_co_ordinate + 1, y_co_ordinate + 1, new_color, old_color)
		flood_fill(image, x_co_ordinate - 1, y_co_ordinate - 1, new_color, old_color)


if __name__ == "__main__":
	image = [[1,1,1,1], [1,9,9,2], [1,9,9,2], [2,2,2,2]]
	print("Before")
	print_image_array(image)
	print("After")
	flood_fill(image,1,1,7,9)
	print_image_array(image)
