class wordCount:
	def __init__(self,add_file1,add_file2):

		'''
		This function return the word count of file1 and file 2 in a list form		
		'''
		self.add_file1=add_file1
		self.add_file2=add_file2
	def word_Count(self):
		add_file1=self.add_file1
		add_file2=self.add_file2
		file1 =open(add_file1 , "r")
		words_from_file1 = file1.read().split()
		words_in_file1 = len(words_from_file1)
		file1.close()
		file2 =open(add_file2 , "r")
		words_from_file2 = file2.read().split()
		words_in_file2 = len(words_from_file2)
		file2.close()
		word_counter= ["words count in file 1 " , words_in_file1, "words count in file 2" , words_in_file2]
		return word_counter
	
