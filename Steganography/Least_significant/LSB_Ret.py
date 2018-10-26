import cv2 as cv

height = 0
width = 0

def last(x):
	"""Return an integer value, the least significant bit of the argument."""
	x = bin(x)
	return x[len(x)-1]

def get_ascii(arr_list):
	"""Return a character, ascii equivalent of a number"""
	deci = 0
	for i in range(len(arr_list)):
		if arr_list[i] == '1':
			deci = deci + pow(2,len(arr_list)-i)

	return str(deci)
		
def getnext(list1,pos):
	"""Returns next character in message"""
	sum = 0
	k = 7
	for i in range(pos,pos+8):
		if list1[i]=='1':
			sum = sum+pow(2,k)
		k = k-1

	return chr(sum)

def get_message_size():
	"""Determines the size of message"""
	file_obj = open("user_input.txt","r")
	string = file_obj.readline()
	return len(string)

def write_To_File(message):
	"""Writes the decoded message to a file named Decoded.txt"""
	file_obj = open("decoded.txt","w")
	file_obj.write(message)


def decode():
	"""main decoding logic"""
	
	''' Reading the steganographed Imgae file and calculating height and width of the image'''
	steganoImage = cv.imread("steganographed_image.png",1)
	height,width = steganoImage.shape[:2]

	''' Initializes the message as null'''
	message = ""

	''' Initializes the starting conditions'''
	column=0
	row=0
	color=0

	''' Last bits is an array that holds last bits of pixel values.'''
	last_bits = []

	for row in range(height):
		for column in range(width):
			last_bits.append(last(steganoImage[row][column][color]))
			if (column+1)%width == 0:
				row = row+1
				if row == height:
					row = 0
					color = color+1
			column = (column+1)%width
	
	message_size = get_message_size()

	i=0
	while message_size:
		message+=getnext(last_bits,i)
		i = i+8
		message_size = message_size-1
		
	write_To_File(message)

def main():
	decode()
	
if __name__ == '__main__':
	main()
