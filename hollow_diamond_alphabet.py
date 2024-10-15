def hollow_diamond_alphabet(n):
    '''
       Print a Hollow diamond pattern using alphabets

       Parameters (n) : Size of the hollow diamond. Represeting no.of rows.

       Example:
           n=5
              A
             B C
            D   E
           F     G
          H       I
           F     G
            D   E
             B C
              A    '''   
  
  alpha=64
  for i in range(1,n+1):
      left_spaces=" "*(n-i)
      hollow_spaces=" "*(((i-1)*2)-1)
      if(i==1):
        print(left_spaces+chr(alpha+1))
      else:
        print(left_spaces+chr(alpha)+hollow_spaces+chr(alpha+1))
      alpha+=2
  alpha-=2  
  for i in range(n-1,0,-1):
      left_spaces=" "*(n-i)
      hollow_spaces=" "*(((i-1)*2)-1)
      if(i==1):
        print(left_spaces+chr(alpha-1))
      else:
        print(left_spaces+chr(alpha-2)+hollow_spaces+chr(alpha-1))
      alpha-=2        


n=int(input())
hollow_diamond_alphabet(n)
