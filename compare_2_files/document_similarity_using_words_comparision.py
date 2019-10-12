class compare:
	def __init__(self,file1,file2):
		self.file1=file1
		self.file2=file2
	def common_word_list(self):	
		'''
	These are some common words we use in english therefore while comparing two files these words will not be count
	'''
		words_list = [
		 	"the",  "at",   "there"  ,"some",  "my",             
		 	"of",   "be",   "use"    ,"her",   "than",   
		 	"and",  "this"  "an"     ,"would", "first",  
		 	"a",    "have", "each"   ,"make",  "water",  
		 	"to",   "from", "which", "like",   "been"   ,         
		 	"in",   "or",   "she",   "him"     "call",   
		 	"is",   "one",  "do",    "into",   "who",            
		 	"you",  "had"   "how",   "time",   "oil",            
		 	"that", "by",   "their", "has"     ,"its",    
		 	"it",   "word", "if",    "look",   "now",            
		 	"he",   "but",  "will",  "two"     ,"find",   
		 	"was",  "not",  "up",    "more"    , "long",   
		 	"for",  "what", "other", "write",  "down",           
		 	"on",   "all",  "about", "go",     "day",            
		 	"are",  "were", "out",   "see",    "did",            
		 	"as",   "we",   "many",  "number", "get",            
		 	"with", "when", "then"   ,"no",    "come",   
			"his",  "your", "them"   ,"way",   "made",   
		 	"they", "can",  "these", "could",  "may",            
		 	"I",    "said", "so",    "people", "part" ]
		return words_list

	def words(self,add_file1):
		'''
		This function return the words present in file1 and file 2 with word counter in a list form		
		'''
		file1 =open(add_file1 , "r")
		words_from_file = file1.read().split()
		file1.close()
		
		return words_from_file
	def common_word_list_ret(self,Comp_list):
		'''
		This function removes all the common words from list and returns a new list	
		'''
		common_word_list = self.common_word_list()
		new_list = []
		for word in Comp_list:
			if word.lower() not in common_word_list:
				new_list.append(word)
		return new_list
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

	def similarity_percentile(self):
		'''
		This function is working like a main function for percentile 	
		'''
		list1 = self.words(self.file1)
		list2 =self.words(self.file2)
		new_list_1= self.common_word_list_ret(list1)
		new_list_2= self.common_word_list_ret(list2)
		final_list= self.diff_list(new_list_1 , new_list_2)
		return self.percentile(new_list_1,new_list_2,final_list)