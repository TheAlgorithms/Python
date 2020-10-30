'''
# How to split a string for int in python

To do this you must first use python is native `split()` function, it separates a string according to a delimiter.
#Syntax

`string.split(separator, max)`
`separator`	Optional. Specifies the separator to use when splitting the string. Default value is a whitespace. 
`max`	Optional. Specifies how many splits to do. Default value is -1, which is "all occurrences"
'''
# HOW 


string = "ONE TWO"
one = string.split(' ')[0] # ['ONE']
two = string.split(' ')[1] # ['TWO']
print(one,two)

'''
the `[i]` indicates which word will be selected, where i represents the position of the separated word
'''
# HOW TO DO TO RESULT IN INT

string = "02-04-1994"
string.split('-')  # ['02', 04', '1994']
 
day = string.split('-')[0]  # ['02']
month = string.split('-')[1] # ['04']
year = string.split('-')[2] # ['1994']
day = int(day)
month = int(month)
year = int(year)
print(day,month,year) # output is 2 4 1994
