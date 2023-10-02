''' this program is for finding the given username is of 10 letters or not
user=input("Enter a valid username\n")

if(len(user)>=10):
    print("it is a valid username")
else:
    print("sorry! please enter a valid username")
'''
# Another program for finding given name is present in list or not
names=["yash","naksh","patel","harshita","shubham","rohit","rohan","aditi"]
name=input("Enter the name to check\n")
if(name in names):
    print("Your name is present in the list")
else:
    print("Your name is not present in the list")