import random

"""
pad with prefix of a chosen character or cut the string to a chosen positive length.
examples:
pad string 'a' with character '_' for length 3 >> '__a'
pad string '15' with character '0' for length 4 >> '0015'
pad string 'hello' with character '*' for length 2 >> 'he'
pad string 'aaaa' with character '*' for length -4 >> not defined.
"""
def pad(txt, char_to_pad, final_length):

	remaining_chars_to_pad = final_length - len(txt)
	return ((char_to_pad * remaining_chars_to_pad) + txt)[0:final_length]
	