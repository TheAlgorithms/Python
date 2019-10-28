#factors of a number
num=int(input("Enter a number to find factors="))
b=[]
c=0
for i in range(1,num+1):
        if num%i==0:
                b.append(i)
                c+=1
print("The factors of",num,"are=",b)
print('Number of factors of',num,'are=',c)
