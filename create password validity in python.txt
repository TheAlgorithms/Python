import time
pwd=input("Enter your password: ")    #any password u want to set

def IInd_func():
  count1=0
  for j in range(5):
    a=0
    count=0
    user_pwd = input("Enter remember password: ")        #password you remember
    for i in range(len(pwd)):
      if user_pwd[i] == pwd[a]:       #comparing remembered pwd with fixed pwd
        a +=1
        count+=1 
    if count==len(pwd):
      print("correct pwd")
      break
    else:
      count1 += 1
      print("not correct")
  if count1==5:
    time.sleep(30)
    IInd_func()

IInd_func()