#Python Program to find *first Non Duplicate* character in a string
s=input("Enter the string: ")#ask user for input string
#s.lower()#uncomment for a case sensitive check
hb = dict()#empty dictionary to store frequency of each character in the string
for i in range(len(s)):#loop over the entire string
    if s[i] in hb:#if character is already present in the dictionary, increment its frequency by 1
        hb[s[i]]+=1
    else:
        hb[s[i]]=1#else set its frequency to 1 on first occurence
        
for k,v in hb.items():#loop over the dictionary to find character with frequncy 1
    if v==1:
        print(s.index(k)+1)#print character position
        break
else:
    print(-1)#else print -1