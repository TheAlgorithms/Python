print("Enter height and length of the mat with a space in between \nExample:- \n9 10")
a = input().split()
height = int(a[0])
width = int(a[1])
half_height = height//2
c1=0
for i in range(half_height,0,-1):
    print(("-"*3*i)+"."+("|.."*c1)+"|"+("..|"*c1)+"."+("-"*3*i))
    c1+=1
print("WELCOME".center(width,"-"))
for j in range(1,half_height+1):
    c1-=1
    print(("-"*3*j)+"."+("|.."*c1)+"|"+("..|"*c1)+"."+("-"*3*j))
