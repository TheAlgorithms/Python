"""
LCS Problem Statement: Given two sequences, find the length of longest subsequence present in both of them.
A subsequence is a sequence that appears in the same relative order, but not necessarily continious.
Example:"abc", "abg" are subsequences of "abcdefgh". 
"""
def LCS(x,y):
    b=[[] for j in range(len(x)+1)]
    c=[[] for i in range(len(x))]
    for i in range(len(x)+1):
        b[i].append(0)
    for i in range(1,len(y)+1):
        b[0].append(0)
    for i in range(len(x)):
        for j in range(len(y)):
            if x[i]==y[j]:
                b[i+1].append(b[i][j]+1)
                c[i].append('/')
            elif b[i][j+1]>=b[i+1][j]:
                b[i+1].append(b[i][j+1])
                c[i].append('|')
            else :
                b[i+1].append(b[i+1][j])
                c[i].append('-')            
    return b,c


def print_lcs(x,c,n,m):
    n,m=n-1,m-1
    ans=[]
    while n>=0 and m>=0:
        if c[n][m]=='/':
            ans.append(x[n])
            n,m=n-1,m-1
        elif c[n][m]=='|':
            n=n-1
        else:
            m=m-1 
    ans=ans[::-1]
    return ans                   
                       

if __name__=='__main__':
    x=['a','b','c','b','d','a','b']
    y=['b','d','c','a','b','a']
    b,c=LCS(x,y)
    print('Given \nX : ',x)
    print('Y : ',y)
    print('LCS : ',print_lcs(x,c,len(x),len(y)))
