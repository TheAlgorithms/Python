<h2> String </h2>

***Strings are what we use in python when working with words.*** Strings are either enclosed with single quotes or double quotes.Also we can write multi line string using triple qutations(single and double both)
So, we can use either single quotes or double quotes as long as we are consistant about which qutation we are using.
```
my_name = "Hello! I am mouly"
myy_name = 'Helloo! I am Mouly'
x = '''this is
a multi line 
string
that we can write'''
print(my_name)
print(myy_name)
print(x)
```
Output:
```
Hello! I am mouly
Helloo! I am Mouly
this is
a multi line 
string
that we can write
```
We can also make an ***empty string***
```
p = " "                                       #empty string
print(p)
```
Output:
```

```
We can ***concatenate*** strings by using the plus(+) sign.
```
var1 = "we want"
var2 = "to visit a"
var3 = "zoo"
var =  var1 +" "+ var2 +" "+ var3             #concetenation of a string
print(var)
```
Output:
```
we want to visit a zoo
```
Notice one thing, this + sign doesn't add any ***space*** while concatenating. 

***type***

this built-in fuction returns the type of an object
```
name = "alan walker"  
print(type(name))                             #type of name variable
```
Output:
```
<class 'str'>
```
Also,
```
p = "5"                                      #this is a string
q = 5                                        #this is an integer
print(type(p))
print(type(q))
```
Output:
```
<class 'str'>
<class 'int'>
```
Even though p and q might look same to you.. their types are different and there are different consequences for this. 
```
p = "5"
q = 5
print(p)
print(q + 45)
```
Output:
```
5
50
```
but 
```
p = "5"
q = 5
print(p + 45)                                 #this will give an error
print(q)
```
Output:
```
TypeError: can only concatenate str (not "int") to str
```
here, p is a string. Even though 5 happens to look like a number, in python it's just a sequence of characters and we can't add a number to a sequence of characters.
we can add them if we cast this p string into an integer.
```
p = "5"
q = 5
print(int(p) + 45))                          #this won't give an error
print(q)
```
Output:
```
50
5
```
```
p = "5"
print(p + "45")                              #string concetenation
```
Output:
```
545
```
When we call a int of float to cast a string it needs to be a valid number.
```
p = "20 taka"
print(p + 25)
```
Output:
```
TypeError: can only concatenate str (not "int") to str
```
So, python can't convert this string into integer.

Strings are sequential collection datatype.This means a string is actually a collection of single characters.

***Indexing***

We can access a sub-string or part of a string using the indexing operator.
This operator is handy for accessing a single character by it's position or ***index value***
This index value for sequential collection datatypes always begins at ***zero***
For example, string with six character have entities from 0 through 5. So if we want to access a 5th character of a string we'll use an index of 4.
```
xmple = "we want to access"
print(xmple[0])
print(xmple[2])   
print(xmple[8]) 
print(xmple[-1])                                 #negative indexing
```
Output:
```
w

t
s
```
Positive indexing starts from 0 and from the right side while negative indexing starts from the left side,
so we can access the last characters also by using negative indexing.
Yess, the space also counts.
the built-in function ***len()*** can help us determine the length of a string. So the last index of a stirng will always be ***one less*** than the length of that string.
```
xmple = "we want to access"
print(len(xmple))                               #length of a string
```
Output:
```
17
```
If we want to access last character of a string we can do either of them from below:
```
xmple = "we want to access"
print(xmple[len(xmple)-1])
print(xmple[-1])
```
Output:
```
e
e
```
***Slice Operator***

Another way of accessing characters in a stirng is to use the slice operator. This allows us to create a sub-string that is more than one character long.
***Keep in mind*** that, the slice operator leaves the original operator intact.
```
xmple = "we want to access"
print(xmple[1:9:1])
```
Output:
```
e want t
```
In this example,the colon used in this slicing operator will return the characters from index 1 upto index 8(so not including index 9) and the increment will be 1.

***Built-in methods***

***It's important to remember that, Python is immutable*** means they can not be changed.

Python has some built-in method to access or process characters in string.

For example,

***count method***
we can use the count method to count the occurances of a particular substring.
```
place = "I want to visit USA"
print(place.count("i"))
```
Output:
```
2
```
As python is ***case-sensitive,*** we can't access I here cause the ASCII value of I is different than i***

***index method***

we can use the index method to find the index of the ***first occurance*** of a given substring.
```
place = "I want to visit USA"
print(place.index("i"))
```
Output:
```
11
```
***Upper and lower method***

Upper returns the copy of a given string in all uppercase letters; while lower returns the copy of a given string in all lowercase letters.
```
place = "I want to visit USA"
print(place.upper())
print(place.lower())
```
Output:
```
I WANT TO VISIT USA
i want to visit usa
```
upper or lower method takes no arguments.

***strip method***

this strip method returns the copy of a string with the leading and trailing ***whitespaces*** removed.

Whitespaces refers to any character that represents a space in text like a tab,a space or a new line character.

```
new = "   Well this is another line   !     "       #Strips all whitespace characters from both ends.
print(new.strip())
```
Output:
```
Well this is another line   !
```
Notice, the whitespace between characters are not removed, only the leading and trailing whitespaces are removed.

***split method***

Split helps us breaking sentences of a string into more managable pieces.

Split takes a ***delimiter*** and splits the string into sub-strings.The method returns a list where each item is a sub-string that is cut at every instance of that delimeter.

For example,

```
song = "Tell me why? Aint noting but a heartache. Tell me why? Aint noting but a mistake"
print(song.split("?"))
```
Output:
```
['Tell me why', ' Aint noting but a heartache. Tell me why', ' Aint noting but a mistake']
```
This output comes as a list
Here "?" is the delimeter.. so It will cut in those places and won't return the delimeter in output.

```
x = "Library is a place where you can find peace"
print(x.split(" "))
```
Output:
```
['Library', 'is', 'a', 'place', 'where', 'you', 'can', 'find', 'peace']
```
Here my delimeter is a space. So the resulting list will include every word in that sentence but no spaces.
```
x = "Library is a place where you can find peace"
print(x.split("a"))
```
Output:
```
['Libr', 'ry is ', ' pl', 'ce where you c', 'n find pe', 'ce']
```
So, the split method won't include the delimeter in the list it returns.

***join method***

The inverse of the split method is join. We can choose a desired separator string, (often called the glue) and join the list with the glue between each of the elements.

```
x = ["*light blue?", "sky", "it's raining hard","colin, where you go","?*"]
y = "! "
p = y.join(x)
print(p)
```
Output:
```
*light blue?! sky! it's raining hard! colin, where you go! ?*
```
We can also use empty string or multi-character strings as glue.
