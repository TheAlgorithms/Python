from time import time
abc=time()
for u in range(1000,123456781239):
    puan=0
    for x in range(2,21):
        if(u%x==0):
            puan+=1
        else:
            break
    if(puan==19):
        print(u)
        break
    if(puan>15):
        print(puan,u)
print(time()-abc)
