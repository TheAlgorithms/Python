mydict={
    "pankha":"fan",
    "dabba":"box",
    "vastu":"item"
}
print("options are: ",mydict.keys())
a=input("enter the hindi word\n")
# below line will not throw error if the key is not present in the dictionary
print("the meaning of word is:",mydict.get[a])