#Created by Vismaya 
#This python program finds the duplicate elements in any string


string=input("Enter a string:").strip())
set_dupli=set({})
for i in string:
    count=0
    for j in string:
        if(i==j):
            count+=1
    if(count>1):
        set_dupli.add(i)
print("Duplicate elements are: {}".format(set_dupli))
