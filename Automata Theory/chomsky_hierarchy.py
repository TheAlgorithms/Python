# ---------------------Implementing Chomsky Hierarchy--------------------
# For background understanding, refer https://www.geeksforgeeks.org/chomsky-hierarchy-in-theory-of-computation/ 
# Taking input from user
v=input("Enter non-terminals(Click enter if done): ").split()
t=input("Enter terminals(Click enter if done): ").split()
t.append('$')
p=list()  
print("Please enter details for your productions now \n Note that \n 1) If a production is like A->aB|b, give it as two separate productions like \n A->aB \n A->b \n 2) Give $ for empty string")
n=input("Enter number of productions: ")
for i in range(int(n)):
    p.append(input(F"Give production {i+1}: "))

# defining global variable
prodtypehighest=[]  # list to store highest type for each production

# function to check left linear 
def ll(rightofproduction: str)->bool:
    lst=list(rightofproduction)
    if lst[0] in v:
        for char in lst[1:]:
            if char not in t:
                return False
        return True
    else: 
        return False
    
# function to check right linear 
def rl(rightofproduction: str)->bool:
    lst=list(rightofproduction)
    if lst[-1] in v:
        for char in lst[:-1]:
            if char not in t:
                return False
        return True
    else: 
        return False

# function to check the special case for type 1 grammar
def check_specialcase(productions_list: list)->bool:
    flag=0
    start_symbol= productions_list[0].split('->')[0]
    for p in productions_list:
        if p==start_symbol+'->$':
            flag=1
            break
    if flag==1:
        for p in productions_list:
            lhs=p.split('->')[0]
            rhs=p.split('->')[1]
            if lhs==start_symbol:  # means it's not a further production
                continue
            else:
                for char in rhs:
                    if char==start_symbol:
                        return True
        return False
    else:
        return False
        
# function to check if given grammar is a mixture of left linear and right linear
def check_mixture_of_ll_rl(productions_list: list)->bool:
    lst=['']*len(productions_list) 
    i=0
    for p in productions_list:
        r=p.split('->')[1]
        if ll(r)==True:
            lst[i]='ll'
        elif rl(r)==True:
            lst[i]='rl'
        if (ll(r) and rl(r))==True:
            lst[i]='both'
        i=i+1
    first_value=lst[0]
    for item in lst:
        if item!=first_value and item!='':
            return True
    return False

# function to check if all productions of a grammar are type 0
def all_t0(production_list: list)->bool:
    for prod in production_list:
        count=0
        l=[]
        l=prod.split('->')[0]
        for char in l:
            count=count+1
            trueorfalse=char in v
            if trueorfalse == True:
                break
            if count==len(l):
                return False
    return True
    
# function to get the type (0/1/2/3) for a given production α->β 
def get_type(prod: str) -> Any:  
    prodtype='Neither of type 0, type 1, type 2 or type 3'
    flag=0
    l=[];r=[]
    l=prod.split('->')[0]
    r=prod.split('->')[1]
    left=ll(r)
    right=rl(r)
    for char in l:
        trueorfalse=char in v
        if trueorfalse == True:
            prodtype=0
            break
    if prodtype==0 and len(l)<=len(r):
        prodtype=1
    if prodtype==1 and len(l)==1:
            prodtype=2
    if prodtype==2:
        if r=='$':
            prodtype=3
        elif (left or right) and not(left and right):
            prodtype=3
        else:
            for char in r:
                if char not in t: 
                     flag=1
                     break
            if (flag != 1):
                prodtype=3
    return prodtype

# getting and storing highest type for each production of the grammar
for i in p:
    prodtypehighest.append(get_type(i))

# type of grammar will be the highest 'common' type for all its productions
result=min(prodtypehighest)

# checking for special case of type 1 grammar
if check_specialcase(p):
    if all_t0(p)==True:
        result=0
    else:
        result='Neither of type 0, type 1, type 2 or type 3'

# checking for mixture of left linear and right linear grammar
if result==3:
    if check_mixture_of_ll_rl(p):
        result=2

# printing the result to user
print("The grammar is of type -",result)

# doctests
import doctest
doctest.testmod()
