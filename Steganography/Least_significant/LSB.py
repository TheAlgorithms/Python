import cv2 as cv

def conv_to_bin(number):
	"""Returns a list, binary equivalent of a number."""
	bytes = bin(number)
	list = []
	for i in range(2,len(bytes)):
		list.append(bytes[i])
	i = len(list)
	while i!=8:
		list.insert(0,'0')
		i = i+1
	return list

def last(x):
	"""Return an integer value, the least significant bit of the argument."""
	x = bin(x)
	return x[len(x)-1]

def get_user_message():
	"""Returns a string, the user input."""
	file_obj = open("user_input.txt","r")
	user_message = file_obj.readline()
	return user_message
	

def encode():
	"""Main Encoding Process."""

	''' Reading the Imgae file and calculating height and width of the image'''
	raw_image = cv.imread('input_image.png',1)
	height,width = raw_image.shape[:2]

	'''calls get_user_message function to take input of the user message and converts it to a byte array'''
	user_message = get_user_message()
	covertmsg = user_message.encode()
	
	'''Initializing the starting encoding conditions by setting coordinate to 0,0 and Color pointer to Red'''
	row=0
	column=0
	color=0
	
	iterations = 0

	for byteMessage in covertmsg:
		
		Binary_equival = conv_to_bin(byteMessage)
		
		for number in Binary_equival:
			if number == '1':
				if last(raw_image[row][column][color]) == '0':
					raw_image[row][column][color] = raw_image[row][column][color] + 1
			else:
				if last(raw_image[row][column][color]) == '1':
					raw_image[row][column][color] = raw_image[row][column][color] - 1

			column = (column+1)%width

			if column == 0:
				row = row+1
				if row == height:
					row = 0
					column = 0
					color = color+1

	'''Writing the steganographed image'''
	cv.imwrite('steganographed_image.png',raw_image)

def main():
	encode()
	
if __name__ == '__main__':
	main()