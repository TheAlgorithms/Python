s=input("Enter Time: ")
if s[8]=='A':
    l=s.rstrip('AM').split(':')
    op=l[0]
    if op =='12':
        op='00'
        l.insert(0,op)
        l.remove('12')
        m=''
        for i in l:
            m+=i+':'
        print(m.rstrip(':'))
    else:
        m=''
        for i in l:
                m+=i+':'
        print(m.rstrip(':'))
else:
    s1=s.rstrip('PM')
    k=s1.split(':')
    op=k[0]
    if op=='12':
        k.insert(0,op)
        k.remove('12')
        m=''
        for i in k:
            m+=i+':'
        print(m.rstrip(':'))
    else:
        op2=int(op)
        op2+=12
        op3=str(op2)
        k.insert(0,op3)
        k.remove(op)
        m=''
        for i in k:
            m+=i+':'
        print(m.rstrip(':'))
