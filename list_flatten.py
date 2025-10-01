a=[1,2,3,[4],[3,[4,5,6,[7]]],[8,9,[10],11]]


    
print(a)
res=[]
def flatten(element):
    if isinstance(element,int):
        res.append(element)
    else:
        for i in element:
            flatten(i)

for data in a:            
    flatten(data)
    
print(res)



