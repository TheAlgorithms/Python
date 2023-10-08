"""
   Given 'n' Pairs of parenthesis,
   this program generates all combinations of parenthesis 
   Example, n=3 :
   [
       "((()))",
       "(()())",
       "(())()",
       "()(())",
       "()()()"
   ]
   This problem is solved using Backtracking 
"""
def solve(op,open,close, ans):
    if(open == 0 and close == 0):
        ans.append(op)
        return
    if(open == close):
        op1 = op
        op1+=('(')
        solve(op1, open-1, close, ans)
    elif(open == 0):
        op1 = op
        op1+=(')')
        solve(op1, open, close-1, ans)
    elif(close == 0):
        op1 = op
        op1+=('(')
        solve(op1, open-1, close, ans)
    else:
        op1 = op
        op2 = op
        op1+=('(')
        op2+=(')')
        solve(op1, open-1, close, ans)
        solve(op2, open, close-1, ans)


def generate_parenthesis(n):
    open = n
    close = n
    ans=[]
    op = ""
    solve(op, open, close, ans)
    return ans
    

print(generateParenthesis(3))
