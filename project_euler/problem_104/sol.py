"""
Project Euler Problem 104 : https://projecteuler.net/problem=104

The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
It turns out that F541, which contains 113 digits, is the first Fibonacci number for which the last nine digits are 1-9 pandigital (contain all the digits 1 to 9, but not necessarily in order). And F2749, which contains 575 digits, is the first Fibonacci number for which the first nine digits are 1-9 pandigital.

Given that Fk is the first Fibonacci number for which the first nine digits AND the last nine digits are 1-9 pandigital, find k.

"""


def check(a : int) ->bool : 
  '''
  Takes a number and checks if it is pandigital both from start and end


  >>> check(123456789987654321)
  True

  >>> check(120000987654321)
  False

  >>> check(1234567895765677987654321)
  True

  '''

  checkLast=[0]*11 
  checkFront=[0]*11
  
  #mark last 9 numbers
  for x in range(9):
      checkLast[int(a%10)]=1
      a=a//10
  #flag
  f=True

  #check last 9 numbers for pandigitality
  
  for x in range(9):
      if( not checkLast[x+1]):
          f=False
  if(not f):
    return f
  
  
  #mark first 9 numbers
  a= int(str(a)[:9])
  
  for x in range(9):
      checkFront[int(a%10)]=1
      a=a//10

  #check first 9 numbers for pandigitality

  for x in range(9):
      if( not checkFront[x+1]):
          f=False
  return f




def check1(a : int) ->bool:
  '''
  Takes a number and checks if it is pandigital from END


  >>> check1(123456789987654321)
  True

  >>> check1(120000987654321)
  True

  >>> check1(12345678957656779870004321)
  False

  '''

  checkLast=[0]*11 
  
  #mark last 9 numbers
  for x in range(9):
      checkLast[int(a%10)]=1
      a=a//10
  #flag
  f=True

  #check last 9 numbers for pandigitality
  
  for x in range(9):
      if( not checkLast[x+1]):
          f=False
  return f


def solution()->int:
    """
    Outputs the answer ie the least fib number pandigital from both sides.
    >>> solution()
    329468
    """

    a=1
    b=1
    c=2
    # temporary fibonacci numbers

    a1=1
    b1=1
    c1=2
    # temporary fibonacci numbers mod 1e9

    #mod m=1e9, done for fast optimisation
    tocheck=[0]*1000000
    m=1000000000

    for x in range(1000000):
        c1= (a1+b1)%m
        a1=b1%m
        b1=c1%m
        if(check1(b1)):
            tocheck[x+3]=1
        

    for x in range(1000000) :
        c= (a+b)
        a=b
        b=c
        #perform check only if in tocheck
        if(tocheck[x+3] and check(b)):
            return x+3 #first 2 already done
        

if __name__ == "__main__":
    print(f"{solution() = }")
