# Author: OMKAR PATHAK

import Stack

def isOperand(char):
    return (ord(char) >= ord('a') and ord(char) <= ord('z')) or (ord(char) >= ord('A') and ord(char) <= ord('Z'))

def precedence(char):
    if char == '+' or char == '-':
        return 1
    elif char == '*' or char  == '/':
        return 2
    elif char == '^':
        return 3
    else:
        return -1

def infixToPostfix(myExp, myStack):
    postFix = []
    for i in range(len(myExp)):
        if (isOperand(myExp[i])):
            postFix.append(myExp[i])
        elif(myExp[i] == '('):
            myStack.push(myExp[i])
        elif(myExp[i] == ')'):
            topOperator = myStack.pop()
            while(not myStack.isEmpty() and topOperator != '('):
                postFix.append(topOperator)
                topOperator = myStack.pop()
        else:
            while (not myStack.isEmpty()) and (precedence(myExp[i]) <= precedence(myStack.peek())):
                postFix.append(myStack.pop())
            myStack.push(myExp[i])

    while(not myStack.isEmpty()):
        postFix.append(myStack.pop())
    return ' '.join(postFix)

if __name__ == '__main__':
    myExp = 'a+b*(c^d-e)^(f+g*h)-i'
    myExp = [i for i in myExp]
    print('Infix:',' '.join(myExp))
    myStack = Stack.Stack(len(myExp))
    print('Postfix:',infixToPostfix(myExp, myStack))

    # OUTPUT:
    # Infix: a + b * ( c ^ d - e ) ^ ( f + g * h ) - i
    # Postfix: a b c d ^ e - f g h * + ^ * + i -
