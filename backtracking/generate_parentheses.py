"""
Given 'n' pairs of parentheses,
this program generates all combinations of parentheses.

Example, n = 3 :
[
   "((()))",
   "(()())",
   "(())()",
   "()(())",
   "()()()"
]

This problem can be solved using the concept of "BACKTRACKING". 

By adding an open parenthesis to the solution and 
recursively add more till we get 'n' open parentheses. 

Then we start adding close parentheses until the solution is valid 
(open parenthesis is closed). 

If we reach a point where we can not add more parentheses to the solution,
we backtrack to the previous step and try a different path.
"""

def generate_parentheses(n)->None:
    """

    >>> generate_parentheses(3)
    ['((()))', '(()())', '(())()', '()(())', '()()()']

    >>> generate_parentheses(1)
    ['()']

    >>> generate_parentheses(0)
    ['']
    
    """
    def backtrack(x='', left=0, right=0)->None:
        if len(x) == 2 * n:
            sol.append(x)
            return
        if left < n:
            backtrack(x+'(', left+1, right)
        if right < left:
            backtrack(x+')', left, right+1)

    sol = []
    backtrack()
    return sol

def main() -> None:
    print(generate_parentheses(3))

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    main()
