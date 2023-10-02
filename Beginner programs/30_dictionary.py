mydict={
     #key ---> #value    
    "Fast": "in a quick manner",
    "yash": "a student",
    "marks": [90,70,33],
    "anotherdict":{'yash':'player'}
}

print(mydict['Fast'])
print(mydict['yash'])
mydict['marks']=[60,50,36]#we can change value of dictionary
print(mydict['marks'])
print(mydict['anotherdict']['yash'])