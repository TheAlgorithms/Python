mydict={
     #key ---> #value    
    "fast": "in a quick manner",
    "yash": "a student",
    "marks": [90,70,33],
    "anotherdict":{'yash':'player'},
    1:2

}
# dictionary methods
print(list(mydict.keys()))#prints the keys of the dictionary
print(mydict.values())#prints the value of the dictionary
print(mydict.items())#prints the (key,values) for all contents of the dictionary
print(mydict)
updatedict={
    "lovish":"freind",
    "divya":"friend",
    "shubham":"friend",
    "yash": "a dancer"
}
mydict.update(updatedict)# updates the dictionary by adding key-value pairs from updatedict
print(mydict)
print(type(mydict.keys()))

#the difference between .get and [] syntax in dictionaries ? 

print(mydict.get("yash")) # prints the value associated with yash key 
print(mydict["yash"]) # prints the value associated with yash key 

print(mydict.get("yash2")) # this line will not show error it will return none as a output
print(mydict["yash2"]) # this line will throw an error


# for more methods you will search on google --> python dictionary methods