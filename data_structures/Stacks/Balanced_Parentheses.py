# Author: OMKAR PATHAK

import Stack

def parseParenthesis(string):
    balanced = 1
    index = 0
    myStack = Stack.Stack(len(string))
    while (index < len(string)) and (balanced == 1):
        check = string[index]
        if check == '(':
            myStack.push(check)
        else:
            if myStack.isEmpty():
                balanced = 0
            else:
                myStack.pop()
        index += 1

    if balanced == 1 and myStack.isEmpty():
        return True
    else:
        return False

if __name__ == '__main__':
    print(parseParenthesis('((()))'))   # True
    print(parseParenthesis('((())'))    # False
