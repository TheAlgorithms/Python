def swap_case(s):
    #This method will swap the cases of a given string
    # eg: input: s= "Hello" output: t="hELLO"
    m=list(s)
    for i in range(len(m)):
        if m[i]>='A' and m[i]<='Z':
            m2=ord(m[i])
            m1=m2+32
            m[i]=chr(m1)
        elif m[i]>='a' and m[i]<='z':
            m3=ord(m[i])
            m4=m3-32
            m[i]=chr(m4)
        else:
            pass
    t=[ele for ele in m]
    t="".join(t)
    return t

s=input()
sc= swap_case(s)
print(sc)
