
#Defining factorial function
def Fac(n):
    if n<0:
        print("n should be no less than 0！")
    elif n==0:
        return 1
    else:
        result=1
        for i in range(1,n+1):
            result=result*i
        return result
 if __name__=='__main__':
     print(Fac(8))
