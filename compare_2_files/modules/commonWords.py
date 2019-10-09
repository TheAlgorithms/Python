'''
These are some common words we use in english therefore while comparing two files these words will not be count
'''
class common_words:
	def __init__(self,abc):
		self.abc=abc
	def common_word_list(self):	
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
		if(self.abc==True):
			'''
			This function's functionality is rather you want to use this wordlist or not
			'''
			return words_list
		else:
			return null
	

