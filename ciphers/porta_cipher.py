alpha=[]
alpha2=[]



key= "college"
start_letter="p"
plain= "ELECTRONICS"

"""
college

main:      abcdefghijklmnopqrstuvwxyz
mapped to :hijkmnpqrstuvwxyzcolegabdf
"""

def porta(key,st,plain):
    
    key=key.upper()
    st=st.upper()
    plain=plain.upper()
    c=[]
    ind=0
    for i in range(0,26):
        alpha2.append('0')

    for i in range(65,91):
        alpha.append(chr(i))


    for i in range(len(key)):
        if key[i] not in c:
            c.append(key[i])


    ind=alpha.index(st)

    i=ind

    m=0
    k=0
    count=0

    temp_key=[]

    for i in key:
        if i not in temp_key:
            temp_key.append(i)

    L=len(temp_key)
    i=0

    while count <(26+L) :
        if i>=26:
            i=0
        if k<len(c):
            alpha2[i]=c[k]
            k+=1
            i+=1
        elif alpha[m] in c:
            m+=1
        elif (alpha[m] not in c) and m<26:
            alpha2[i]=alpha[m]
            m+=1
            i+=1
        count+=1

    cipher=[]

    for i in range(len(plain)):
            for j in range(len(alpha)):
                if plain[i]==alpha[j]:
                    for k in range(len(alpha2)):
                        if(j==k):
                            cipher.append(alpha2[k])
    cr=""
    for i in cipher:
        cr+=i
    return cr
    
print('Encrypted:',porta(key,start_letter,plain,))

"""
Enter the key: COLLEGE
Enter the index: P
Enter the plain text: ELECTRONICS
Encrypted: GJGLTRNMFLS

"""
