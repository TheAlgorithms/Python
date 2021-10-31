'''
This program is to find (n)th, (n+1)th fibonacci number is very fast and efficient way
The logic is explain below


There is a formula known as "Binet's formula", even though it was already known by Moivre:
Fn=(1+5√2)n−(1−5√2)n5–√

Closed-form expression
This formula is easy to prove by induction, but it can be deduced with the help of the concept of generating functions or by solving a functional equation.

You can immediately notice that the second term's absolute value is always less than 1
, and it also decreases very rapidly (exponentially). Hence the value of the first term alone is "almost" Fn

. This can be written strictly as:
Fn=⎡⎣⎢(1+5√2)n5–√⎤⎦⎥

where the square brackets denote rounding to the nearest integer.

Matrix form

It is easy to prove the following relation:
(Fn−1Fn)=(Fn−2Fn−1)⋅(0111)

Denoting P≡(0111)

, we have:
(FnFn+1)=(F0F1)⋅Pn

Thus, in order to find Fn
, we must raise the matrix P to n. This can be done in O(logn)

(see Binary exponentiation).
Fast Doubling Method

Using above method we can find these equations:
F2k F2k+1=Fk(2Fk+1−Fk).=F2k+1+F2k.

Thus using above two equations Fibonacci numbers can be calculated easily by the following code:

'''

# Use function fibonacci(n) for nth fibonaci number
# Use function fib(n) for nth and (n+1)th fibonaci number. The result will in the form of list.

#Time complextity T(n) =  O(logn)

def fib(n):
    if n == 0:
        return [0,1]
    p = fib(n>>1)
    c = p[0]*(2 * p[1] - p[0])
    d = p[0] * p[0] + p[1] * p[1];
    if n & 1:
        return [d, c+d]
    else:
        return [c,d]

def fibonacci(n):
  temp = fib(n)
  return temp[0]


print(fib(5))
