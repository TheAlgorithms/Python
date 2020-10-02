ans="yes"
l1=[]
Sum=i=0
'''
Enter n numbers
'''
while ans=="yes":
  '''
  check for invalid input
  '''	
  try:
    n=int(input("Enter the number :"))
    l1.append(n)      #adding elements to the list
  except:
    i+=1
    if i>=1:
        print("Enter a valid integer !")
        continue
    
    try:
      print("Enter a valid integer !")  
      n=int(input("Enter the number :"))
      l1.append(n)    #adding elements to the list
    except:
        continue
    
    
  ans=input("Do you want to add more numbers? (yes/no) :")
'''
finding the sum n numbers
'''
for i in range(0,len(l1)):
  Sum+=l1[i]
print("Sum of numbers is :",Sum)

        
    






