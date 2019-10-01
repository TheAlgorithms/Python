s1=input("enter 1st string: ")
s2=input("enter 2nd string: ")
if len(s1)!=len(s2):
   print("strings are not anagram to each other")
else:
   if (set(s1)==set(s2)):
       print("strings are anagram to each other")
   else:
       print("strings are not anagram to each other")
