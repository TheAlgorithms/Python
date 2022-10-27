def josephus(person, k, index):
   
  # when only one person is left
  if len(person) == 1:
    print(person[0])
    return
   
  # find the index of first person which will die
  index = ((index+k)%len(person))
   
   # remove the first person which is going to be killed
  person.pop(index)
   
  # recursive call for n-1 persons
  Josh(person,k,index)
 
n = 14 
k = 2
k-=1   
 
index = 0
 
person=[]
for i in range(1,n+1):
  person.append(i)
 
josephus(person,k,index)