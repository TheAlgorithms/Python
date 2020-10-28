"""the problem is write a function who represent the sum of 0,1,2,3,n elements ,where n is a argument from the function.Using backtracking when save the value of manys fibonacci call.
"""
def backtracking_fibonacci(n) :
  saved = [-1 for x in range(n+1)]
  def cal_fib(a) :
    if a == 1: return 0
    if a == 2: return 1
    if saved[a] != -1: return saved[a]
    saved[a] = cal_fib(a-1) + cal_fib(a-2)
    return saved[a]
  return cal_fib(n)
"""the complexy time for this solution is O(n),because for the n ,we call just n cal_fib() with O(1) 
"""    

