'''
Find the sum of n numbers
'''
def add():
	ans="y"
    list1=[]
    sum1=i=0
'''
Enter n numbers
'''
    while ans=="y":
'''
check for invalid input
'''	
      try:
        num=int(input("Enter the number :").strip())
        list1.append(num)      #adding elements to the list
      except:
        i+=1
        if i>=1:
            print("Enter a valid integer !")
            continue
        try:
          print("Enter a valid integer !")  
          num=int(input("Enter the number :").strip())
          list1.append(num)    #adding elements to the list
        except:
            continue
    
    
      ans=input("Do you want to add more numbers? (y/n) :").strip()
'''
finding the sum n numbers
'''
    for i in range(0,len(list1)):
      sum1+=list1[i]
    print("Sum of numbers is :",sum1)

if __name__=="__main__":
	add()