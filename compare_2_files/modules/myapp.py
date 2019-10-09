'''
	 just paste the two files you want to compare in files folder and then pass the name of files below
	 Example==>    word_function = compare("myfile.txt", "officeDoc.txt")
	 both files must have same file extention
	1) first function returns a list of number of words present in both files.
	2) Second function returns all the words of both files stored in list. 	
	 	to see all the words of file1 one use word_function.word_list()[1]
	 	to see all the words of file2 one use word_function.word_list()[3]

	3) Third function returns a list of the common english words that will be remove while checking the similarity
	4) Fouth function returns list of unsimilar words in both list without removing common words
	5) Fifth function returns the percentage of similarity in both files

'''
from comparision import compare
def main():
	
	word_function = compare("file1.txt","file2.txt")


	# First Function
	print("Number of word in both files "+str(word_function.word_count()))

	# Second Function
	print("All words in file 1 "+str(word_function.word_list()[1]))

	# Third Function
	print("Common Words"+str(word_function.common_words_function()))
	
	# Fouth Function
	print("Similar words in Both files"+str(word_function.diff_list_no_common_words()))

	# Fifth Function
	print("percentage of similarity "+str(word_function.similarity_percentile()))
main()
