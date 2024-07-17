class permutation:
    def __init__(self):
        self.__n=int(input('array size : '))
        self.__arr=[]
        for i in range (0,self.__n):
            a=input(f'input for idx {i}: ')
            self.__arr.append(int(a))
    
    def __get_permutations(self,lst,res,arr,n):
        if(len(lst)==n):
            res.append(lst[:])
            return
        for i in range (0,len(arr)):
            lst.append(arr[i])
            self.__get_permutations(lst,res,arr[0:i]+arr[i+1:],n)
            lst.pop()
        
    def compute_permutations(self):
        lst=[]
        res=[]
        self.__get_permutations(lst,res,self.__arr,self.__n)
        print('the permutations are\n')
        print(res)

a=permutation()
a.compute_permutations()
        
