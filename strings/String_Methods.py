'''
This is a helper file that shows all the string methods that can be used to exploit a string to get a desired string in a much easier way.
These methods are useful when building a complex algorithm that has string manipulation as one of the parts of the entire program
or when you are lazy enough to go the conventional way
> single line comments are the output of the print line
> multi line comments explain the working of the functions
'''
#example string
string = 'kaIVALya LoVes chocOLates {} LoVes'
print('\nString Functions\n')
#Capitalize
a = string.capitalize()
print(a) #Kaivalya loves chocolates {} Loves
b = string.casefold()
print(b) #kaivalya loves chocolates {} Loves
c = string.center(40,'X') '''center function requires two parameters,the width and fill character, letter must be one character long'''
print(c) #XXXkaIVALya LoVes chocOLates {} LoVesXXX
d = string.count('a') '''count function requires atleast one parameter'''
print(d) #3
string2 = '#@!%$&^*('
e = string2.encode()
print(e) # b'#@!%$&^*('
print(string.endswith('a',2,10),string.endswith(' '))
f = string.expandtabs(8)#def tab size is 8
print('Tab Size is 8',f)
g = string.find('h')
print('print',g,string.rfind('IVAL',2,32))
print(string.format(g))
#print(string.format_map(26)) map takes exactly one argument
h = string.index('e',2,26)#if the substring not present value error appears
print(h,string.rindex('c',10,30))
''' The below functions return boolean values '''
print(string.isalnum(),string.isalpha(),string.isascii())
print(string.isdecimal(),string.isdigit(),string.isidentifier())
print(string.islower(),string.isnumeric(),string.isprintable())
print(string.isspace(),string.istitle(),'UPPER',string.isupper())
''' .join() is used for concatenation '''
i = string.join('more')
print(i)#it joins one char at a time requires atleast one int
print(string.ljust(40,'L'))# argument length
print(string.lower())
print(string.rjust(40,'R'))
print(string.lstrip())
print(string.lstrip('k'))#*
j = string.partition(' LoVes ') #*print(string.maketrans(''))
print(j,string.rpartition(' LoV'))
k = string.replace('LoVes','HaTes',1)#*
print(k)
l = string.split()
print(l,string.rsplit('{}',2))
m = string.strip()
print('printtt',m,string.rstrip(),string.splitlines(), string.splitlines(True))
print(string.startswith(''))
print(string.swapcase())
n = string.title()
print(n, string.upper()) #string.translate()
o = string.zfill(45)
print(o)#if the value is less than len of string no filling is done
