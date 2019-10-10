from wordCount import wordCount
from wordlist import wordList
from commonWords import common_words
class compare:
	def __init__(self,file1,file2):
		self.file1=file1
		self.file2=file2
	def word_count(self):

		'''
		just a regular function used to return the word count of words in file from wordCount.py		
		'''
		word_Counter = wordCount(self.file1,self.file2)
		return word_Counter.word_Count()
	def word_list(self):
		'''
		just a regular function used to return the words  in files from wordlist.py		
		'''
		word_list = wordList(self.file1,self.file2)
		return word_list.words()
	def common_words_function(self):
		'''
		just a regular function used to return common words from common words.py		
		'''
		my_common_words=common_words(True)
		return my_common_words.common_word_list()
	def common_word_list(self,Comp_list):
		'''
		This function removes all the common words from list and returns a new list	
		'''
		common_word_list = self.common_words_function()
		new_list = []
		for word in Comp_list:
			if word.lower() not in common_word_list:
				new_list.append(word)
		return new_list
	def percentile(self,new_list1,new_list2,final_list):
		'''
		This function returns the percentage of similarity in two files	
		'''
		len_of_list1 = len(new_list1)
		len_of_list2 = len(new_list2)
		len_of_final_list = len(final_list)
		percentage_of_list1 = (len_of_final_list/len_of_list1)*100
		percentage_of_list2 = (len_of_final_list/len_of_list2)*100
		temp1 = percentage_of_list1+percentage_of_list2
		temp2 = temp1/2
		temp2 = 100-temp2
		return temp2
		
	def diff_list(self,list1 , list2):
		'''
		This function removes all the similar words from both list and returns a new list	
		'''
		final_list= []
		final_list1= []
		final_list2 = []
		temp_list = []
		if len(list1)>len(list2):
			final_list2=list1
			final_list1=list2
		else:
			final_list2=list2
			final_list1 = list1
		for words in final_list2:
			temp_list.append(words.lower())
		for word in final_list1:
			if word.lower() not in temp_list:
				final_list.append(word)
		return final_list
	
	def diff_list_no_common_words(self):
		'''
		This function removes all the similar words from both list and returns a new list	
		'''
		final_list= []
		final_list1= []
		final_list2 = []
		temp_list = []
		list1=self.word_list()[1]
		list2=self.word_list()[3]
		if len(list1)>len(list2):
			final_list2=list1
			final_list1=list2
		else:
			final_list2=list2
			final_list1 = list1
		for words in final_list2:
			temp_list.append(words.lower())
		for word in final_list1:
			if word.lower() not in temp_list:
				final_list.append(word)
		return final_list
		
	def similarity_percentile(self):
		'''
		This function is working like a main function for percentile 	
		'''
		list1 = self.word_list()[1]
		list2 =self.word_list()[3]
		new_list_1= self.common_word_list(list1)
		new_list_2= self.common_word_list(list2)
		final_list= self.diff_list(new_list_1 , new_list_2)
		return self.percentile(new_list_1,new_list_2,final_list)
		
