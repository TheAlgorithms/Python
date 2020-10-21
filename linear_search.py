arr = list()
size=int(input("Input the size of list"))
for i in range(0,size):
    ele=int(input("Input element no. %d"%(i+1)))
    arr.append(ele)
print("The inputted list is = {}".format(arr))
flag=int(input("Enter the element to be searched for :")) 
count=0
for i in range(len(arr)):
    if(arr[i]==flag):
        count=count+1
        print("Element %d found at location %d"%(flag,i+1))
if (count == 0):
    print("Element %d is not present in the list"%flag)
print("Element %d found %d times in the list"%(flag,count))