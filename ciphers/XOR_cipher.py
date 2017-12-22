"""
	author: Christian Bender
	date: 21.12.2017
	class: XORCipher

	This class implements the XOR-cipher algorithm and provides
	some useful methods for encrypting and decrypting strings and
	files.

	Overview about methods

	- encrypt : list of char
	- decrypt : list of char
	- encrypt_string : str
	- decrypt_string : str
	- encrypt_file : boolean
	- decrypt_file : boolean
"""
class XORCipher(object):

	def __init__(self, key = 0):
		"""
			simple constructor that receives a key or uses
			default key = 0
		"""

		#private field
		self.__key = key

	def encrypt(self, content, key):
		"""
			input: 'content' of type string and 'key' of type int
			output: encrypted string 'content' as a list of chars
			if key not passed the method uses the key by the constructor.
			otherwise key = 1
		"""

		# precondition
		assert (isinstance(key,int) and isinstance(content,str))

		# testing for default arguments
		if (key == 0):
			if (self.__key == 0):
				key = 1
			else:
				key = self.__key

		# make sure key can be any size
		while (key > 255):
			key -= 255

		# This will be returned
		ans = []
		resultNumber = 0

		for ch in content:
			ans.append(chr(ord(ch) ^ key))

		return ans

	def decrypt(self,content,key):
		"""
			input: 'content' of type list and 'key' of type int
			output: decrypted string 'content' as a list of chars
			if key not passed the method uses the key by the constructor.
			otherwise key = 1
		"""

		# precondition
		assert (isinstance(key,int) and isinstance(content,list))

		# testing for default arguments
		if (key == 0):
			if (self.__key == 0):
				key = 1
			else:
				key = self.__key

		# make sure key can be any size
		while (key > 255):
			key -= 255

		# This will be returned
		ans = []
		resultNumber = 0

		for ch in content:
			ans.append(chr(ord(ch) ^ key))

		return ans


	def encrypt_string(self,content, key = 0):
		"""
			input: 'content' of type string and 'key' of type int
			output: encrypted string 'content'
			if key not passed the method uses the key by the constructor.
			otherwise key = 1
		"""

		# precondition
		assert (isinstance(key,int) and isinstance(content,str))

		# testing for default arguments
		if (key == 0):
			if (self.__key == 0):
				key = 1
			else:
				key = self.__key

		# make sure key can be any size
		while (key > 255):
			key -= 255

		# This will be returned
		ans = ""
		resultNumber = 0

		for ch in content:
			ans += chr(ord(ch) ^ key)

		return ans

	def decrypt_string(self,content,key = 0):
		"""
			input: 'content' of type string and 'key' of type int
			output: decrypted string 'content'
			if key not passed the method uses the key by the constructor.
			otherwise key = 1
		"""

		# precondition
		assert (isinstance(key,int) and isinstance(content,str))

		# testing for default arguments
		if (key == 0):
			if (self.__key == 0):
				key = 1
			else:
				key = self.__key

		# make sure key can be any size
		while (key > 255):
			key -= 255

		# This will be returned
		ans = ""
		resultNumber = 0

		for ch in content:
			ans += chr(ord(ch) ^ key)

		return ans


	def encrypt_file(self, file, key = 0):
		"""
			input: filename (str) and a key (int)
			output: returns true if encrypt process was
			successful otherwise false
			if key not passed the method uses the key by the constructor.
			otherwise key = 1
		"""

		#precondition
		assert (isinstance(file,str) and isinstance(key,int))

		try:
			fin = open(file,"r")
			fout = open("encrypt.out","w+")

			# actual encrypt-process
			for line in fin:
				fout.write(self.encrypt_string(line,key))

			fin.close()
			fout.close()

		except:
			return False

		return True


	def decrypt_file(self,file, key):
		"""
			input: filename (str) and a key (int)
			output: returns true if decrypt process was
			successful otherwise false
			if key not passed the method uses the key by the constructor.
			otherwise key = 1
		"""

		#precondition
		assert (isinstance(file,str) and isinstance(key,int))

		try:
			fin = open(file,"r")
			fout = open("decrypt.out","w+")

			# actual encrypt-process
			for line in fin:
				fout.write(self.decrypt_string(line,key))

			fin.close()
			fout.close()

		except:
			return False

		return True




# Tests
# crypt = XORCipher()
# key = 67

# # test enrcypt
# print crypt.encrypt("hallo welt",key)
# # test decrypt
# print crypt.decrypt(crypt.encrypt("hallo welt",key), key)

# # test encrypt_string
# print crypt.encrypt_string("hallo welt",key)

# # test decrypt_string
# print crypt.decrypt_string(crypt.encrypt_string("hallo welt",key),key)

# if (crypt.encrypt_file("test.txt",key)):
# 	print "encrypt successful"
# else:
# 	print "encrypt unsuccessful"

# if (crypt.decrypt_file("a.out",key)):
# 	print "decrypt successful"
# else:
# 	print "decrypt unsuccessful"