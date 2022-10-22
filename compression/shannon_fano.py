'''
Wiki Explanation: https://en.wikipedia.org/wiki/Shannon%E2%80%93Fano_coding
'''
class  node :
    def __init__(self) -> None:
        self.sym=''
        self.pro=0.0
        self.arr=[0]*20
        self.top=0
p=[node() for _ in range(20)]
 
def shannon_fano(l, h, p):
    pk1 = 0; pk2 = 0; dif1 = 0; dif2 = 0
    if ((l + 1) == h or l == h or l > h) :
        if (l == h or l > h):
            return
        p[h].top+=1
        p[h].arr[(p[h].top)] = 0
        p[l].top+=1
        p[l].arr[(p[l].top)] = 1
         
        return
     
    else :
        for i in range(l,h):
            pk1 = pk1 + p[i].pro
        pk2 = pk2 + p[h].pro
        dif1 = pk1 - pk2
        if (dif1 < 0):
            dif1 = dif1 * -1
        j = 2
        while (j != h - l + 1) :
            k = h - j
            pk1 = pk2 = 0
            for i in range(l, k+1):
                pk1 = pk1 + p[i].pro
            for i in range(h,k,-1):
                pk2 = pk2 + p[i].pro
            dif2 = pk1 - pk2
            if (dif2 < 0):
                dif2 = dif2 * -1
            if (dif2 >= dif1):
                break
            dif1 = dif2
            j+=1
         
        k+=1
        for i in range(l,k+1):
            p[i].top+=1
            p[i].arr[(p[i].top)] = 1
             
        for i in range(k + 1,h+1):
            p[i].top+=1
            p[i].arr[(p[i].top)] = 0
             
 
        shannon_fano(l, k, p)
        shannon_fano(k + 1, h, p)
     
 
def ProbabilitySort(n, p):
    temp=node()
    for j in range(1,n) :
        for i in range(n - 1) :
            if ((p[i].pro) > (p[i + 1].pro)) :
                temp.pro = p[i].pro
                temp.sym = p[i].sym
 
                p[i].pro = p[i + 1].pro
                p[i].sym = p[i + 1].sym
 
                p[i + 1].pro = temp.pro
                p[i + 1].sym = temp.sym
             
         
def display(n, p):
    print("\n\n\n\tSymbol\tProbability\tCode",end='')
    for i in range(n - 1,-1,-1):
        print("\n\t", p[i].sym, "\t\t", p[i].pro,"\t",end='')
        for j in range(p[i].top+1):
            print(p[i].arr[j],end='')
     
 
if __name__ == '__main__':
    total = 0
 
    n=int(input("Enter number of symbols\t: "))
    i=0
    # Input symbols
    for i in range(n):
        ch=input("Enter symbol {} : ".format(i+1))
 
        p[i].sym += ch
     
 
    # Input probability of symbols
    x = [None] * n
    for i in range(n):
        x[i]=float(input("\nEnter probability of {} : ".format(p[i].sym)))
 
        p[i].pro = x[i]
        total = total + p[i].pro
 
        # checking max probability
        if (total > 1) :
            print("Invalid. Enter new values")
            total = total - p[i].pro
            i-=1
         
     
    i+=1
    p[i].pro = 1 - total
    ProbabilitySort(n, p)
 
    for i in range(n):
        p[i].top = -1
 
    shannon_fano(0, n - 1, p)
 
    # display codes
    display(n, p)