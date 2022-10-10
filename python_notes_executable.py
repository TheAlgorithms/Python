#Modules are predefined piece of codes which makes our work easy!

import os #importing modules
from os import close, replace #importing modules 

print("Hello World") 

# single line comment

'''
Multi line comment
'''

# print in multiple lines

print('''Next we will learn about variables,there are 5 types of variables
1-Integer
2-Strings
3-Booleans
4-Floating type number
5-none''')

#Escape sequence  (\n,\t,\'\\) #check the use yourself by looking at the output screen 
print("Next we will learn about variables,there are 5 types of variables\n\t1-Integer\n\t2-Strings\n\t3-Booleans\n\'4-Floating type number\'\n5-none")


# variables
a = "Icecrac34r"  # string
b = 69  # integer
c = 41.1  # Floating type number
d = True  # Boolean
e = False  # Boolean
f = None  # NoneType

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

# printing type of variable
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))

'''rules for naming a variable

Rules for defining a variable name: (Also applicable to other identifiers)

A variable name can contain alphabets, digits, and underscore.
A variable name can only start with an alphabet and underscore.
A variable can't start with a digit.
No white space is allowed to be used inside a variable name. '''

print("This is how you print variable with a sentence-",a,b,c,d,e,f) #It must start with a " , " else it will be treated as an unknown string 

b = "Operators"
print("Next, we'll learn about-",b)

# Operators
# Arithmetic Operators (+, -, *, /, etc.)
a = 6
b = 9
print("The value of 6+9 is", a + b)
print("The value of 6-9 is", a - b)
print("The value of 6*9 is", a * b)
print("The value of 6/9 is", a / b)
print("The remainder of 6/9 is", a % b)
print("The exponential product  of 6&9 is", a ** b) # value of 6 raise to the power of 9 

# Assignment Operators (=, +=, -=, etc.)
a = 69  # =
a += 1  # +=
print("This should add 1 in 69->", a)
a -= 1  # -=
print("This should substract 1 in 70->", a)
a /= 3  # /=
print("This should divide 69 by 3->", a)
a *= 3  # *=
print("This should multiply 23 by 3->", a)

# Comparison Operators (==, >=, <=, >, <, !=, etc.) IT COMPARES AND RETURN A BOOLEAN VALUE i.e TRUE OR FALSE
a = (69 == 69)
print("Is 69 = 69? ", a)
a = (70 > 69)
print("Is 70>69? ", a)
a = (70 < 69)
print("Is 70<69? ", a)
a = (70 > 70)
print("Is 70>70? ", a)
a = (70 > 69)
print("Is 70 > or = 70? ", a)
a = (70 != 69)  # ! stants for not equal to
print(" 70 is not equal to 69? ", a)

# Logical Operators (and, or, not)
bool1 = True
bool2 = False
print((bool1 and bool2)) #If both are True
print((bool1 or bool2)) #If either of them is True
print((not bool2)) #Reverse the boolean value
bool1 = True
bool2 = True
print((bool1 and bool2))
print((bool1 or bool2))
print((not bool2))
#Learn about boolean algebra for better understanding 

#Typecasting [Conversion from one data type to other]
a = "696969"
print (a)
#a += 2 -> this wont work since python interpretor is taking it as a string 
print(type(a)) #Its in string format
a = int(a) #Converted it to integer data type
a += 2 #Now it will add 2 in 696969 since py interpretor now treates it as an integer
print (a)
a = float(a) #Now this will add decimal places
print (a)
#Llly, a = str(a) to convert it back to string 

#Input function [Takes input from user]
a = input("Enter your name- ")
print (a ,"suck at python")

#Working with Strings
#concatenating two strings
name = str(input("Your name- ")) #typecasting in input function
greeting = "Fuck off,"
print (name , greeting)
#or
merge = greeting + name
print (merge)

#string index 
'''Index in a string starts from 0 to (length-1)
If i print Icecrac34r, I=0 c=1 e=2 ....r=10'''
a = "Icecrac34r"
print (a[0])
print (a[1])
print (a[4])

#string slicing 
print (a[0:3]) #here it will print from 0 to 2 i.e ice
print (a[0:10])
print (a[:10]) #Initialize from 0 ==> its same as (a[0:10])
print (a[0:]) #Ends on last possible index ==> its same as (a[0:10])

'''negetive index [usually used to print last character of the string since it is always market as -1]
Here in Icecrac34r r=-1 4=-2 3=-3 c =-4 .... '''
print (a[-1]) #Last part of the string is taken to be -1 ==> value of -1 is same as 9 
c = a[-10:-1] #same as a[0:9]
print (c)

#slicing with skip values
c = "Python"
d = (c[0::2]) #This is read as print from index 0 to end with skip value of 2 i.e skip every alternate value.
d = (c[0::3]) #This will skip 2 values it will go like (n-1), 3 means it will skip 2 values and print "ph"
print (d)

#STRING FUNCTION 
a = "let's take a big string for better understanding! "
#len
print (len(a)) #string function "len" = length, it will print length of the string
#endswith
print (a.endswith("wrong ending = false")) #since string ends with "understanding" anything else as endswith value will return false 
print (a.endswith("understanding! ")) # This will show true since string endswith word understanding 
#count
print (a.count("t")) #counts how many times letter "t" is present in the string 
print (a.count("better")) #works for words as well 
#capitalize 
print (a.capitalize()) #it will capitalize the first word of the string 
#find
print (a.find("for")) #Finds word "for" if it exist in the string you'll get index number else it will return -1 i.e negetive
#replace
print (a.replace("let's" , "let us")) #replace a word in a string with another 

#F strings
print (f"{c} + {a} = {c+a} this is fstring") # f at the beginnig  of the string {variables and operators/operations in curly bracket} 

'''note- 'find' works for only 1st occurance in the string whereas 'replace' will work for all the existing occurance in the string'''

#List- containers that store a certain value, works with any given data type. 

list1 = [69, 420.0 , 'hem' , 'ice'] #List must be enclosed with []
print (list1)
print (list1[2]) #prints value at index = 2 of list1 i.e hem
list1[3] = "icecrac34r" #change value of index 3 to icecrac34r
print (list1[3])
print (list1) #will print with updated content at index 3
print (list1[0:3]) #list slicing 
print (list1[-4:])
print (list1[0:4:2]) #list with skip value of 2 i.e skip n-1 word at a time

#List functions
l2 = [69, 420.0 ,4*3, 16/2 , 5-2 , 34]
print (l2)
l2.sort() #sort in asscending order
print (l2)
l2.reverse()
print (l2) #sort in descending order 
l2.append(999) #Add 999 at the end of the list i.e -1 index
print (l2)
l2.insert (3,4) #insert "4" at index "3"
print (l2)
l2.pop (4) #remove the value that is stored at index "4" for of l2
print (l2)
l2.remove (420.0) #remove 420.0 from the list (if the value exists twice, only first one will be removed)
print (l2)

#TUPLES (List whose values cannot be changed/updated)
tuple1 = ("hem" , "icecrac34r" , 69 ,420) #Tuples must be enclosed with ()
print (tuple1[2]) #Print element using index
print (tuple1[0:3]) #string slicing
print (tuple1[0:4:2]) #skip value

#Tuples functions
print (tuple1.count(69)) #Will return number of times 69 occurs in tuple1
print (tuple1.index("icecrac34r")) #Will return number of index of which "icecrac34r" is stored 

#Something important 
tuple_eg = (4) #This is a variable whose value is 4
print(type(tuple_eg))
tuple_eg = (4,) #This is a singular tuple
print(type(tuple_eg))

#Dictonary
mydictonary = {
    "key" : "stores a specific value",
    "key1" : "Keys can't be duplicated",
    "anotherdictonary": {"newkey": "new dictonary can be created in the pre-existing one"}
    }
print(mydictonary["key"]) #to print value of the given key
print(mydictonary["anotherdictonary"])
print(mydictonary["anotherdictonary"]["newkey"])
mydictonary["anotherdictonary"]["newkey"] = "value of the key can be changed like this"
print(mydictonary["anotherdictonary"]["newkey"])

#Dictonary functions
print(mydictonary.keys()) #Prints all the keys of dictonary 
print(mydictonary.values()) #Prints all the values of dictonary 
print(mydictonary.items()) #Prints all the kays and values of dictonary 
yet_another_dict = {
    "yet_another_Dictonary" : "we'll add this in the existing dictonary using .update function",
    "key3" : "yet another key"
    }
mydictonary.update(yet_another_dict) #Updates existing dictonary with new values and keys from different dictonary 
print(mydictonary["yet_another_Dictonary"])
print(mydictonary["key3"])
print(mydictonary.get("key1")) #to print value of the given key

#Something important
#Difference between print(mydictonary["key2"]) and print(mydictonary.get("key2"))

#print(mydictonary["key2"]) #Since key 2 dosen't exist this will throw error 
print(mydictonary.get("key2")) #Since key 2 dosen't exist this will return "None" as the value and program will still be executed without errors 

#Sets
s = {2 ,4,5,6,7,1,7,1,4,1,12,6} #Set must be enclosed with {}
print(s)

#Set functions 
print(len(s)) #Prints the length if set s 
s.remove(7) #Removes 7 from set
print(s)
s.add(7) #Adds 7 in set 
print(s)
print(s.pop()) #Remove and return an arbitrary set element.
print(s)
print(s.union({69,6})) #prints elements from both set s and set {69,6}
print(s.intersection({69,6})) #prints elements that are common in set {69,6} and s

#something important
s1 = {} #This is an empty dictonary
print(type(s1))
s1 = set() #this is an empty set 
print(type(s1))

'''Note- Dictonary and lists are mutable, i.e their values can be changed. whereas Sets and tuples are immutable'''

#Conditional statement 
#If-else statement 
year = 1961
age = int(2021)-year
print (age)
if(age>18):
    print ("you're eligible to vote,since you're" ,age, "years old")
else:
    print("you're not eligible to vote,since you're" ,age, "years old")

#if elif else statements
number = 5
if number == 1:
    print ("number is 1")
elif number ==2 :
    print ("number is 2")
elif number ==3:
    print ("number is 3")
elif number ==4:
    print ("number is 4")
else: 
    print ("number is 5")

#Logical operators
if age > 21 and age < 60: #If both the operands are true,else returns false
    print("you're eligible to work")
else:
    print("you're not eligible to work")

if age == 60 or year > 1960: #if one of the operands is true,it will return true
    print("you're on the brink of retirement")
else:
    print("you're not eligible to work")

#Relational operators 
a = 35
if a<= 35:
    print("A is less than or equal to 35")
elif a>= 40:
    print("A is greater than or equal to 40")
elif a == 45:
    print("A is equal to 45")

#In and Is
list2 = ["bottle","Socks","cleaner"]
product = "bottle"
if product in list2: #Used to sort items from list/tuple/dictonary 
    print ("Yes that item is part of the list!")
else: 
    print("item isn't present in the list")

num = 69
if num is 69: #same as ==
    print ("Number = 69")

'''Practice-1
Make a list of students, if name is part of the list ask to enter marks of all 5 subjects and match it with grading system followed by you and give grades to the student
Answer - go to pr_1_grading.py '''
    
#Loops in python (instructs program which set to repeat and how)
#While loop
a = 1 #Let a = 1
while a<10: # while the value of a is less than 10 print a, if the while condition is "False" loop won't be executed
    print (a)
    a = a+1 # a = a+1 means initial value is 1 and it will continue adding 1 "while" the condition for loop stands true. If the condition never becomes false the loop will keep on running 
# loop will be oven once the value of "a" will be 10 or more 

#Print list with the help of while loop
listt =  ["Python","c++","c","java","HTML :-)"] #List of all programming languages
i = 0 #initially we took index as 0
while i<len(listt): #while length of i is less than length of the list (i.e 5) run the loop
    print (listt[i]) #Print index "i"
    i = i+1 #So all the index are printed. i=i will make an infinite loop with python

#Easier way to print list
#FOR loop
for language in listt: #language is a variable assigned to the items in the list
    print (language) #for items in the list print the items

#for loop with else
for language in listt:
    print (language)
else:
    print ("all the language in the list has been printed") #If the loop isn't running print this statement 

#Functions in loop
#range - used  to generate sequence of numbers
for numbers in range (0, 10): #for numbers in range start from zero and print till 10
    print (numbers)
for numbers in range (0,20,2): #for number in range from 0 to 20 with skip value of 2 #range (start , stop ,skip value)
    print (numbers)

#break - used to break the loop at certain met condition
for digits in range (0,1000): #print from 0 to 1000
    print (digits)
    if digits == 6: 
        break #if 6 is present in the loop exit the loop after it

#continue - 
for i in range (5):
    if i == 3:
        continue # if the value of i = 3, continue the loop without printing the below condition
    print(i)

#pass
for i in range (10):
    if i == 5:
        pass #If you don't want to put any output to the loop just write pass , if you give if statement and don't assign a task it will throw error

#printing patterns using loop
'''
*
**
***
****
'''
for starts in range (5): 
    print ("*" * (starts+1))
#inverse of 1st exercise 
for n in range(1,5):
    print("*" * (5-n))

'''Practice -2
ASK USER TO INPUT ANY NUMBER AND PRINT ITS TABLE , SOLVE THIS BY BOTH WHILE AND FOR LOOP
Answer- pr_2_tables.py '''

'''Try to make a rock paper scissor game using "Random" module randomize selection by computer and take user input.....'''

#Functions
#<404 NOT FOUND> :D
#When an operation needs to be executed multiple times, we can define it as a function and call it when needed instead of writing whole operation multiple times
def hello(): #define a function named as hello
    print("Hello world!") #operation of the function
    return print
     
hello() #calling the function
hello() #calling the function again
hello() #calling the function yet again 
hello() #calling the function yet yet again 

#method 2 (more convincing to me)
def hello2():
    p = print ("hello world")
    return p

hello2() #calling the function
hello2() #calling the function again
hello2() #calling the function yet again 
hello2() #calling the function yet yet again 

#function with changable value (variable)
def greet(name):
    p = print ("hello world", str(name))
    return p

name = str("hem")
(greet(name))
name = str("Icecrac34r")
greet(name)

#arguments in functions
def mysum(n1,n2): #Add 2 argument
    p = n1 + n2
    return p 

print (mysum(4,6))

#default parameters 
def greet3(name = "stranger" ): #Same function as above but if no name is provied it will return "Stranger" as we've set it as a default perameter
    p = print ("hello world", str(name))
    return p
greet3() #this must print "Stranger" since no value is provied for name
greet3("HEM")
#Example 2 #positional parameter - position of digits matter 
def mydiff(n1=" Define a value",n2=" Define a value"): 
    p = n1 - n2 #n1-n2 wont be same as n2-n1
    return p 

print(mydiff(8 , 6))

#positional parameters - positional arguments are arguments that need to be included in the proper position or order.

#Recursions - re-occuring functions . they follow a certain pattern , and hence calls itself 
def factorial(n):
    if(n ==0 or n==1):
        return 1
    return n * factorial(n - 1) #  A certain pattern is followed and function will call itself 5 times till n-1 = 1 

a = factorial(5)
print(a)

'''Practice 3-
since we've learnt about functions, try to improvise the grading program from practice 1. define percentage as a specific function and call it when needed'''

#file i/o - handling files in python 
#Text files - ones that can be opened by a notepad .txt
#Binary files - one containing binary codes  - .dat , .png ....

#opening a file using python 
open ("sample.txt") 
#closing a file in python 
close 

#A better way to do it 
file = open ("sample.txt") # defining a variable will make it easy to call functions
#file = open ("c://Desktop/sample.txt") #open absolute path 
file.close()

#Yet better way to do it, using with statement 
with open ("sample.txt", "r") as f:
    f.read() #thats the end no need to close by f.close()
    


#Different modes - read , write , append , update , creation , 
#Files open in read mode by default 


file = open ("sample.txt" , "r") #"r" stands for read, it will just read contents from file and won't change anything
file.close()

file = open ("sample.txt" , "w") #"w" stands for write, it will rewrite everything in a .txt file
file.write ("This will rewrite everythin in .txt \n")
file.close()

file = open ("sample.txt" , "a") #"a" stands for append, it will add the changes at the end of the file, its a branch of write itself
file.write ("This will add the statement at the end of the existing file \n")
file.close()

'''UNCOMMENT THE LINES BELOW ONE BY ONE AND CHECK RESULT ! ! !'''

# file = open ("sample.txt" , "r+") #"+" stands for read and write (update) w+ = read and rewrite all contents , r+ = read and write at the beginnig of the file , a+ =  ead and write at the end of the file
# file.read() #read 
# file.write ("this will update") #Write
# file.close()

# file2 = open ("sample2.txt", "x") #create a file named sample2.txt
# file2.write ("add this statement in file")
# file2.close

#some more functions
'''UNCOMMENT THE LINES BELOW ONE BY ONE AND CHECK RESULT ! ! !'''
#writelines()
#file = open ("sample.txt", "a")
# file.writelines(["IT WILL PRINT" , "ALL ELEMENTS" , "OF A LIST"] )
# file.close

# #readline
# file = open ("sample.txt", "r")
# print (file.readline(2)) #reads 1 line at a time if no value of n is given else reads first n characters from 1 line
# print (file.readline()) #reads 2nd line
# print (file.readline()) #reads 3rd line 
# print (file.readline()) #reads 4th line
# file.close

# #readlines
# file = open ("sample.txt", "r")
# print (file.readlines()) #print all lines in a form of a list - line 1 = 1st element of list and ........
# file.close

#Data manupulation in text file - change some content from a text file
#seek() and tell() functions

with open ("sample.txt" , "r+") as f:
    a = f.tell() #tells current position of cursor 
    print (a)
    f.seek (30) #changes the positon of the cursor 
    print((f.read())) #will read after 55 byte/words
    a = f.tell() #tells current position of cursor , here it will be the last position since its reading the whole file
    print (a)

'''Practice 4-
since we've learnt about files, try to improvise the grading program from practice 1. when a student checks the result,save it in a result.txt file
also, if same student checks marks again , make sure that he is unable to update marks in result.txt file'''

'''Practice 5-
since we've learnt about files, try to improvise the grading program from practice 1. make a seperate folder for result (relative path) 
and save file seperate for each student with his/her name written on it! , also read the result from the file and print it '''
#use of data manupulation irl
#fixing spelling error or replacing a word with another

with open ("data_manupulation.txt" , "r") as d: #Open as read to read the default content 
    print("Below are the default contents of the text file- \n \n")
    c = d.read()
    print (c)
with open ("data_manupulation.txt" , "w+") as d: #opening in write mode 
    existing_word = (str(input("Enter the word you want to replace - ")))
    new_word = (str(input("Enter the new word - ")))
    a = c.replace (existing_word, new_word)
    d.write(a)
    d.seek(0) #after writing go back to starting 
    print("Below is the updated content of the text file- \n \n")
    print (d.read())

#binary files basics
#pickle modue is used to read or write binary files 
import pickle #importing the module 
#use of pickle.dump() function - write text(list/dictonary) in form of a binary file 
binary_list = ["Convert this to binary form", "convert this item as well", "Why leaving me, convert me as well"] #list with 3 items
#Open binary file in write mode
with open ("binaryfile.dat" , "wb") as b: #opening a binary file binaryfile.dat, if you don't have that file,python will make a new file with that name
    pickle.dump(binary_list , b) #write contents of list in binary file b 

#now that we have a binary file, let's see how to print contents from it in python
with open ("binaryfile.dat", "rb") as d: #opening binary file in read mode
    printing = pickle.load(d) #load contents from d
    print (printing) #print the loaded content from binary file 

#all modes read,write,append works same in binary...its just followed by "b"

'''Congratulations, this marks the end of python basics, now just lear about object oriented programming and take an advance course in any field which you want !!!'''

#THIS CODE IS WRITTEN BY @icecrac34r 
#https://github.com/icecrac34r/
