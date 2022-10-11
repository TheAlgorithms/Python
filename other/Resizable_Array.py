class resizable_array:
    def __init__(self,arraysize):
        self.arraysize = arraysize
        self.array = [None for i in range(self.arraysize)]
        self.temp =1
    def __insert(self,value):

        for i in range(len(self.array)):

            if self.array[i] == None:
                self.array[i] = value
                break

        #print(self.array)
        #return self.array

    def insert_at_end(self, value):

        if None not in self.array :
            self.newsize= self.temp+len(self.array)
            self.newarray = [None for i in range(self.newsize)]
            for i in range(len(self.array)):
                self.newarray[i]=self.array[i]
                # temp contains value of i
                i_temp=i

            self.newarray[i_temp+1]=value
            self.array = self.newarray
            self.newarray = None
            #print(self.array)
            #return self.array
        else:
            self.__insert(value)
    def printarray(self):
        return self.array

    def insert_at_first(self, value):
        self.create_new_size = len(self.array)+1
        self.create_new_size = ['insert' for i in range(self.create_new_size)]
        self.create_new_size[0] = value
        n = len(self.array)
        for i in range(1,n+1):
            self.create_new_size[i] = self.array[i-1]
        self.array = self.create_new_size
        self.create_new_size = None
        #print(self.array)
        #return self.array

    def delete_at_end(self):
        if len(self.array) == 0:
            print("Array is empty")
        else:
            self.newsize = len(self.array)-1
            self.newarray = [None for i in range(self.newsize)]
            for i in range(len(self.array)-1):

                self.newarray[i] = self.array[i]
            self.array=self.newarray
            #print(self.array)
            #return(self.array)

    def delete_at_first(self):
        
        if len(self.array) == 0:
            print('Array is empty!')
        else:
            if len(self.array)==1:
                self.array =[]
            else:
                self.create_new_size = len(self.array) - 1
                self.newarray = ['insert' for i in range(self.create_new_size)]
                n = len(self.newarray)
                for i in range(0,n):
                    self.newarray[i] = self.array[i+1]
                self.array = self.newarray
                self.newarray = None
                #print(self.array)
                #return self.array

    def insert_at_middle(self, insertafter, insertedvalue):

        self.create_new_size = len(self.array) + 1
        self.newarray = [None for i in range(self.create_new_size)] #3

        n = len(self.array)-1 #2
        if self.array[n] == insertafter:
            self.insert_at_end(insertedvalue)
        elif insertafter in self.array:
            for i in range(0, n):

                if self.array[i] == insertafter:

                    self.newarray[i] = self.array[i]
                    self.newarray[i + 1] = insertedvalue
                    i = i + 2
                    break

                else:
                    self.newarray[i] = self.array[i]

            for j in range(i , len(self.newarray)):
                self.newarray[j] = self.array[j - 1]

            self.array = self.newarray
            self.newarray = None
            #print(self.array)
            #return self.array
        else:
            print("value does not exists in Array after which you want to insert new value!")

    def shrink(self,value):
        self.create_new_size = len(self.array)-1
        self.newarray = [None for i in range(self.create_new_size)]
        flag=False
        if len(self.array)==0:
            print("Array is empty!")
        else:
            for i in range(len(self.array)):
                try:
                    if self.array[i]!=value and flag == False:
                        self.newarray[i]=self.array[i]
                    elif flag == True or self.array[i]==value:
                        self.newarray[i]=self.array[i+1]
                        flag = True
                    else:
                        flag=True
                except:
                    pass
            self.array=self.newarray
            self.newarray=None
            #print(self.array)
            #return self.array
    def maximum_value(self):
        max=self.array[0]
        for i in range(len(self.array)):
            for j in range(len(self.array)):
                if max<self.array[j]:
                    max = self.array[j]
        print("maximum value in array is: {}".format( max))
        return max
    def minimum_value(self):
        min=self.array[0]
        for i in range(len(self.array)):
            for j in range(len(self.array)):
                if min>self.array[j]:
                    min = self.array[j]
        print("minimum value in array is: {}".format(min))
        return min


ob1= resizable_array(1)

print("\n---------Initial Array---------")
print(ob1.printarray())

print("\n---------Insert at End---------")
ob1.insert_at_end(5)
ob1.insert_at_end(6)
ob1.insert_at_end(7)
ob1.insert_at_end(7.5)
print(ob1.printarray())

print('\n---------Insert at First---------')
ob1.insert_at_first(4)
ob1.insert_at_first(3)
ob1.insert_at_first(2)
ob1.insert_at_first(1)
ob1.insert_at_first(0.5)
print(ob1.printarray())

print('\n---------Delete at First---------')
ob1.delete_at_first()
print(ob1.printarray())

print("\n---------Delete at End---------")
ob1.delete_at_end()
print(ob1.printarray())


print("\n---------Insert at Middle--------- ")
ob1.insert_at_middle(5, 5.5)
ob1.insert_at_middle(6, 6.5)
ob1.insert_at_middle(7, 7.5)
print(ob1.printarray())
ob1.insert_at_middle(8, 88)

print("\n---------Shrink--------- ")
ob1.shrink(5.5)
ob1.shrink(6.5)
ob1.shrink(7.5)
print(ob1.printarray())
print("\n---------Maximum Value--------- ")
ob1.maximum_value()

print("\n---------Minimum Value--------- ")
ob1.minimum_value()
