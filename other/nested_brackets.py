'''
The nested brackets problem is a problem that determines if a sequence of
brackets are properly nested.  A sequence of brackets s is considered properly nested
if any of the following conditions are true:

	- s is empty
	- s has the form (U) or [U] or {U} where U is a properly nested string
	- s has the form VW where V and W are properly nested strings

For example, the string "()()[()]" is properly nested but "[(()]" is not.

The function called is_balanced takes as input a string S which is a sequence of brackets and
returns true if S is nested and false otherwise.

'''


def is_balanced(S):

    stack = []
    
    for i in range(len(S)):
        
        if S[i] == '(' or S[i] == '{' or S[i] == '[':
            stack.append(S[i])
            
        else:
            
            if len(stack) > 0:
                
                pair = stack.pop() + S[i]
                
                if pair != '[]' and pair != '()' and pair != '{}':
                    return False
                
            else:
                return False
                
    if len(stack) == 0:
        return True
        
    return False


def main():

    S = input("Enter sequence of brackets within quotes: ")

    if is_balanced(S):
        print S, "is balanced"
    
    else:
	print S, "is not balanced"


if __name__ == "__main__":
    main()
